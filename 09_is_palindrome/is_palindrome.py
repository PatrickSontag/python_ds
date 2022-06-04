def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # print("phrase: ", phrase)
    low_phrase = phrase.lower()
    # print("low_phrase: ", low_phrase)
    ready_phrase = low_phrase
    if " " in phrase:
        ready_phrase = low_phrase.replace(" ", "")
    # print("ready_phrase: ", ready_phrase)
    ready_list = list(ready_phrase)
    backwards = []
    for char in ready_list:
        backwards.insert(0, char)
    # print("ready_list: ", ready_list)
    # print("backwards: ", backwards)
    if ready_list == backwards:
        return True
    else:
        return False

