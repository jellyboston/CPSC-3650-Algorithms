# test_detect_wheel.py
import pytest
from graph import Graph
from wheel import is_wheel

test_cases = [
    # ----------------------- Positives (T*) -----------------------
    pytest.param(
        5,
        [(0,1),(1,2),(2,3),(3,0),(4,0),(4,1),(4,2),(4,3)],
        True,
        id="T1: W5 (valid wheel: hub=4, rim 0-1-2-3-0)"
    ),
    pytest.param(
        7,
        [(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),
         (6,0),(6,1),(6,2),(6,3),(6,4),(6,5)],
        True,
        id="T2: W7 (valid wheel: hub=6, full rim cycle)"
    ),

    # ----------------------- Negatives (N*) -----------------------
    pytest.param(
        5,
        [(4,0),(4,1),(4,2),(4,3)],
        False,
        id="N1: Star only (no rim cycle)"
    ),
    pytest.param(
        6,
        [(0,1),(1,2),(2,3),(3,4),  # missing (4,0)
         (5,0),(5,1),(5,2),(5,3),(5,4)],
        False,
        id="N2: Missing one rim edge (no simple cycle)"
    ),
    pytest.param(
        6,
        [(0,1),(1,2),(2,3),(3,4),(4,0),(2,4),  # extra chord
         (5,0),(5,1),(5,2),(5,3),(5,4)],
        False,
        id="N3: Extra chord on rim (rim not a simple cycle)"
    ),
    pytest.param(
        6,
        # rim
        [(0,1),(1,2),(2,3),(3,4),(4,0),
        # hub 5 (to all rim vertices)
         (5,0),(5,1),(5,2),(5,3),(5,4),
        # make 0 also hub-like (0 connected to 1,2,3,4,5)
         (0,2),(0,3),(0,4)],
        False,
        id="N4: Two hubs exist (violates 'exactly one hub')"
    ),
    pytest.param(
        6,
        [(0,1),(1,2),(2,0),(3,4)],  # disconnected components
        False,
        id="N5: Disconnected graph"
    ),
    pytest.param(
        5,
        [(0,1),(0,2),(0,3),(0,4),
         (1,2),(1,3),(1,4),
         (2,3),(2,4),
         (3,4)],
        False,
        id="N6: Complete graph K5 (too many edges; rim not a simple cycle)"
    ),
    pytest.param(
        6,
        [(0,1),(1,2),(2,3),(3,4),(4,0),
         (5,0),(5,1),(5,2),(5,3)],  # 5 missing neighbor 4
        False,
        id="N7: 'Hub' missing one neighbor (no degree n-1 vertex)"
    ),

    # ----------------------- Robustness (R*) ----------------------
    pytest.param(
        5,
        # Valid W5 but labels permuted; rim = {4,2,0,3}, hub = 1
        [(4,2),(2,0),(0,3),(3,4),
         (1,4),(1,2),(1,0),(1,3)],
        True,
        id="R1: Valid wheel with permuted labels (label-agnostic)"
    ),
    pytest.param(
        7,
        # Wheel on {0..5} with hub 5; vertex 6 isolated → should fail
        [(0,1),(1,2),(2,3),(3,4),(4,0),
         (5,0),(5,1),(5,2),(5,3),(5,4)],
        False,
        id="R2: Wheel + isolated vertex (graph must be exactly the wheel)"
    ),
    pytest.param(
        7,
        # Two disjoint 3-cycles around hub 6 → not a single rim cycle
        [(0,1),(1,2),(2,0),
         (3,4),(4,5),(5,3),
         (6,0),(6,1),(6,2),(6,3),(6,4),(6,5)],
        False,
        id="R3: Two rim cycles (violates single simple rim cycle)"
    ),

    # ----------------------- Preconditions (P*) -------------------
    pytest.param(
        4,
        [(0,1),(1,2),(2,3),(3,0)],
        False,
        id="P0: n < 5 (fails size precondition)"
    ),
]

@pytest.mark.parametrize("n, edges, expected", test_cases)
def test_is_wheel(n, edges, expected):
    g = Graph(n)
    for u, v in edges:
        g.add_edge(u, v)
    assert is_wheel(g) == expected
