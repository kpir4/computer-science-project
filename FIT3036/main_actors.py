from queue import deque
import network
from betweenness_centrality import betweenness
from closeness_centrality import closeness
from degree_centrality import degree, normalise, weighted_degree
from eigenvector_centrality import eigenvector

class EnronGraph:
    def __init__(self):
        self.net = network.SocialNetwork()
        self.net.find_connections()
        self.adj_matrix = self.net.comm_matrix

        self.adj_table = [[] for _ in range(len(self.net.employee_data))]
        self.construct_adjacency_table()

        self.metric_degree = normalise(self.adj_table)
        self.metric_weighted_degree = weighted_degree(self.adj_table, self.adj_matrix, 0.7)
        self.metric_closeness = closeness(self.adj_table)
        self.metric_betweennness = betweenness(self.adj_table)
        self.metric_eigenvector = eigenvector(degree(self.adj_table), self.adj_matrix, 0.000001)

    def construct_adjacency_table(self):
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] > 0 and self.adj_matrix[j][i] > 0:
                    self.adj_table[i].append(j)

    def find_top_actors(self, top_n):
        self.top_actors = set()

        for i in range(top_n):
            self.top_actors.add(self.net.employee_data[self.metric_degree[i][2]][3])

        for i in range(top_n):
            self.top_actors.add(self.net.employee_data[self.metric_weighted_degree[i][2]][3])

        for i in range(top_n):
            self.top_actors.add(self.net.employee_data[self.metric_closeness[i][2]][3])

        for i in range(top_n):
            self.top_actors.add(self.net.employee_data[int(self.metric_betweennness[i][2])][3])

        for i in range(top_n):
            self.top_actors.add(self.net.employee_data[int(self.metric_eigenvector[i][2])][3])
