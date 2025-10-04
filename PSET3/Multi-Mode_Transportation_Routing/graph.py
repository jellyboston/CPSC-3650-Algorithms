from adj_list import AdjListGraph

class Graph(AdjListGraph):
    """ An undirected weighted graph with vertices labelled by consecutive integer indices starting from 0. """
    def __init__(self, n):
        super().__init__(n)


    def degree(self, v):
        """ Returns the degree of the given vertex in this graph.
            v -- a valid vertex index for this graph
        """
        return self.outdegree(v)


    def add_edge(self, u, v, w):
        """ Adds the given edge to this graph.
            u -- a valid vertex index for this graph with no edge to v
            v -- a valid vertex index for this graph not u and with no edge to u
            w -- a number for the weight of the edge
        """
        self._adj[u].append((v, w))
        self._adj[v].append((u, w))

