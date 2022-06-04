def list_check(lst):
    """Are all items in lst a list?

        >>> 
        True

        >>> list_check([[1], "nope"])
        False
    """
    for item in lst:
        if not isinstance(item, list):
            return False
    return True
