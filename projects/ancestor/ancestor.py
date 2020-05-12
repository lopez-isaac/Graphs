from util import Stack, Queue


#ancestor = detination_node
def earliest_ancestor(ancestor, starting_node):

    parents = {}

    for a in ancestor:
        key = a[1]
        value = a[0]
        if key not in parents:
            parents[key] = []
        parents[key].append(value)

    #Depth first search

    visited = set()

    stack = Stack()
    stack.push([starting_node])

    while stack.size() > 0:
        path = stack.pop()
        current_vert = path[-1]

        if current_vert not in visited:
            visited.add(current_vert)

            for parent in parents[current_vert]:
                path_copy = path.copy()
                path_copy.append(parent)
                stack.push(path_copy)









