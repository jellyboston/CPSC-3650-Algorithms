from pq_heap import PQHeap

class SSSPResult:
    def __init__(self, p, d):
        self.parent = p
        self.d = d


    def __repr__(self):
        return str({"parent": self.parent, "d": self.d})


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


    def weight(self, u, v):
        """ Returns the weight of the given edge in this graph.
            Returns None if the edge does not exist
        
            u -- a valid vertex index for this graph
            v -- a valid vertex index for this graph
        """
        if u < 0 or u >= self.size() or v < 0 or v >= self.size():
            return None

        # sequential search (w.c. Theta(V)) for edge on u's adj list
        i = 0
        while i < len(self._adj[u]) and self._adj[u][i][0] != v:
            i += 1
        if i < len(self._adj[u]):
            # found edge; get weight
            return self._adj[u][i][1]
        else:
            # edge not found
            return None
    

    def outdegree(self, v):
        """ Returns the degree of the given vertex in this graph.
            v -- a valid vertex index for this graph
        """
        return len(self._adj[v])


    def edges(self, v):
        """ Returns a list of the vertices adjacent to the given vertex
            in this graph and the weights of the corresponding edges.  Each
            element in the returned list is a (destination, weight) pair.
            v -- a valid vertex index for this graph
        """
        return self._adj[v][:]


    def dijkstra(self, s):
        """ Returns the shortest paths tree for this graph starting with the
            given vertex.  The tree is returned as an array of SSSPResult
            objects, where entry i gives the next-to-last vertex in the
            shortest path to vertex i and the total wright of the shortest
            (least total weight) path from s to i.

            self -- a weighted graph with no negative-weight edges
            s -- a valid vertex index for this graph
        """
        # initialize vertices to unseen
        parent = [None] * self._size
        d = [float('inf')] * self._size

        # distance from source to itself is 0
        d[s] = 0

        q = PQHeap(d)

        while not q.is_empty():
            # get next-closest vertes
            u = q.extract_min()

            # go over edges from u
            for v, w in self._adj[u]:
                if q.contains(v) and d[u] + w < d[v]:
                    # path through u is new best path to v
                    d[v] = d[u] + w
                    parent[v] = u
                    q.decrease_key(v, d[v])

        return [SSSPResult(p, d) for p, d in zip(parent, d)]
