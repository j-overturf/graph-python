from vertex import Vertex
from edge import Edge
from duplicate_vertex_error import DuplicateVertexError
from vertex_not_found_error import VertexNotFoundError
from edge_not_found_error import EdgeNotFoundError


class Graph:
    """
    Implementation of a graph in Python.
    """

    def __init__(self, directed=False, weighted=True):
        """
        Initializes the graph internal state.
        :param directed: If the graph is directed or not.
        """
        self.vertices = []
        self.edges = {}
        self.directed = directed
        self.weighted = weighted

    def contains_vertex(self, label):
        """
        Iterate through graph vertices and check if the vertex exists.
        :param label: Label of the vertex to check for.
        :return: True if the vertex exists.
        """
        exists = False

        # Get the vertex if it exists
        if self.get_vertex(label) is not None:
            exists = True

        return exists

    def contains_edge(self, source, dest, weight):
        """
        Checks if an edge exists in the graph given the source, dest, and weight
        :param source: Source of the edge.
        :param dest: Destination of the edge.
        :param weight: Weight of the edge.
        :return: True if the edge exists.
        """
        exists = False

        # Find the source vertex
        vertex = self.get_vertex(source)

        # Find the edge from the map
        if vertex is not None:
            edges = self.edges[vertex]
            # Iterate through edges that exist for that vertex
            for edge in edges:
                # Check if the graph is weighted
                if self.weighted:
                    # If the edges match
                    if edge.source == source and edge.destination == dest and edge.weight == weight:
                        exists = True
                else:
                    # If the edges match
                    if edge.source == source and edge.destination == dest:
                        exists = True

        else:
            raise VertexNotFoundError("Vertex not found in graph")

        return exists

    def add_vertex(self, label):
        """
        Adds a new vertex to the graph.
        :param label: Label for the new vertex.
        """
        # Check if a vertex with that label exists in the graph
        if self.contains_vertex(label):
            raise DuplicateVertexError("Vertex already exists")

        # Add new vertex to graph
        new_vertex = Vertex(label)
        self.vertices.append(new_vertex)

    def add_edge(self, source, dest, weight=None):
        """
        Adds a new edge to the graph.
        :param source: Source of the edge.
        :param dest: Destination of the edge.
        :param weight: Weight of the edge.
        """
        # Create new edge
        new_edge = Edge(source, dest, weight)

        # Add to graph
        edge_list = self.edges[source]
        edge_list.append(new_edge)

        # If the graph is not directed, add to dest as well
        if not self.directed:
            edge_list = self.edges[dest]
            edge_list.append(new_edge)

    def degree(self, label):
        """
        Returns the degree of a vertex.
        :param label: Label of vertex to find.
        :return: Degree of the vertex if it exists.
        """
        degree = 0

        # Get vertex if it exists
        vertex = self.get_vertex(label)
        if vertex is not None:
            # Calculate the degree
            degree = len(self.edges[vertex])
        else:
            # Raise exception if it does not
            raise VertexNotFoundError("Vertex not found in graph")

        return degree

    def get_vertex(self, label):
        """
        Gets a vertex from the graph with the specified label.
        :param label: Label of vertex to find.
        :return: Vertex of label.
        """
        found = None

        # Iterate through vertices
        for vertex in self.vertices:
            # If labels match
            if vertex.label == label:
                # Calculate the degree
                found = vertex

        return found

    def get_edge(self, source, dest, weight=None):
        """
        Gets an edge from the graph given the source, destination, and weight.
        :param source: Source of the edge.
        :param dest: Destination of the edge.
        :param weight: Weight of the edge.
        :return: The edge if it exists
        """
        found = None

        # Find the source vertex
        vertex = self.get_vertex(source)

        # Find the edge from the map
        if vertex is not None:
            edges = self.edges[vertex]
            # Iterate through edges that exist for that vertex
            for edge in edges:
                # If the graph is weighted
                if self.weighted:
                    # If the edges match
                    if edge.source == source and edge.destination == dest and edge.weight == weight:
                        found = edge
                else:
                    # If the edges match
                    if edge.source == source and edge.destination == dest:
                        found = edge
        else:
            raise VertexNotFoundError("Vertex not found in graph")

        return found

    def adjacent(self, label):
        """
        Gets the adjacent vertices of the specified vertex label.
        :param label: Label of the vertex.
        :return: Array of adjacent vertices.
        """
        adjacent_vertices = []

        # Find vertex
        vertex = self.get_vertex(label)

        # If it exists
        if vertex is not None:
            # Get adjacent vertices
            edge_list = self.edges[vertex]
            # Append each vertex from edges
            for edge in edge_list:
                adjacent_vertices.append(edge.destination)
        else:
            # Raise exception if it does not
            raise VertexNotFoundError("Vertex not found in graph")

        return adjacent_vertices

    def total_degree(self):
        """
        Gets the total degree of the graph.
        :return: The total degree of the graph.
        """
        degree = 0
        # Iterate through the vertices of the graph
        for vertex in self.vertices:
            degree += len(self.edges[vertex.label])

        return degree

    def is_connected(self):
        """
        Checks if the entire graph is connected.
        :return: True if the entire graph is connected.
        """
        is_connected = True

        # Iterate through vertices
        for vertex in self.vertices:
            # If the length is zero, that means the vertex has no edges and cannot be connected
            if len(self.edges[vertex.label]) == 0:
                is_connected = False

        return is_connected

    def is_simple(self):
        """
        Checks if the graph is a simple graph.
        :return: True if the graph is a simple graph.
        """
        simple = True

        # Iterate through the vertices
        for vertex in self.vertices:
            # Check the edge list for parallel edges or loops
            destinations = []
            for edge in self.edges[vertex.label]:
                # Check for loop
                if edge.source == edge.destination:
                    simple = False

                # Check if the destination has already been spotted, if it has then it is a parallel edge
                if destinations.__contains__(edge.destination):
                    simple = False

                # Append destination
                destinations.append(edge.destination)

        return simple

    def is_complete(self):
        """
        Checks if the graph is complete. Each vertex connects to every other vertex.
        :return: True if the graph is complete.
        """
        complete = True

        # Check if the graph is simple, if it is not then it cannot be complete at all
        if self.is_simple():
            # Iterate through vertices
            for vertex in self.vertices:
                # If the vertex edge amount does not equal to the total number of vertices, it cannot be complete
                if len(self.edges[vertex.label]) != len(self.vertices) - 1:
                    complete = False
        else:
            complete = False

        return complete
