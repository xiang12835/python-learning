#coding=utf-8

def bfs(graph, start, end):

    queue = []
    queue.append([start])

    visited = set()  # 树可省，图不可
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    # other processing work
