import db_manager
import networkx as nx
import matplotlib.pyplot as plt

class SocialNetwork:
    def __init__(self):
        self.dbu = db_manager.DatabaseUtility()
        self.employees = self.dbu.get_eid()
        self.comm_matrix = [[0 for i in range(len(self.employees))] for j in range(len(self.employees))]
        self.g = nx.Graph()

    def find_connections(self):
        connections = self.dbu.get_communication()
        for i in range(len(connections)):
            # get_communication() retreives the eid which start from 1 in MySQL
            self.comm_matrix[connections[i][0] - 1][connections[i][1] - 1] = 1

    def find_node_label(self, node1, node2):
        label1 = self.employees[node1][1] + ' ' + self.employees[node1][2]
        label2 = self.employees[node2][1] + ' ' + self.employees[node2][2]
        return label1, label2

    def construct_graph(self):
        for i in range(len(self.comm_matrix)):
            for j in range(len(self.comm_matrix[i])):
                if self.comm_matrix[i][j] == 1:
                    node1, node2 = self.find_node_label(i, j)
                    self.g.add_edge(node1, node2)

    def draw_graph(self):
        # Draw node size based on the node's degrees
        d = nx.degree(self.g)
        d = [(d[node] + 1) * 20 for node in self.g.nodes()]
        nx.draw(self.g, with_labels=True, edge_color = 'b', node_size = d)
        plt.show()
        print(str(nx.closeness_centrality(self.g)))

