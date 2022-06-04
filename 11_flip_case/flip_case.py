def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ""
    for char in phrase:
        if to_swap == char or to_swap == char.swapcase() :
            new_phrase = new_phrase + char.swapcase()
        else:
            new_phrase = new_phrase + char
    # print(new_phrase)
    return new_phrase