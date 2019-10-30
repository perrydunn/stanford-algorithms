def first_pass(graph_rev, n):
    t = 0
    # Ignore explored[0] existence
    explored = [False for _ in range(n+1)]
    finishing_times = {t: None for t in range(1, n+1)}
    stack = []

    for i in range(1, n+1):
        if not explored[i]:
            explored[i] = True
            stack.append(i)

            while stack:
                s = stack[-1]

                heads = graph_rev.get(s, [])
                dead_end = True

                for j in heads:
                    if not explored[j]:
                        if dead_end:
                            dead_end = False
                        explored[j] = True
                        stack.append(j)

                if dead_end:
                    stack.pop()
                    t += 1
                    finishing_times[t] = s

    return finishing_times


def second_pass(graph, n, finishing_times):
    s = None
    # Ignore explored[0] existence
    explored = [False for _ in range(n+1)]
    sccs = {}
    stack = []

    for i in range(n, 0, -1):
        if not explored[finishing_times[i]]:
            s = finishing_times[i]
            sccs[s] = []
            explored[s] = True
            stack.append(s)

            while stack:
                t = stack[-1]

                heads = graph.get(t, [])
                dead_end = True

                for j in heads:
                    if not explored[j]:
                        if dead_end:
                            dead_end = False
                        explored[j] = True
                        stack.append(j)

                if dead_end:
                    stack.pop()
                    sccs[s].append(t)

    return sccs


if __name__ == "__main__":
    graph = {}
    graph_rev = {}
    n = 0

    with open("SCC.txt", "r") as f:
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

    top_five = [1, 1, 1, 1, 1]

    for _, members in sccs.items():
        size = len(members)
        if size > min(top_five):
            top_five.remove(min(top_five))
            top_five.append(size)

    top_five.sort(reverse=True)
    print(",".join([str(n) for n in top_five]))
