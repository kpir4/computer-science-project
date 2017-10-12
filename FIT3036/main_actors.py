from queue import deque
import network

class EnronGraph:
    def __init__(self):
        self.net = network.SocialNetwork()
        self.net.find_connections()
        self.adj_matrix = self.net.comm_matrix

        self.adj_table = [[] for _ in range(len(self.net.employee_data))]
        self.metric_closeness = None
        self.metric_betweennness = None

    def construct_adjacency_table(self):
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] > 0 and self.adj_matrix[j][i] > 0:
                    self.adj_table[i].append(j)

    def closeness(self):
        self.metric_closeness = [0] * len(self.adj_table)

        for node in range(len(self.adj_table)):
            shortest_path_sum = 0
            pred = self.bfs(self.adj_table, node)

            for edge in range(len(self.adj_table)):
                shortest_path_sum += self.get_shortest_path(pred, edge)

            if shortest_path_sum > 0:
                self.metric_closeness[node] = ((self.count_nodes()-1)/shortest_path_sum, node)
            ############################## Remove later #####################################
            else:
                self.metric_closeness[node] = (0, node)

    def betweenness(self):
        graph = [set() for _ in range(len(self.adj_table))]

        for i in range(len(self.adj_table)):
            for j in range(len(self.adj_table[i])):
                graph[i].add(self.adj_table[i][j])

        self.metric_betweennness = [0] * len(self.adj_table)

        for i in range(len(self.adj_table)):
            for j in range(len(self.adj_table)):
                if i != j:
                    paths = self.bfs_paths(graph, i, j)

                    counter = [0] * len(self.adj_table)
                    for row in paths:
                        for k in range(len(self.adj_table)):
                            if k != i and k != j and k in row:
                                counter[k] += 1

                    for node in range(len(self.adj_table)):
                        # Prevent division by zero
                        if len(paths) > 0:
                            self.metric_betweennness[node] += counter[node] / len(paths)

        for i in range(len(self.metric_betweennness)):
            # Normalise the betweenness centrality
            self.metric_betweennness[i] = self.metric_betweennness[i] / ((self.count_nodes()-1) * (self.count_nodes()-2))

    def count_nodes(self):
        node_count = 0
        for node in self.adj_table:
            if len(node) > 0:
                node_count += 1
        return node_count

    def bfs(self, graph, s):
        visited = [False] * len(graph)
        inqueue = [False] * len(graph)
        dist = [float('inf')] * len(graph)
        pred = [None] * len(graph)
        queue = deque()
        queue.append(s)
        dist[s] = 0
        while len(queue) != 0:
            u = queue.popleft()
            visited[u] = True
            inqueue[u] = False
            for i in graph[u]:
                if not visited[i] and not inqueue[i]:
                    dist[i] = dist[u] + 1
                    pred[i] = u
                    queue.append(i)
                    inqueue[i] = True
        return pred

    def get_shortest_path(self, pred, u):
        v = u
        path = [v]
        while pred[v] is not None:
            path.append(pred[v])
            v = pred[v]
        return len(path) - 1

    def dfs(self, pred, node, paths, curr_path):
        curr_path.append(node)

        # if path ends
        if len(pred[node]) == 0:
            paths.append(list(reversed(curr_path)))

        for parent in pred[node]:
            self.dfs(pred, parent, paths, curr_path)

        # Backtrack
        curr_path.pop()

    def bfs_paths(self, graph, start, end):
        if len(graph) == 0:
            return []

        queue = deque()
        dist = [float('inf')] * len(graph)
        pred = [set() for _ in range(len(graph))]
        dist[start] = 0
        queue.append(start)

        ans = False
        while len(queue) != 0:
            current = queue.popleft()

            for child in graph[current]:
                if dist[child] == float('inf'):
                    queue.append(child)
                    dist[child] = dist[current] + 1
                    pred[child].add(current)
                elif dist[child] == dist[current] + 1:
                    pred[child].add(current)

                if child == end:
                    ans = True

        if ans:
            all_paths = []
            curr_path = []
            self.dfs(pred, end, all_paths, curr_path)
            return all_paths

        return []

if __name__ == '__main__':
    c = EnronGraph()
    c.construct_adjacency_table()
    c.betweenness()
    sort = sorted(c.metric_betweennness)
    for i, v in enumerate(sort):
        #label = c.net.employee_data[sort[i][1]][1] + ' ' + c.net.employee_data[sort[i][1]][2]
        print(i, v)

    # test = EnronGraph()
    # test.adj_table = [[1,2,5],[0,2,4],[0,1,3,4,5],[2,4,5],[1,2,3],[0,2,3]]
    # test.betweenness()
    #
    # for i, v in enumerate(test.metric_betweennness):
    #     print(i, v)