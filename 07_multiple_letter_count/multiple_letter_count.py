def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    count = {}

    for char in phrase:
        if count.get(char) == None:
            count[char] = 1
        else:
            count[char] = count[char] + 1

    return count
        
