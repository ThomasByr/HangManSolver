import re  # regex
from unidecode import unidecode_expect_ascii  # great to remove accents

__all__ = ["find"]

# user input
# letters or dots then tested letters
# for eg. : .a.er aeiouls


def _find_with(pattern: str, l: list):
    """
    find all words that match the pattern

    Parameters
    ----------
        pattern: str
            pattern to match
        l: list[str]
            list of words to search

    Returns
    -------
        list[str]: matched words
    """
    p = re.compile(f"{pattern.lower()}$")  # save time
    # filter words that do match the pattern
    filtered = list(filter(lambda x: p.match(x) is not None, l))

    return filtered


def _find_without(letters: str, l: list, input: str):
    """
    find all words that don't contain the letters matching blanks in input

    Parameters
    ----------
        letters: str
            letters not to match
        l: list[str]
            list of words to search
        input: str
            input of the user

    Returns
    -------
        list[str]: matched words
    """
    pos = {i
           for i, e in enumerate(input) if e == "."}  # find positions of dots
    s = set(letters)  # set of letters that were used
    for e in input:  # adding input letters to the set
        if e != ".":
            s.add(e)
            s.add(unidecode_expect_ascii(e))

    filtered = l.copy()
    new = []
    for w in l:  # for each word
        # if any letter in the word is in the set of letters assuming the letter is not a dot
        # discard the word (made it in reverse)
        if all(e not in s for i, e in enumerate(unidecode_expect_ascii(w))
               if i in pos):
            new.append(w)
        filtered = new.copy()  # startting over
    return filtered


def find(input: str, l: list):
    """
    solves hangman game

    Parameters
    ----------
        input: str
            input of the user (must conform to the rules)
        l: list[str]
            list of words to search

    Returns
    -------
        list[str]: matched words
    """
    # reading user input
    try:
        x, y = input.split(maxsplit=1)
    except ValueError:
        x = input
        y = ""

    # filtering
    tmp = l.copy()
    tmp = _find_with(x, tmp)
    tmp = _find_without(y, tmp, x)
    return tmp
