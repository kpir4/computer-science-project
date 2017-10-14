def degree(adj_table):
    metric_degree = [0] * len(adj_table)

    for node in range(len(adj_table)):
        metric_degree[node] = len(adj_table[node])

    metric_degree = normalise(metric_degree, adj_table)

    return metric_degree

def normalise(metric_degree, adj_table):
    for node in range(len(metric_degree)):
        metric_degree[node] /= (count_nodes(adj_table) - 1)

    return metric_degree

def count_nodes(adj_table):
    node_count = 0

    for node in adj_table:
        if len(node) > 0:
            node_count += 1

    return node_count


if __name__ == '__main__':
    test = [[1,2,5],[0,2,4],[0,1,3,4,5],[2,4,5],[1,2,3],[0,2,3]]
    result = degree(test)

    for i in result:
        print(str(i))