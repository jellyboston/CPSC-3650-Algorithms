from graph import Graph
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
    # translate into diretcted graph by adding forward/back edges
    for u in range(V):
        for v, w in car.edges(u):
            # process each undirected edge once
            if u < v: 
                # add layer of car edges
                H.add_edge(L0(u), L0(v), w)
                H.add_edge(L0(v), L0(u), w)

                # layer of only hyperloop edges
                H.add_edge(L1(u), L1(v), w)
                H.add_edge(L1(v), L1(u), w)
    
    # fill with possible car <-> hyperloop connected vertices with hyperloop weights
    for u in range(V):
        for v, w in loop.edges(u):
            H.add_edge(L0(u), L1(v), w)
            H.add_edge(L1(v), L0(u), w)

'''
dijsktra explores all possibilities. we must consider two edge cases:
    1. the hyperloop is not needed to get the SSSP (dest. will be in layer 0)
    2. the hyperloop was used (dest. will be in layer 1)
Take the fastest of the two as they were both existing possibilities found by Dijsktra's.
'''    
def expanded_dijsktra(H, source, dest):
    sssp = H.dijkstra(L0(source))
    fastest_no_coupon = sssp[L0(dest)].d
    fastest_used_coupon = sssp[L1(dest)].d
    return min(fastest_no_coupon, fastest_used_coupon)

def find_route(car, loop, source, dest):
    """ Finds the shortest path from sourse to destination and returns it as a list
        of edges with the mode used.

        car -- an undirected, weighted graph with non negative-weight edges
        loop -- an undirected, weighted graph with the same edges as car and corresponding weights no greater
        source -- the index of a vertex in the graphs
        dest -- the index of a vertex in the graphs reachable from and not equal to source
    """
    # YOUR SOLUTION HERE
    '''
    My Idea so far:
    1. Read graph size V
    2. Build expanded graph H with 2*V vertices
    3. Add CAR edges to H
        (u,0) <-> (v,0) with weight w
        (u,1) <-> (v,1) with weight w
    4. Add Hyperloop edges to H as one-time coupon transitions
        (u,0) -> (v,1) with weight w
        (v,0) -> (u,1) with weight w
    5. Run Dijsktra once from (s,0)
    6. Choose best end state 
    7. Reconstruct expanded-graph node path using parent[]
    8. Convert to output
    '''

    # build expanded graph H to hold car/loop vertices (size 2V)
    V = car.size()
    expanded_graph = Graph(2 * V)

    # add car edges to both layers; connect layers with the hyperloop edges
    fill_expanded_graph(expanded_graph, V, car, loop)

    # run dijsktra starting from source layer 0
    shortest_to_dest = expanded_dijsktra(expanded_graph, source, dest)

    # trace back to identify the parent of each node and format to exp output
    
    

    return [] # here to keep Python validator happy (routing.py imports hyperloop.py even though not used for checking C++ output)
