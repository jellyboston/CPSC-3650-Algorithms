from flow_graph import FlowGraph

def requires_backward(n):
    """
        Returns a flow graph with integer capacities and size linear
        in n along with a path in that graph with positive residual
        capacity such that after adding the maximum possible flow
        along that path, the maximum flow achieved by Ford-Fulkerson
        without backward edges is less than 1/n the maximum flow
        possible when allowing backward edges.  The graph and path are
        returned as a tuple (g, s, t, p) where g is the graph, s is
        the index of the source vertex in g, t is the index of the
        sink vertex in g, and p is the source-to-sink path that, when
        flow is added along it, blocks Ford-Fulkerson from achieving
        maximum flow when now using backward edges, given as a list
        of vertices.

        n -- an integer greater than 1

        Requirements:
        - Max flow broken FF <= 1/n max flow normal FF 
        - We need to find a path that prevents flow from being added with normal FF?
        - flow_with >= n * flow_without
    """
    # YOUR SOLUTION HERE
    # make a graph with two vertices (souce 0, sink 1)
    g = FlowGraph(4)

    # add edge (0, 1) with capacity 1
    g.add_edge(0, 1, 1)
    g.add_edge(1, 3, 1)
    g.add_edge(0, 2, n)
    g.add_edge(2, 1, n)

    src, sink = 0, 3
    p = [0, 1, 3]

    return g, src, sink, p
