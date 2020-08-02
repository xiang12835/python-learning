# coding=utf-8


def dfs(node):
    # 递归写法
    visited = set()
    visited.add(node)

    # process current node here

    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node)


def dfs_stack(self, tree):
    if tree.root is None:
        return []

    visited = set()
    stack = [tree.node]

    while stack:
        node = stack.pop()
        visited.add(node)

        process(node)

        nodes = generate_related_nodes(node)
        stack.push(nodes)

    # other processing work
