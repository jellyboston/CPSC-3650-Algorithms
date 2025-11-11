import sys

import flow
import update
import backward

def main():
    if len(sys.argv) < 2:
        print(f"{sys.argv[0]}: requires n argument")
        return
    n = int(sys.argv[1])
    if n <= 1:
        print(f"{n} must be at least 2; got {n}")
        return
    
    g, s, t, p = backward.requires_backward(n)

    # check number of vertices
    if g.size() > 4 * n:
        print(f"graph must have at most 4n={4 * n} vertices; got {g.size()}")
        return

    # check number of edges and no edges into source or out of sink
    edge_count = 0
    for u in range(g.size()):
        for e in g.edges(u):
            edge_count += 1
            if e.destination() == s and e.capacity() > 0:
                print(f"can't have edge with positive capacity into source")
                return
            if u == t and e.capacity() > 0:
                print(f"can't have edge with positive capacity out of sink")
                return
    if edge_count > 16 * n:
        print(f"graph must have at most 16n={16 * n} edges; got {edge_count}")

    # validate source and sink
    if s < 0 or s >= g.size():
        print(f"invalid source vertex {s}")
        return
    if t < 0 or t >= g.size():
        print(f"invalid sink vertex {t}")
        return
    if s == t:
        print("source and sink must be distinct")
        return

    # check that path is source to sink
    if len(p) < 2:
        print(f"path must contain at least source and sink")
        return

    if p[0] != s:
        print(f"path must start at source {s}, not {p[0]}")
        return
    if p[-1] != t:
        print(f"path must end at sink {t}, not {p[-1]}")
        return
    
    # convert list of vertices into list of edges
    used = [False] * g.size()
    used[s] = True
    path = []
    for i in range(len(p) - 1):
        src = p[i]
        dest = p[i + 1]

        # check for cycles
        if used[dest]:
            print(f"path repeats vertex {dest}")
            return
        used[dest] = True
        
        # check that vertex indices are valid
        if src < 0 or src >= g.size():
            print(f"invalid vertex {src} in path")
            return

        e = g.find_edge(src, dest)
        if e is None:
            print(f"edge ({src},{dest}) does not exist")
            return
        
        # find the edge (total time here still linear)
        path.append(e)

    # add flow along the path
    b = min(e.residual() for e in path)
    if b < 1:
        print(f"all edges in path must have positive residual capacity; got {b}")
    for e in path:
        update.update(e, e.opposite(), b)
        
    # use Ford-Fulkerson without backward edges to add more flow and
    # get value of resulting flow
    flow.ford_fulkerson(g, s, t, lambda e: e.residual() > 0 and e.capacity() > 0)
    flow_wo = g.value(s)

    # use unrestricted Ford-Fulkerson to add more flow and get value of flow
    flow.ford_fulkerson(g, s, t)
    flow_with = g.value(s)

    # check that there is at least n times more flow with backward edges
    if flow_with < n * flow_wo:
        print(f"got {flow_wo} flow w/o backward edges; {flow_with} flow with; required {flow_wo * n}")
    else:
        print(f"flow ratio at least {n}")
        
        
if __name__ == "__main__":
    main()
