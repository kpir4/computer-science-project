from queue import deque
import db_manager

def closeness(adj_table):
    dbu = db_manager.DatabaseUtility()
    employee_data = dbu.get_eid()

    nnodes = len(adj_table)
    metric_closeness = [0] * nnodes

    for node in range(nnodes):
        shortest_path_sum = 0
        pred = bfs(adj_table, node)

        for edge in range(nnodes):
            shortest_path_sum += get_shortest_path(pred, edge)

        label = employee_data[node][1] + ' ' + employee_data[node][2]
        # Prevent division by zero error
        if shortest_path_sum > 0:
            metric_closeness[node] = (label, (count_nodes(adj_table) - 1) / shortest_path_sum, node)
        else:
            metric_closeness[node] = (label, 0, node)

    metric_closeness.sort(key = lambda x: x[1], reverse = True)

    return metric_closeness


def bfs(graph, s):
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


def get_shortest_path(pred, u):
    v = u
    path = [v]

    while pred[v] is not None:
        path.append(pred[v])
        v = pred[v]

    return len(path) - 1


def count_nodes(adj_table):
    node_count = 0

    for node in adj_table:
        if len(node) > 0:
            node_count += 1

    return node_count