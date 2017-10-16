import db_manager
import networkx as nx
import matplotlib.pyplot as plt

class SocialNetwork:
    def __init__(self):
        self.dbu = db_manager.DatabaseUtility()
        self.employee_data = self.dbu.get_eid()
        self.employees = self.get_employees()
        self.comm_matrix = [[0 for i in range(len(self.employee_data))] for j in range(len(self.employee_data))]
        self.g = nx.Graph()

    def get_employees(self):
        employees = {}
        for i in self.employee_data:
            employees[i[3]] = int(i[0])
        return employees

    def find_connections(self):
        connections = self.dbu.get_communication()
        for i in range(len(connections)):
            # get_communication() retreives the eid which start from 1 in MySQL
            if connections[i][0] != connections[i][2]:
                self.comm_matrix[self.employees[connections[i][0]]-1][self.employees[connections[i][2]]-1] += 1

    def find_node_label(self, node1, node2):
        label1 = self.employee_data[node1][1] + ' ' + self.employee_data[node1][2]
        label2 = self.employee_data[node2][1] + ' ' + self.employee_data[node2][2]
        return label1, label2

    def construct_graph(self):
        for i in range(len(self.comm_matrix)):
            for j in range(len(self.comm_matrix[i])):
                if self.comm_matrix[i][j] > 0 and self.comm_matrix[j][i] > 0:
                    node1, node2 = self.find_node_label(i, j)
                    self.g.add_edge(node1, node2, weight = self.comm_matrix[i][j] + self.comm_matrix[j][i])

    def draw_graph(self):
        # Draw node size based on the node's degrees
        d = nx.degree(self.g)
        d = [(d[node] + 1) * 20 for node in self.g.nodes()]
        nx.draw(self.g, with_labels=True, edge_color = 'b', node_size = d)
        plt.show()
        print(str(nx.betweenness_centrality(self.g)))

if __name__ == '__main__':
    test = [[0,1,1,0,0,1],
            [0,0,1,0,1,0],
            [0,0,0,1,0,1],
            [0,0,0,0,1,0],
            [0,1,1,0,0,0],
            [0,0,0,1,0,0]]
    # test = [[0,1,0,0],
    #        [1,0,1,1],
    #        [0,1,0,1],
    #        [0,1,1,0]]
    t = nx.Graph()

    for i in range(len(test)):
        for j in range(len(test[i])):
            if test[i][j] == 1:
                t.add_edge(i, j)

    print(str(nx.degree_centrality(t)))
