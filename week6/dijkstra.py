def dijkstra(graph, s):
    V = set(graph.keys())
    V.remove(s)
    X = set([s])
    # In A, ignore first entry (indexes from 0 vs 1 for graph)
    A = [1000000 for i in range(len(V) + 2)]
    A[s] = 0

    while V:
        winner_len = 1000000
        winner = [0, 0]
        for tail in X:
            for head in V:
                if graph[tail].get(head) is not None:
                    greedy_score = A[tail] + graph[tail][head]
                    if greedy_score < winner_len:
                        winner_len = greedy_score
                        winner[0], winner[1] = tail, head
        X.add(winner[1])
        V.remove(winner[1])
        A[winner[1]] = winner_len

    return A


if __name__ == "__main__":
    graph = {}
    with open("dijkstraData.txt", "r") as f:
        line = f.readline()
        while line:
            node_details = line.split()
            tail_node = int(node_details[0])
            graph[tail_node] = {}
            for edge in node_details[1:]:
                head_node, edge_length = [int(num) for num in edge.split(",")]
                graph[tail_node][head_node] = edge_length
            line = f.readline()
    result = dijkstra(graph, 1)
    nodes_to_report = [7,37,59,82,99,115,133,165,188,197]
    string_result = ""
    for node in nodes_to_report:
        string_result += str(result[node]) + ","
    print(string_result[:-1])
