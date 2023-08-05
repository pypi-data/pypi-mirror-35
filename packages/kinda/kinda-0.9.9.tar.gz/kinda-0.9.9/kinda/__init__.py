"""Module init"""
from sys import version_info


# pylint: disable=import-error
if version_info < (3, 5, 0):
    from shim import isclose  # type: ignore  # noqa

else:
    from math import isclose  # type: ignore  # noqa
# pylint: enable=import-error

# pylint: disable=cyclic-import,import-self
if version_info[0] < 3:
    from kinda import eq, ne, lt, gt, ge, le        # type: ignore  # noqa

else:
    from kinda.kinda import eq, ne, lt, gt, ge, le  # type: ignore  # noqa
# pylint: enable=cyclic-import,import-self
