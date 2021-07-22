from core.scan import *
from core.search import *

__all__ = ["prettyprint"]


def prettyprint(user_space: str, d: list):
    """
    prints the user space in a readable way

    Parameters
    ----------
        user_space: str
            the user space to be printed
        d: list
            list of words
    """
    k = min(
        len(user_space) if " " not in user_space else user_space.index(" "),
        10)
    m = "".join(list(map(str, range(k))))
    print(f"<{user_space}")  # input
    print(f" {m}")  # first k letters indexes (max of 10)
    print(f">{(res := find(user_space, d))}")  # possibilities
    print(f"?{freq(res)}")  # analitics
