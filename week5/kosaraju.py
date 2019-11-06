def first_pass(graph_rev, n):

    def dfs(graph_rev, i):
        explored[i] = True
        if graph_rev.get(i):
            for j in graph_rev[i]:
                if not explored[j]:
                    dfs(graph_rev, j)
            nonlocal t
            t += 1
            finishing_times[t] = i

    t = 0
    explored = [False for _ in range(n+1)]  # Ignore explored[0] existence
    finishing_times = {t: None for t in range(1, n+1)}

    for i in range(1, n+1):
        if not explored[i]:
            dfs(graph_rev, i)

    return finishing_times


def second_pass(graph, n, finishing_times):

    def dfs(graph, i):
        explored[i] = True
        nonlocal s
        sccs[s].append(i)
        if graph.get(i):
            for j in graph[i]:
                if not explored[j]:
                    dfs(graph, j)

    s = None
    explored = [False for _ in range(n+1)]  # Ignore explored[0] existence
    sccs = {}

    for i in range(n, 0, -1):
        if not explored[finishing_times[i]]:
            s = finishing_times[i]
            sccs[s] = []
            dfs(graph, s)

    return sccs


if __name__ == "__main__":
    graph = {}
    graph_rev = {}
    n = 0
    with open("test.txt", "r") as f:
        line = f.readline()
        while line:
            edge = [int(v) for v in line.split()]
            if edge[0] > n: n = edge[0]
            if edge[1] > n: n = edge[1]
            if graph.get(edge[0]) is None:
                graph[edge[0]] = []
            graph[edge[0]].append(edge[1])
            if graph_rev.get(edge[1]) is None:
                graph_rev[edge[1]] = []
            graph_rev[edge[1]].append(edge[0])
            line = f.readline()
    f = first_pass(graph_rev, n)
    sccs = second_pass(graph, n, f)
    print(sccs)
    for leader, members in sccs.items():
        sccs[leader] = len(members)
    print(sccs)
