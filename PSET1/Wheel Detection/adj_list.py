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

    
    def dfs(self, order=None):
        """ Performs DFS on this graph with roots of the DFS-tree chosen in
            the given order.  If the order is None, then vertices are considered
            in order of increasing index.
            order -- a non-repeating list of vertex indices in this graph, or None
        """
        # initialize empty info for each vertex
        results = [DFSResult() for i in range(self._size)]

        # no order specified -> go in order of increasing index
        if order is None:
            order = range(self._size) # don't need to listify!


        # select roots of DFS trees in order given
        time = 0
        for v in order:
            if results[v].color == 0:
                time = self.dfs_visit(v, time, results)

        return results


    def dfs_visit(self, u, time, results):
        results[u].d = time
        time = time + 1
        results[u].color = 1 # 1 = GREY/processing
        
        for v in self._adj[u]:
            if results[v].color == 0:
                results[v].parent = u
                time = self.dfs_visit(v, time, results)

        results[u].f = time
        results[u].color = 2 # 2 = BLACK/finished
        return time + 1

