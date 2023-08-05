"""Compare floating point values"""
from . import isclose  # type: ignore


def eq(a, b, rel_tol=1e-09, abs_tol=0.0):  # pylint: disable=invalid-name
    # type: (float, float, float, float) -> bool
    """Test ~`a == b` or `abs(a - b) < tolerance`

    Arguments:
        a {float} -- value
        b {float} -- another value

    Keyword Arguments:
        rel_tol {float} -- relative tolerance (default: {1e-09})
        abs_tol {float} -- absolute tolerance (default: {0.0})

    Returns:
        bool -- `a` is similar to `b`
    """
    return isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


def ne(a, b, rel_tol=1e-09, abs_tol=0.0):  # pylint: disable=invalid-name
    # type: (float, float, float, float) -> bool
    """Test ~`a != b` or `abs(a - b) > tolerance`

    Arguments:
        a {float} -- value
        b {float} -- another value

    Keyword Arguments:
        rel_tol {float} -- relative tolerance (default: {1e-09})
        abs_tol {float} -- absolute tolerance (default: {0.0})

    Returns:
        bool -- values are dissimilar
    """
    return not isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


def lt(a, b, rel_tol=1e-09, abs_tol=0.0):  # pylint: disable=invalid-name
    # type: (float, float, float, float) -> bool
    """Test `a < b`, or `a - b < 0 - tolerance`

    Arguments:
        a {float} -- value
        b {float} -- another value

    Keyword Arguments:
        rel_tol {float} -- relative tolerance (default: {1e-09})
        abs_tol {float} -- absolute tolerance (default: {0.0})

    Returns:
        bool -- `a` is unambigously less than `b`
    """
    return a < b and not isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


def gt(a, b, rel_tol=1e-09, abs_tol=0.0):  # pylint: disable=invalid-name
    # type: (float, float, float, float) -> bool
    """Test `a`(-ish) > `b`(-ish)

    Arguments:
        a {float} -- value
        b {float} -- another value

    Keyword Arguments:
        rel_tol {float} -- relative tolerance (default: {1e-09})
        abs_tol {float} -- absolute tolerance (default: {0.0})

    Returns:
        bool -- `a` is unambigously greater than `b`
    """
    return a > b and not isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


def ge(a, b, rel_tol=1e-09, abs_tol=0.0):  # pylint: disable=invalid-name
    # type: (float, float, float, float) -> bool
    """Test `a`(-ish) >= `b`(-ish)

    Arguments:
        a {float} -- value
        b {float} -- another value

    Keyword Arguments:
        rel_tol {float} -- relative tolerance (default: {1e-09})
        abs_tol {float} -- absolute tolerance (default: {0.0})

    Returns:
        bool -- `a` is greater than/similar to `b`
    """
    return not lt(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


def le(a, b, rel_tol=1e-09, abs_tol=0.0):  # pylint: disable=invalid-name
    # type: (float, float, float, float) -> bool
    """Test `a`(-ish) <= `b`(-ish)

    Arguments:
        a {float} -- value
        b {float} -- another value

    Keyword Arguments:
        rel_tol {float} -- relative tolerance (default: {1e-09})
        abs_tol {float} -- absolute tolerance (default: {0.0})

    Returns:
        bool -- `a` is less than/similar to `b`
    """
    return not gt(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
