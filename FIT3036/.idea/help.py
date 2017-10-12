from queue import deque

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

if __name__ == '__main__':
    graph = [set() for _ in range(6)]
    # edges = [[0, 1],
    # [0, 2],
    # [1, 2],
    # [1, 3],
    # [1, 4],
    # [2, 4],
    # [3, 4],
    # [3, 5],
    # [3, 6],
    # [4, 6],
    # [4, 7],
    # [5, 8],
    # [5, 9],
    # [6, 9],
    # [7, 9],
    # [8, 9]]
    edges = [[0,1],[0,2],[0,5],[1,2],[1,4],[2,3],[2,5],[3,4],[4,1],[4,2],[5,3]]

    for i in edges:
        graph[i[0]].add(i[1])
        graph[i[1]].add(i[0])

    total = [0] * 6

    for i in range(6):
        for j in range(6):
            if i != j:
                paths = bfs_paths(graph, i, j)

                counter = [0] * 6
                for row in paths:
                    for k in range(6):
                        if k != i and k != j and k in row:
                            counter[k] += 1

                for node in range(6):
                    total[node] += counter[node] / len(paths)

    for i in total:
        print(i/2)
                # print("New bfs")
                # for row in paths:
                #     print(str(row))