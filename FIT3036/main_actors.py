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
        self.metric_betweennness = [0] * len(self.adj_table)

        for node in range(len(self.adj_table)):
            pred = self.bfs(self.adj_table, node)

            for edge in range(len(self.adj_table)):

                for node_between in range(len(self.adj_table)):
                    if self.is_between(pred, edge, node_between):
                        self.metric_betweennness[node_between] += 1

        for node in range(len(self.metric_betweennness)):
            self.metric_betweennness[node] = (2 * self.metric_betweennness[node]) / (self.count_nodes()-1) * (self.count_nodes()-2) * (len(self.adj_table) - self.count_nodes())

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

    def is_between(self, pred, s, t, b):
        v = s
        while pred[v] is not None:
            if pred[v] != s and pred[v] != t:
                if pred[v] == b:
                    return True
            v = pred[v]
        return False

if __name__ == '__main__':
    c = EnronGraph()
    c.construct_adjacency_table()
    c.closeness()
    sort = sorted(c.metric_closeness)
    for i, v in enumerate(sort):
        label = c.net.employee_data[sort[i][1]][1] + ' ' + c.net.employee_data[sort[i][1]][2]
        print(label, v)

    # test = EnronGraph()
    # test.adj_table = [[1,2,5],[0,2,4],[0,1,3,4,5],[2,4,5],[1,2,3],[0,2,3]]
    # # close = [0] * len(test.adj_table)
    # #
    # # for node in range(len(test.adj_table)):
    # #     shortest_path_sum = 0
    # #     pred = test.bfs(test.adj_table, node)
    # #
    # #     for edge in range(len(test.adj_table)):
    # #         shortest_path_sum += test.get_shortest_path(pred, edge)
    # #     if shortest_path_sum > 0:
    # #         #print("Shortest Path: " + str(shortest_path_sum))
    # #         close[node] = (len(test.adj_table) - 1) / shortest_path_sum
    #
    # test.metric_betweennness = [0] * len(test.adj_table)
    #
    # for node in range(len(test.adj_table)):
    #     pred = test.bfs(test.adj_table, node)
    #
    #     for edge in range(len(test.adj_table)):
    #
    #         for node_between in range(len(test.adj_table)):
    #             if test.is_between(pred, edge, node, node_between):
    #                 test.metric_betweennness[node_between] += 1
    #
    # for node in range(len(test.metric_betweennness)):
    #     print(test.metric_betweennness[node])
    #     test.metric_betweennness[node] = (test.metric_betweennness[node]) / ((test.count_nodes() - 1) * (
    #     test.count_nodes() - 2))
    #
    # for i, v in enumerate(test.metric_betweennness):
    #     print(i, v)