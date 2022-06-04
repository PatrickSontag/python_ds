def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    s_list = list(s)
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    tracker = []
    for i, letter in enumerate(s_list):
        if letter in vowels:
            tracker.append(s_list[i])
            s_list = s_list[:i] + [None] + s_list[1 + i:]
    for j, item in enumerate(s_list):
        if item == None:
            x = tracker.pop()
            s_list = s_list[:j] + [x] + s_list[j + 1:]
    result = ''.join(s_list)
    return result
    