#  File: Graph.py

#  Description: Performs various functions on a graph of cities.

#  Student Name: Srijeeta Biswas

#  Student UT EID: sb48779

#  Partner Name: Kenneth Pham

#  Partner UT EID: khp455

#  Course Name: CS 313E

#  Unique Number: 50725

#  Date Created: 4/29/2019

#  Date Last Modified: 4/29/2019

# Stack class
class Stack(object):
    # initializer
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))


# queue class
class Queue(object):
    # initializer
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


# vertex class
class Vertex(object):
    # initializer
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)

# edge class
class Edge(object):
    # initializer
    def __init__(self, fromVertex, toVertex, weight):
        self.u = fromVertex
        self.v = toVertex
        self.weight = weight

    # equality methods

    def __lt__(self, other):
        return (self.weight < other.weight)

    def __gt__(self, other):
        return (self.weight > other.weight)

    def __le__(self, other):
        return (self.weight <= other.weight)

    def __ge__(self,other):
        return (self.weight >= other.weight)

    def __eq__(self, other):
        return (self.weight == other.weight)

    def __ne__(self, other):
        return (self.weight != other.weight)


# graph class
class Graph(object):
    # initializer
    def __init__(self):
        self.Vertices = []  # list of Vertex objects
        self.adjMat = []  # adjacency matrix

    # returns a list of the vertices
    def get_vertices(self):
        return self.Vertices


    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given a label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        # if vertex is not in the graph
        if (not self.has_vertex(label)):
            self.Vertices.append(Vertex(label))

            # add a new column in the adjacency matrix
            nVert = len(self.Vertices)
            for i in range(nVert - 1):
                (self.adjMat[i]).append(0)

            # add a new row for the new Vertex
            new_row = []
            for i in range(nVert):
                new_row.append(0)
            self.adjMat.append(new_row)


    # returns edge weight between two vertices
    def get_edge_weight(self, fromVertexLabel, toVertexLabel):
        fromVertex = self.get_index(fromVertexLabel)
        toVertex = self.get_index(toVertexLabel)
        # if edge exists
        if self.adjMat[fromVertex][toVertex] != 0:
            return (self.adjMat[fromVertex][toVertex])
        return -1

    # deletes an edge
    def delete_edge(self, fromVertexLabel, toVertexLabel):
        fromVertex = self.get_index(fromVertexLabel)
        toVertex = self.get_index(toVertexLabel)
        # since undirected, both pathways are set to 0
        self.adjMat[fromVertex][toVertex] = 0
        self.adjMat[toVertex][fromVertex] = 0

    # deletes a vertex
    def delete_vertex(self, vertexLabel):
        vertex = self.get_index(vertexLabel)
        nVert = len(self.Vertices)
        # if vertex exists
        if vertex >= 0:
            for entry in self.Vertices:
                # looks for vertex in vertex list
                if vertexLabel == entry.label:
                    # removes entry in vertices
                    self.Vertices.remove(entry)
            # removes vertex from adj matrix
            for i in range(len(self.adjMat)):
                del self.adjMat[i][vertex]
            del self.adjMat[vertex]

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # do the depth first search in a graph
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # mark the vertex v as visited and push it on the stack
        (self.Vertices[v]).visited = True
        print(self.Vertices[v])
        theStack.push(v)

        # visit the other vertices according to depth
        while (not theStack.is_empty()):
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print(self.Vertices[u])
                theStack.push(u)

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs(self, v):
        # create the Queue
        theQueue = Queue()
        # mark the starting vertex as visited
        (self.Vertices[v]).visited = True
        # print starting vertex
        print((self.Vertices[v]))
        # add the starting vertex to the queue
        theQueue.enqueue(v)
        while (not theQueue.is_empty()):
            # the first vertex in the queue
            u = theQueue.dequeue()
            # finds an adjacent vertex next to the dequeued element
            u2 = self.get_adj_unvisited_vertex(u)
            # marks the unvisited vertex as visited
            (self.Vertices[u2]).visited = True
            # while there are available adjacent and unvisited vertices
            while u2 != -1:
                # mark adjacent vertex as visited
                (self.Vertices[u2]).visited = True
                # print adjacent vertex
                print((self.Vertices)[u2])
                # enqueue the adjacent vertex
                theQueue.enqueue(u2)
                u2 = self.get_adj_unvisited_vertex(u)

        # resetting all the vertices to unvisited since queue is empty
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

    # returns a list of neighbors
    def get_neighbors(self, vertexLabel):
        neighbors = []
        idx = self.get_index(vertexLabel)
        # if vertex exits
        if idx >= 0:
            for i in range(len(self.adjMat[idx])):
                # if an edge exists between the given vertex and another
                if self.adjMat[idx][i] != 0:
                    neighbor = self.Vertices[i].label
                    # append to the list
                    neighbors.append(neighbor)
            # return list
            return neighbors
        else:
            return None


# main function
def main():
    # create the Graph object
    cities = Graph()

    # open the file for reading
    in_file = open("./graph.txt", "r")

    # read the number of Vertices
    num_vertices = int((in_file.readline()).strip())

    # add the vertices to the list
    for i in range(num_vertices):
        city = (in_file.readline()).strip()
        cities.add_vertex(city)

    # read the edges and add them to the adjacency matrix
    num_edges = int((in_file.readline()).strip())

    for i in range(num_edges):
        edge = (in_file.readline()).strip()
        edge = edge.split()
        start = int(edge[0])
        finish = int(edge[1])
        weight = int(edge[2])

        cities.add_directed_edge(start, finish, weight)


    # read the starting vertex for dfs and bfs
    start_vertex = (in_file.readline()).strip()

    # get the index of the starting vertex
    start_index = cities.get_index(start_vertex)

    # test depth first search
    print("\nDepth First Search")
    cities.dfs(start_index)
    print()

    # test breadth first search
    print("\nBreadth First Search")
    cities.bfs(start_index)
    print()

    # test deletion of an edge
    print('Deletion of an edge')
    print()
    edge_deletion = in_file.readline().strip()
    edge_deletion = edge_deletion.split()
    f_city = edge_deletion[0]
    s_city = edge_deletion[1]
    cities.delete_edge(f_city,s_city)
    print('Adjacency Matrix')
    adj_mat_1 = (cities.adjMat)
    blank1 = ''
    for l in range(len(adj_mat_1)):
        for m in range(len(adj_mat_1[0])):
            blank1 += str(adj_mat_1[l][m]) + ' '
        print(blank1)
        blank1 = ''
    print()

    # test deletion of a vertex
    print('Deletion of a vertex')
    print()
    print('List of Vertices')
    vertex_deletion = in_file.readline().strip()
    cities.delete_vertex(vertex_deletion)
    list_vertex = (cities.get_vertices())
    for k in range(len(list_vertex)):
        print(list_vertex[k])
    print()
    print('Adjacency Matrix')
    adj_mat_2 = (cities.adjMat)
    blank2 = ''
    for element in range(len(adj_mat_2)):
        for item in range(len(adj_mat_2[0])):
            blank2 += str(adj_mat_2[element][item]) + ' '
        print(blank2)
        blank2 = ''


    # close the file
    in_file.close()


if __name__ == "__main__":
  main()

