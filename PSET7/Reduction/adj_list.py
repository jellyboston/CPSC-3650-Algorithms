class DFSResult:
    def __init__(self):
        self.parent = None
        self.d = None
        self.f = None
        self.color = 0 # 0 = WHITE/unvisited


    def __repr__(self):
        return str({"parent": self.parent, "d": self.d, "f": self.f, "color": self.color})


class AdjListGraph:
    """ An graph with vertices labelled by consecutive integer indices starting from 0. """
    # TODO: make this abstract
    def __init__(self, n):
        self._size = n

        # make empty adjacency lists
        self._adj = [[] for i in range(n)]


    def size(self):
        return self._size


    def has_edge(self, u, v):
        """ Determines if this graph contains the given edge.
            u -- a valid vertex index for this graph
            v -- a valid vertex index for this graph
        """
        return v in self._adj[u]


    def outdegree(self, v):
        """ Returns the degree of the given vertex in this graph.
            v -- a valid vertex index for this graph
        """
        return len(self._adj[v])


    def edges(self, v):
        """ Returns a copy of the list of vertices adjacent to the given vertex
            in this graph.
            v -- a valid vertex index for this graph
        """
        return self._adj[v][:]


    def __repr__(self):
        return "\n".join(str(adj) for adj in self._adj)
