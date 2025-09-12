# test_scc.py
import pytest
from digraph import Digraph
from scc import sccs  # your function under test


scc_test_cases = [
    # ------------------ Singles / trivial ------------------
    pytest.param(
        1, [],
        [ {0} ],
        id="S1: single vertex, no edges"
    ),
    pytest.param(
        1, [(0,0)],
        [ {0} ],
        id="S1a: single vertex with self-loop"
    ),

    # ------------------ Simple DAGs / chains ------------------
    pytest.param(
        3, [(0,1),(1,2)],
        [ {0},{1},{2} ],
        id="S2: simple chain DAG (all singletons)"
    ),
    pytest.param(
        6, [(0,1),(1,2),(2,3),(3,4),(4,5)],
        [ {0},{1},{2},{3},{4},{5} ],
        id="S13: long chain DAG (all singletons)"
    ),
    pytest.param(
        4, [(0,1),(0,2),(1,3),(2,3)],
        [ {0},{1},{2},{3} ],
        id="S6: diamond DAG (middle order flexible)"
    ),

    # ------------------ Pure SCCs ------------------
    pytest.param(
        3, [(0,1),(1,2),(2,0)],
        [ {0,1,2} ],
        id="S3: one big SCC (3-cycle)"
    ),
    pytest.param(
        4, [(0,0),(1,1),(2,2)],
        [ {0},{1},{2},{3} ],
        id="S9: self-loops don’t merge SCCs"
    ),
    pytest.param(
        4, [(0,1),(1,2),(2,0),(2,3),(3,1)],
        [ {0,1,2,3} ],
        id="S11: hidden merge via back-edge (everything collapses)"
    ),

    # ------------------ Multi-SCC with forced order ------------------
    pytest.param(
        4, [(0,1),(1,0), (2,3),(3,2), (1,2)],   # {0,1} -> {2,3}
        [ {0,1}, {2,3} ],
        id="S4: two SCCs with A→B"
    ),
    pytest.param(
        6,
        [
            (0,1),(1,2),(2,0),      # A = {0,1,2}
            (3,4),(4,3),            # C = {3,4}
            (2,5),                  # A→B
            (5,3)                   # B→C
        ],
        [ {0,1,2}, {5}, {3,4} ],
        id="S5: three SCCs with unique chain A→B→C"
    ),
    pytest.param(
        3, [(0,1),(1,0),(1,2)],     # {0,1} -> {2}
        [ {0,1}, {2} ],
        id="S7: two-vertex SCC feeding a tail"
    ),

    # ------------------ Disconnected subgraphs / flexible order ------------------
    pytest.param(
        4, [(0,1),(1,0), (2,3)],    # {0,1}, {2}, {3} (no cross edges)
        [ {0,1}, {2}, {3} ],
        id="S8: disconnected components (relative order flexible)"
    ),
    pytest.param(
        4, [(0,1),(0,1),(1,0),(2,3),(2,3)],  # parallel edges ok
        [{0,1}, {2}, {3}],
        id="S12: two SCCs with parallel edges (order flexible)"
    ),

    # ------------------ Larger mixed with unique chain ------------------
    pytest.param(
        8,
        [
            (0,1),(1,2),(2,0),      # A={0,1,2}
            (3,3),                  # B={3}
            (4,5),(5,4),            # C={4,5}
            (6,7),(7,6),            # D={6,7}
            (2,3), (3,4), (5,6)     # A→B→C→D
        ],
        [ {0,1,2}, {3}, {4,5}, {6,7} ],
        id="S10: multi-size SCCs with chain A→B→C→D"
    ),
]

def _partition_ok(n, result, expected_partition):
    # result: list[list[int]]; expected_partition: list[set[int]]
    # 1) cover exactly all vertices once
    flat = [v for comp in result for v in comp]
    assert set(flat) == set(range(n)), "Vertices missing or duplicated"
    # 2) components are disjoint and count matches
    assert sum(len(c) for c in result) == n
    assert len(result) == len(expected_partition)
    # 3) compare as sets ignoring order
    got_sets = [set(c) for c in result]
    assert sorted(map(sorted, got_sets)) == sorted(map(sorted, expected_partition)), \
        f"Component membership mismatch.\nGot: {got_sets}\nExp: {expected_partition}"

def _topo_ok(result, edges):
    # Build comp index map by output order; then check every edge goes within
    # the same comp or from earlier comp to later comp.
    comp_index = {}
    for i, comp in enumerate(result):
        for v in comp:
            comp_index[v] = i
    for u, v in edges:
        if comp_index[u] > comp_index[v]:
            raise AssertionError(
                f"Topological order violated: edge {u}->{v} goes from comp {comp_index[u]} "
                f"to earlier comp {comp_index[v]}"
            )

@pytest.mark.parametrize("n, edges, expected_partition", scc_test_cases)
def test_sccs(n, edges, expected_partition):
    g = Digraph(n)
    for u, v in edges:
        g.add_edge(u, v)
    res = sccs(g)
    _partition_ok(n, res, expected_partition)
    _topo_ok(res, edges)
