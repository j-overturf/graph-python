class Vertex:
    """
    Vertex object for a Graph.
    """

    def __init__(self, label):
        """
        Initializes the vertex internal state.
        :param label: The label for the vertex.
        """
        self.label = label

    def get_label(self):
        """
        Returns the label for the vertex.
        :return: Label for the vertex.
        """
        return self.label
