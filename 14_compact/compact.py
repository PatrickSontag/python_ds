def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    result = []
    for item in lst:
        # print("item: ", item)
        # print("not not item: ", not not item)
        if not not item:
            result.append(item)
            # print(result)
        # else:
            # print("not this time")
    return result