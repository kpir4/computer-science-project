import db_manager

def degree(adj_table):
    metric_degree = [0] * len(adj_table)

    for node in range(len(adj_table)):
        metric_degree[node] = len(adj_table[node])

    return metric_degree


def normalise(adj_table):
    dbu = db_manager.DatabaseUtility()
    employee_data = dbu.get_eid()

    metric_degree = degree(adj_table)

    for node in range(len(metric_degree)):
        label = employee_data[node][1] + ' ' + employee_data[node][2]
        metric_degree[node] = (label, metric_degree[node] / (count_nodes(adj_table) - 1), node)

    metric_degree.sort(key = lambda x: x[1], reverse = True)

    return metric_degree

def count_nodes(adj_table):
    node_count = 0

    for node in adj_table:
        if len(node) > 0:
            node_count += 1

    return node_count

def weighted_degree(adj_table, adj_matrix, alpha):
    dbu = db_manager.DatabaseUtility()
    employee_data = dbu.get_eid()

    degrees = degree(adj_table)

    metric_weighted_degree = [0] * len(adj_table)

    for i in range(len(adj_matrix)):
        weight = 0
        for j in range(len(adj_matrix)):
            weight += adj_matrix[i][j] + adj_matrix[j][i]

        metric_weighted_degree[i] = degrees[i] ** (1-alpha) + weight ** alpha

    for node in range(len(metric_weighted_degree)):
        label = employee_data[node][1] + ' ' + employee_data[node][2]
        metric_weighted_degree[node] = (label, metric_weighted_degree[node], node)

    metric_weighted_degree.sort(key = lambda x: x[1], reverse=True)

    return metric_weighted_degree


if __name__ == '__main__':
    test = [[1,2,5],[0,2,4],[0,1,3,4,5],[2,4,5],[1,2,3],[0,2,3]]
    result = degree(test)

    for i in result:
        print(str(i))