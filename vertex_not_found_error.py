class VertexNotFoundError(Exception):
    """
    Vertex not found error for the graph object.

    Message: Explanation of the Error.
    """
    def __init__(self, message):
        """
        Initializes the exception.
        """
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """
        Returns a string of the exception message.
        :return: String of the exception message.
        """
        return f"{self.message}"
