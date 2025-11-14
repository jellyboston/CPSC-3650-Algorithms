from flow_graph import FlowGraph

'''
      a1 ----> b1 ----> a2 ----> b2 ----> a3 ----> b3
     /  \       |      /  \       |      /  \
    /    \      |     /    \      |     /    \
   s      \     v    /      \     v    /      t
    \      >   t    /        >   t    /
     \            /
      > b1   b2   b3   (extra edges s -> b_i)
'''
def requires_backward(n: int):
    """
    Construct a flow network where Ford–Fulkerson *without* backward edges
    can get stuck at at most (1/n) of the true max flow.

    Returns (graph, source, sink, bad_path) where:
      - graph : FlowGraph with O(n) vertices and edges, integer capacities
      - source: index of the source node
      - sink  : index of the sink node
      - bad_path: an s–t path such that pushing 1 unit of flow along it first
                  makes any FF implementation (that ignores backward edges)
                  perform very poorly compared to one that uses them.

    Idea:
      - Create a "chain" of capacity-1 edges from s to t.
      - Add many extra s→right and left→t edges (also capacity 1).
      - If you first send 1 unit along the chain, these extra routes become
        mostly unusable unless the algorithm uses backward edges to reroute.
    """

    source = 0
    sink = 2 * n + 1              # vertices: 0..2n+1
    graph = FlowGraph(sink + 1)   # total of 2n+2 vertices

    # We will use:
    #   left i   = 1 + i        for i = 0..n-1    (these are a_1..a_n)
    #   right i  = 1 + n + i    for i = 0..n-1    (these are b_1..b_n)

    bad_path = [source]           # we will build the chain path s -> ... -> t

    for i in range(n):
        left  = 1 + i
        right = 1 + n + i

        # Chain edges (capacity 1):
        # For i = 0:   s -> left(0) = a_1
        # For all i:   left(i) -> right(i)   (a_i -> b_i)
        # For i < n-1: right(i) -> left(i+1) (b_i -> a_{i+1})
        # For i = n-1: right(i) -> t         (b_n -> t)
        if i == 0:
            graph.add_edge(source, left, 1)   # s -> a_1

        graph.add_edge(left, right, 1)        # a_i -> b_i

        if i < n - 1:
            next_left = left + 1              # a_{i+1}
            graph.add_edge(right, next_left, 1)
        else:
            graph.add_edge(right, sink, 1)    # b_n -> t

        # Extra edges enabling a much bigger max flow (if used well):
        #   s -> b_i   (right nodes)
        #   a_i -> t   (left nodes)
        graph.add_edge(source, right, 1)      # s -> b_i
        graph.add_edge(left, sink, 1)         # a_i -> t

        # Build the "bad" augmenting path along the chain:
        # s, a1, b1, a2, b2, ..., a_n, b_n, t
        bad_path.extend([left, right])

    bad_path.append(sink)

    return graph, source, sink, bad_path
