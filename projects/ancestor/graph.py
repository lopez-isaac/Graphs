"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)

        #keep track of the visted nodes
        visited = set()

        #repeat till queue is empty
        while queue.size() > 0:
            #deque the first vertex
            v = queue.dequeue()

            #if the node has not been visited
            if v not in visited:
                #setting the vertex as being visted and printing the visit
                print(v)
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    queue.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        stack.push(starting_vertex)

        #keep track of visted
        visited = set()


        while stack.size() > 0:
            #pop the last vertex
            v = stack.pop()

            # if its not visited:
            if v not in visited:
                # mark as visited
                print(v)
                visited.add(v)
                for next_vert in self.get_neighbors(v):
                    stack.push(next_vert)





    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)

        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        queue = Queue()
        # enqueue the first PATH
        queue.enqueue([starting_vertex])

        # keep track of the visted nodes
        visited = set()

        # While the queue is not empty...
        while queue.size() > 0:

            # Dequeue the first PATH
            path = queue.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            # Mark it as visited
            if last_vertex not in visited:
                visited.add(last_vertex)
            # CHECK IF IT'S THE TARGET
            # IF SO, RETURN PATH
                if last_vertex == destination_vertex:
                    return path
            # Then add A PATH TO its neighbors to the back of the queue
            for next_vertex in self.get_neighbors(last_vertex):
            # _COPY_ THE PATH
                path_copy = path.copy()
            # APPEND THE NEIGHOR TO THE BACK
                path_copy.append(next_vertex)
                queue.enqueue(path_copy)




    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #path = []
        stack = Stack()
        # enqueue the first PATH
        stack.push([starting_vertex])

        # keep track of the visted nodes
        visited = set()

        # While the queue is not empty...
        while stack.size() > 0:

            # Dequeue the first PATH
            path = stack.pop()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            # Mark it as visited
            if last_vertex not in visited:
                visited.add(last_vertex)
                # CHECK IF IT'S THE TARGET
                # IF SO, RETURN PATH
                if last_vertex == destination_vertex:
                    return path
            # Then add A PATH TO its neighbors to the back of the queue
            for next_vertex in self.get_neighbors(last_vertex):
                # _COPY_ THE PATH
                path_copy = path.copy()
                # APPEND THE NEIGHOR TO THE BACK
                path_copy.append(next_vertex)
                stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        print(starting_vertex)

        if visited is None:
            visited = set()
        if path is None:
            path =[]

        visited.add(starting_vertex)

        #make a copy of the lists, adding the new vert on
        path = path + [starting_vertex]

        #base case
        if starting_vertex == destination_vertex:
            return path

        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, destination_vertex, visited, path)

                if new_path:
                    return new_path

        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    print("----------")

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print("recursion")
    graph.dft_recursive(1)

    print("--------")
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    print("depth first search")

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print("recursion search")
    print(graph.dfs_recursive(1, 6))
