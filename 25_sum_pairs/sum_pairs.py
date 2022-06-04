def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    val_1 = 0
    val_2 = 0
    for idx, num in enumerate(nums):
        if idx != 0:
            val_1 = num
            for idx2, num2 in enumerate(nums):
                if idx2 < idx:
                    val_2 = num2
                    if val_1 + val_2 == goal:
                        return (val_2, val_1)
    return ()
            