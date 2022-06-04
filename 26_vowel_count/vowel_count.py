def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    low_phrase = phrase.lower()
    # print("low_phrase ", low_phrase)
    vowels = ["a", "e", "i", "o", "u"]
    final = {}
    vow_count = [low_phrase.count(vowel) for vowel in vowels]
    # print("vow_count ", vow_count)
    for index, letter in enumerate(vowels):
        if vow_count[index] != 0:
            final[letter] = vow_count[index]
    return final
