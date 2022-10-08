import heapq
def network(times: list[list[int]], n: int, x: int) -> int:
    edg = dict()
    for [start, end, time] in times:
        edg[start] = edg.get(start, []) + [[time, end]]
    heap = [[0, x]]
    node = set()
    cnt = 0
    while heap:
        edge = heapq.heappop(heap)
        if edge[1] in node:
            continue
        node.add(edge[1])
        cnt = edge[0]
        for [time, end_node] in edg.get(edge[1], []):
            if end_node not in node:
                heapq.heappush(heap, [edge[0] + time, end_node])

    return cnt if len(node) == n else -1
if __name__ == "__main__":
    times = eval(input())
    n = int(input())
    x = int(input())
    print(network(times, n, x))
