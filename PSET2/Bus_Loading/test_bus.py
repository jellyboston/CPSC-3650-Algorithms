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
        expected=[0, 3, 5]
    )
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
    group_indices = optimize_loading(case["input_group"], case["input_cap"])

    # Assert
    assert group_indices == expected
