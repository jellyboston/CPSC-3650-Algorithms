from adj_list import AdjListGraph

class Graph(AdjListGraph):
    """ An undirected graph with vertices labelled by consecutive integer indices starting from 0
        and each with an associate value. """
    def __init__(self, n, v):
        """ Creates an undirected graph with the given number of vertices.

            n -- a nonnegative integer
            v -- a list of numbers of length n for the values assocuated with each vertex
        """
        super().__init__(n, v)


    def degree(self, v):
        """ Returns the degree of the given vertex in this graph.
            v -- a valid vertex index for this graph
        """
        return self.outdegree(v)


    def add_edge(self, u, v):
        """ Adds the given edge to this graph.
            u -- a valid vertex index for this graph with no edge to v
            v -- a valid vertex index for this graph not u and with no edge to u
        """
        self._adj[u].append(v)
        self._adj[v].append(u)

