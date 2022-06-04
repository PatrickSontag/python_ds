def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    count = {}
    top_number = None
    highest_count = None
    for num in nums:
        if not num in count:
            count[num] = 1
        else:
            count[num] += 1
    # print(count)
    for (digit, total) in count.items():
        if highest_count == None:
            top_number = digit
            highest_count = total
        else:
            if total > highest_count:
                top_number = digit
                highest_count = total
    return top_number

