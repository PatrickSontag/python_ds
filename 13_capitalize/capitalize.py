def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    new_phrase = ""
    for char in phrase:
        if new_phrase == "":
            new_phrase = new_phrase + char.upper()
        else: new_phrase = new_phrase + char

    return new_phrase