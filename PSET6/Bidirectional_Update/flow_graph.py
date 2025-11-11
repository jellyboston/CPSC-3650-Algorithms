from adj_list import AdjListGraph

class FlowGraph(AdjListGraph):
    """ An flow graph with vertices labelled by consecutive integer indices starting from 0.
        Flows and residual capacities on flow graphs can be modified after the graph has
        created to facilitate flow algorithms.
    """
    class HalfEdge:
        """ A forward or backward edge in a flow graph.  The two directions are packaged
            together ina HalfEdge to facilitate finding one from the other.
        """
        def __init__(self, u, v, c, p):
            """ Creates the given half edge.
                u -- an integer for the index of the from vertex for the half edge
                v -- an integer the index of the to vertex
                c -- a positive integer for the capacity of the edge
                p -- the parent FlowEdge
            """
            self._source = u
            self._dest = v
            self._flow = 0
            self._capacity = c
            self._residual = c
            self._parent = p


        def source(self):
            return self._source


        def destination(self):
            return self._dest

            
        def flow(self):
            return self._flow


        def capacity(self):
            return self._capacity

        
        def residual(self):
            return self._residual


        def opposite(self):
            if self._parent._forward is self:
                return self._parent._backward
            else:
                return self._parent._forward

            
        def add_flow(self, b):
            """ Adds the given amount of flow to this edge.
                b -- a number so that 0 <= flow()+b <= capacity
            """
            self._flow += b

            
        def add_residual(self, b):
            """ Adds the given amount of residual capacity to this edge.
                b -- a number so that 0 <= residual() + b <= opposite().capacity()
            """
            self._residual += b

            
        def __repr__(self):
            return f"({self._source},{self._dest}):{self._flow}/{self._capacity}"
        
    
    class FlowEdge:
        """ An edge in a flow graph.  The edge represents both the forward edge and the
            backward edge.  Updates to the flow in one direction will update the flow
            and/or capacity in the opposite direction.
        """
        def __init__(self, u, v, c_f, c_b):
            """ Creates an edge from the first vertex to the second with the given capacity.
                u -- an integer for the from vertex
                v -- an integer for the to vertex, not equal to u
                c -- a positive number for the capacity
            """
            self._forward = FlowGraph.HalfEdge(u, v, c_f, self)
            self._backward = FlowGraph.HalfEdge(v, u, c_b, self)
        
    
    def __init__(self, n):
        super().__init__(n)


    def add_edge(self, u, v, c_f, c_b=0):
        """ Adds the given edge to this graph.
            u -- a valid vertex index for this graph with no edge to v
            v -- a valid vertex index for this graph with no edge to u
            c_f -- a nonnegative number for the capacity of the egde in one direction
            c_b -- a nonnegative number for the capacity of the egde in the other direction
        """
        e = self.FlowEdge(u, v, c_f, c_b)
        self._adj[u].append(e._forward)
        self._adj[v].append(e._backward)


    def find_edge(self, source, dest):
        """ Returns the edge from the given vertex to the given vertex. Returns
            None if there is no such edge.

            source -- a valid index of a vertex in this graph
            dest -- a valid index of a vertex in this graph
        """
        return next((e for e in self._adj[source] if e._dest == dest), None)

    
    def value(self, s):
        """ Returns the value of the flow in this graph.

            s -- the index of the source vertex in this graph
        """
        return sum(e._flow for e in self._adj[s])

    
    def validate(self, source, sink):
        """ Checks the invariants for this flow graph and throws an exception if one
            is violated.

            source -- the index of the source vertex in this graph
            sink -- the index of the sink vertex in this graph
        """
        n = len(self._adj)
        flow_in = [0] * n
        flow_out = [0] * n

        # check the capacity constraint and no bi-directional flow constraint for all edges
        for adj_list in self._adj:
            for e in adj_list:
                if e._flow > e._capacity:
                    raise RuntimeError(f"capacity constraint violated for edge {e}")
                if e._flow > 0 and e.opposite()._flow > 0:
                    raise RuntimeError(f"flow in both directions {e} and {e.opposite()}")

                # update flow in and flow out for checking later
                flow_out[e._source] += e._flow
                flow_in[e._dest] += e._flow

        # check the conservation constraint for all vertices except the source and sink
        for v in range(n):
            if v != source and v != sink and flow_out[v] != flow_in[v]:
                raise RuntimeError(f"conservation constraint violated at vertex {v}: flow in={flow_in[v]} != flow_out={flow_out[v]}")
            
        
        
