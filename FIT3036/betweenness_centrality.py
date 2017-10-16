from queue import deque
from numpy import load, save
import db_manager

def betweenness(adj_table):
    try:
        metric_betweenness = load("betweenness.npy")
        return metric_betweenness
    except:
        dbu = db_manager.DatabaseUtility()
        employee_data = dbu.get_eid()

        nnodes = len(adj_table)
        graph = [set() for _ in range(nnodes)]

        for i in range(nnodes):
            for j in range(len(adj_table[i])):
                graph[i].add(adj_table[i][j])

        metric_betweennness = [0] * nnodes

        for i in range(nnodes):
            for j in range(nnodes):
                if i != j:
                    paths = bfs_paths(graph, i, j)

                    counter = [0] * nnodes
                    for row in paths:
                        for k in range(nnodes):
                            if k != i and k != j and k in row:
                                counter[k] += 1

                    for node in range(nnodes):
                        # Prevent division by zero
                        if len(paths) > 0:
                            metric_betweennness[node] += counter[node] / len(paths)

        for node in range(len(metric_betweennness)):
            label = employee_data[node][1] + ' ' + employee_data[node][2]
            metric_betweennness[node] = (label, metric_betweennness[node] / ((count_nodes(adj_table)-1) * (count_nodes(adj_table)-2)), node)

        metric_betweennness.sort(key=lambda x: x[1], reverse=True)

        save("betweenness", metric_betweennness)

        return metric_betweennness

def dfs(pred, node, paths, curr_path):
    curr_path.append(node)

    # if path ends
    if len(pred[node]) == 0:
        paths.append(list(reversed(curr_path)))

    for parent in pred[node]:
        dfs(pred, parent, paths, curr_path)

    # Backtrack
    curr_path.pop()

def bfs_paths(graph, start, end):
    if len(graph) == 0:
        return []

    queue = deque()
    dist = [float('inf')] * len(graph)
    pred = [set() for _ in range(len(graph))]
    dist[start] = 0
    queue.append(start)

    ans = False
    while len(queue) != 0:
        current = queue.popleft()

        for child in graph[current]:
            if dist[child] == float('inf'):
                queue.append(child)
                dist[child] = dist[current] + 1
                pred[child].add(current)
            elif dist[child] == dist[current] + 1:
                pred[child].add(current)

            if child == end:
                ans = True

    if ans:
        all_paths = []
        curr_path = []
        dfs(pred, end, all_paths, curr_path)
        return all_paths

    return []


def count_nodes(adj_table):
    node_count = 0

    for node in adj_table:
        if len(node) > 0:
            node_count += 1

    return node_count