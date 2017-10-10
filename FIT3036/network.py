import db_manager
import networkx as nx
import matplotlib.pyplot as plt

def find_node_label(node1, node2):
    label1 = employees[node1][1] + ' ' + employees[node1][2]
    label2 = employees[node2][1] + ' ' + employees[node2][2]
    return label1, label2

dbu = db_manager.DatabaseUtility()
employees = dbu.get_eid()

comm_matrix = [[0 for i in range(len(employees))] for j in range(len(employees))]

connections = dbu.get_communication()
for i in range(len(connections)):
    #print(str(connections[i][0]) + ',' + str(connections[i][1]))
    comm_matrix[connections[i][0]-1][connections[i][1]-1] = 1

g = nx.Graph()

for i in range(len(comm_matrix)):
    for j in range(len(comm_matrix[i])):
        if comm_matrix[i][j] == 1:
            node1, node2 = find_node_label(i, j)
            g.add_edge(node1, node2)

nx.draw(g, with_labels=True)
plt.show()
