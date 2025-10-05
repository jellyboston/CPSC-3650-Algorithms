from digraph import Digraph
'''
    High level callouts:
    - we establish two different layers: layer 0 (coupon unused) and 1 (used) within the graph
    - Layer 0 coupons -> 0...V-1 and Layer 1 -> V..2V-1
'''
def L0(v):
    return v
def L1(v, OFFSET):
    return v + OFFSET
def is_hyper_edge(a, b, OFFSET):
    # checks if the edge uses a hyperloop
    return a < OFFSET and b >= OFFSET

'''
Visually, you can think of this new graph as a sandwich. Both layers
contain car edges. Layer 1 is stacked on top, layer 0 on the bottom.
It is the hyperloop weights in the second loop that connect
these two layers together. 
'''
def fill_expanded_graph(H, V, car, loop):
    OFFSET = V
    # translate into diretcted graph by adding forward/back edges
    for u in range(V):
        for v, w in car.edges(u):
            # process each undirected edge once
            if u < v: 
                # add car edges to each layer
                H.add_edge(L0(u), L0(v), w)
                H.add_edge(L0(v), L0(u), w)
                H.add_edge(L1(u, OFFSET), L1(v, OFFSET), w)
                H.add_edge(L1(v, OFFSET), L1(u, OFFSET), w)
    
    # fill with possible car <-> hyperloop connected vertices with hyperloop weights
    for u in range(V):
        for v, w in loop.edges(u):
            # again, avoid double adding
            if u < v:
                H.add_edge(L0(u), L1(v, OFFSET), w)
                H.add_edge(L0(v), L1(u, OFFSET), w)

'''
dijsktra explores all possibilities. we must consider two edge cases:
    1. the hyperloop is not needed to get the SSSP (dest. will be in layer 0)
    2. the hyperloop was used (dest. will be in layer 1)
Take the fastest of the two as they were both existing possibilities found by Dijsktra's.
'''    
def expanded_dijsktra(H, V, source, dest):
    OFFSET = V
    sssp = H.dijkstra(L0(source))

    # dest node in each of the layers
    end0, end1 = L0(dest), L1(dest, OFFSET)
    fastest_no_coupon = sssp[end0].d
    fastest_used_coupon = sssp[end1].d

    # edge case: no routes
    if fastest_no_coupon == float('inf') and fastest_used_coupon == float('inf'):
        return None, None, None
    
    # select node index to backtrack from next
    end = end0 if fastest_no_coupon <= fastest_used_coupon else end1
    return sssp, end

def find_route(car, loop, source, dest):
    """ Finds the shortest path from sourse to destination and returns it as a list
        of edges with the mode used.

        car -- an undirected, weighted graph with non negative-weight edges
        loop -- an undirected, weighted graph with the same edges as car and corresponding weights no greater
        source -- the index of a vertex in the graphs
        dest -- the index of a vertex in the graphs reachable from and not equal to source
    """
    # YOUR SOLUTION HERE
    # build expanded graph H to hold car/loop vertices (size 2V)
    V = car.size()
    expanded_graph = Digraph(2 * V)

    # add car edges to both layers; connect layers with the hyperloop edges
    fill_expanded_graph(expanded_graph, V, car, loop)

    # run dijsktra starting from (source, layer 0)
    sssp_tree, end = expanded_dijsktra(expanded_graph, V, source, dest)
    if sssp_tree is None:
        return []
    
    # trace back to identify the parent of each node and format to exp output
    results = []
    node = end
    start_idx = L0(source)
    while node is not None and node != start_idx:
        parent = sssp_tree[node].parent
        if parent is None:
            break
        # if expanded, convert offset indices back to og vertex ids
        u = parent % V
        v = node % V

        # format
        mode = "hyperloop" if (parent < V and node >= V) else "car"
        results.append((u, v, mode))

        # increment next
        node = parent
    results.reverse()
    return results