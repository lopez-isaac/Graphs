from graph import Graph
from util import Stack, Queue


# #ancestor = detination_node
def earliest_ancestor(ancestor, starting_node):
    # Create an empty queue and enqueue A PATH TO the starting node
    q = Queue()
    q.enqueue([starting_node])
    # Create a dictionary to store parents
    parents = {}
    for a in ancestor:
        key = a[1]
        value = a[0]
        if key not in parents:
            parents[key] = []
        parents[key].append(value)

    # list to keep track of len(longest path) and node at that length
    current_longest = [0, 0]
    # While the queue is not empty...
    while q.size() > 0:
        # Dequeue the first PATH
        current_path = q.dequeue()
        # Grab the last node from the PATH
        last_node = current_path[-1]
        # CHECK IF node has parents in the dictionary:
        if last_node not in parents:
      # IF NO, compare length of current path to store current_longest.
            # if current_path is longest, that becomes the current_longest
            # along with node at that distrance (last vertex)
            if len(current_path) > current_longest[0] and last_node > current_longest[1]:
                current_longest = (len(current_path), last_node)
        else:
            # if there are parents in the dictionary, add new paths for each
            # parent of the last_vertex:
            for parent in parents[last_node]:
                q.enqueue(current_path + [parent])
    # if starting node doesn't have any parents, return -1:
    if current_longest[1] == starting_node:
        return -1
    else:
        # otherwise, earliest ancestor should be stored in current_longest
        return current_longest[1]










