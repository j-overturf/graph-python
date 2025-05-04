class Edge:
    """
    Edge object for a Graph.
    """

    def __init__(self, source, dest, weight=None):
        """
        Initializes the edge internal state.
        :param source: The source of the edge.
        :param dest: The destination of the edge.
        :param weight: The weight of the edge.
        """
        self.source = source
        self.destination = dest
        self.weight = weight

    def get_source(self):
        """
        Returns the source of the edge.
        :return: Source of the edge.
        """
        return self.source

    def get_destination(self):
        """
        Returns the destination of the edge.
        :return: Destination of the edge.
        """
        return self.destination

    def get_weight(self):
        """
        Returns the weight of the edge.
        :return: Weight of the edge.
        """
        return self.weight
