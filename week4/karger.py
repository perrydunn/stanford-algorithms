from copy import deepcopy
from math import log
from random import choice, choices


def karger_min_cut(graph):
    n = len(graph)
    N = int(n**2)  # int(n**2 * log(n)) for <= 1 / n
    min_cut = None
    for _ in range(N):
        res = karger(deepcopy(graph))
        cut_num = len(res[list(res.keys())[0]])
        if min_cut is None or cut_num < min_cut:
            min_cut = cut_num
    return min_cut


def karger(graph):
    if len(graph) == 2:
        return graph
    u = choices(list(graph.keys()), weights=map(len, graph.values()))[0]
    v = choice(graph[u])
    for vertex in graph[v]:
        graph[vertex].remove(v)
        if vertex != u:
            graph[u].append(vertex)
            graph[vertex].append(u)
    del graph[v]
    return karger(graph)


if __name__ == "__main__":
    graph = {}
    with open("kargerMinCut.txt", "r") as f:
        line = f.readline()
        while line:
            arr = [int(v) for v in line.split()]
            graph[arr[0]] = arr[1:]
            line = f.readline()
    res = karger_min_cut(graph)
    print(res)
