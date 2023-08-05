"""Shim for Python < 3.5"""


# pylint: disable=invalid-name
def compare_pct(a, b, rel_tol):
    # type: (float, float, float) -> float
    """Calculate max difference as percentage of larger number"""
    max_val = sorted((abs(a), abs(b))).pop()  # type: float

    return max_val * rel_tol


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    # type: (float, float, float, float) -> bool
    """Implement math.isclose where not builtin"""
    diff = abs(a - b)

    return diff <= abs_tol and diff < compare_pct(a, b, rel_tol)
