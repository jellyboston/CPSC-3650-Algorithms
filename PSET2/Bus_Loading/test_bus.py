'''
To run:
pytest {file path} -q
'''
import pytest
from bus import optimize_loading

# ---- Table of test cases (input -> expected) ----
# TIP: keep these as *data only*; no logic here.
basic_cases = [
    # TODO: add a small, clear base case
    dict(
        name="specs_case",
        input_group=[4, 5, 6, 3, 2, 4],
        input_cap=10,
        expected=[0, 2, 4]
    ), 
    dict(name="single_exact", input_group=[7], input_cap=7, expected=[0]),
    dict(name="all_equal_capacity", input_group=[10,10,10], input_cap=10, expected=[0,1,2]),
    dict(name="fills_then_new", input_group=[4,6,3], input_cap=10, expected=[0,2]),
    dict(name="partial_last", input_group=[2,2,2], input_cap=5, expected=[0,2]),
    dict(name="large_front", input_group=[9,2,2], input_cap=10, expected=[0,1]),
    dict(name="large_end", input_group=[2,2,9], input_cap=10, expected=[0,2]),
    dict(name="all_tiny", input_group=[1,1,1,1,1], input_cap=10, expected=[0]),
]

@pytest.mark.parametrize(
    "case", # var name used in test function
    basic_cases, # list of dictionaries
    ids=[c["name"] for c in basic_cases] if basic_cases else []
)
def test_basic(case):
    # Arrange
    expected = case["expected"]

    # Act
    bus_starts = optimize_loading(case["input_group"], case["input_cap"])

    # Assert
    assert bus_starts == expected
