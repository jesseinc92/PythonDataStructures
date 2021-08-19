from os import terminal_size


def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    # first successful attempt

    # if isinstance(collection, list) or isinstance(collection, str) or isinstance(collection, set) or isinstance(collection, tuple):
    #     if start == None or isinstance(collection, set):
    #         for val in collection:
    #             if sought == val:
    #                 return True
    #         return False
    #     else:
    #         for idx in range(start, len(collection)):
    #             if sought == collection[idx]:
    #                 return True
    #         return False

    # if isinstance(collection, dict):
    #     for val in collection.values():
    #         if sought == val:
    #             return True
    #     return False

    # second attempt, using solution

    if isinstance(collection, dict):
        return sought in collection.values()

    if start == None or isinstance(collection, set):
        return sought in collection

    return sought in collection[start:]