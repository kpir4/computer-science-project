from queue import deque
import network
from betweenness_centrality import betweenness
from closeness_centrality import closeness
from degree_centrality import degree, normalise
from eigenvector_centrality import eigenvector

class EnronGraph:
    def __init__(self):
        self.net = network.SocialNetwork()
        self.net.find_connections()
        self.adj_matrix = self.net.comm_matrix

        self.adj_table = [[] for _ in range(len(self.net.employee_data))]
        self.construct_adjacency_table()

        self.metric_degree = normalise(self.adj_table)
        self.metric_closeness = closeness(self.adj_table)
        self.metric_betweennness = betweenness(self.adj_table)
        self.metric_eigenvector = eigenvector(degree(self.adj_table), self.adj_matrix,)

    def construct_adjacency_table(self):
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] > 0 and self.adj_matrix[j][i] > 0:
                    self.adj_table[i].append(j)

if __name__ == '__main__':
    c = EnronGraph()
    sort = sorted(c.metric_closeness)
    for i, v in enumerate(sort):
        label = c.net.employee_data[sort[i][1]][1] + ' ' + c.net.employee_data[sort[i][1]][2]
        print(label, v)

    # test = EnronGraph()
    # test.adj_table = [[1,2,5],[0,2,4],[0,1,3,4,5],[2,4,5],[1,2,3],[0,2,3]]
    # test.betweenness()
    #
    # for i, v in enumerate(test.metric_betweennness):
    #     print(i, v)