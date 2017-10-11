from queue import deque
import db_manager

class EnronGraph:
    def __init__(self):
        self.dbu = db_manager.DatabaseUtility()
        self.employees = self.dbu.get_eid()
        self.adj_table = [[] for _ in range(len(self.employees))]
        self.node_closeness = [0] * len(self.employees)

    def construct_adjacency_table(self):
        connections = self.dbu.get_communication()
        for row in connections:
            self.adj_table[row[0]-1].append(row[1]-1)

    def closeness(self):
        for node in range(len(self.employees)):
            shortest_path_sum = 0
            pred = self.bfs(self.adj_table, node)

            for edge in range(len(self.employees)):
                shortest_path_sum += self.get_shortest_path(pred, edge)

            if shortest_path_sum > 0:
                self.node_closeness[node] = (len(self.employees)-1)/shortest_path_sum

        # for node in self.adj_table:
        #     shortest_path_sum = 0
        #     for edge in node:
        #         pred = self.bfs(self.adj_table, curr_node)
        #         shortest_path_sum += self.get_shortest_path(pred, edge)
        #     if shortest_path_sum > 0:
        #         print("Pred: " + str(len(node)))
        #         self.node_closeness[curr_node] = (len(node)-1)/shortest_path_sum
        #     curr_node += 1

    def bfs(self, graph, s):
        visited = [False] * len(graph)
        inqueue = [False] * len(graph)
        dist = [float('inf')] * len(graph)
        pred = [0] * len(graph)
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
        while pred[v] != 0:
            path.append(pred[v])
            v = pred[v]
        return len(path)

c = EnronGraph()
c.construct_adjacency_table()
c.closeness()
for i, v in enumerate(c.node_closeness):
    print(i, v)