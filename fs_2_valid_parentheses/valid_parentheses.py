def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count1 = 0
    count2 = 0
    if len(parens) % 2 != 0:
        return False
    for char in parens:
        if char == "(":
            count1 += 1
        if char == ")":
            count2 += 1
        if count2 > count1:
            return False
    # print(count1, " | ", count2)
    if count1 == count2:
        return True
    return False
        
        