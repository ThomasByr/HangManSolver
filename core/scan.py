__all__ = ["freq"]

from typing import Counter


def freq(l: list):
    """
    fetch frequency of letters for all words in l

    Parameters
    ----------
        l : list
            list of words
    
    Returns
    -------
        str : letters, sorted by frequency
    """
    d = dict()
    for w in l:
        for c in w:
            try:
                d[c] += 1
            except KeyError:
                d[c] = 1
    return "".join(
        list(
            map(lambda e: str(e[0]),
                sorted(d.items(), key=lambda x: x[1], reverse=True))))
