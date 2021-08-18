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

    # make all characters lowercased

    phrase_list = list(phrase.lower())

    # remove all spaces from the list

    for char in phrase_list:
        if char == ' ':
            phrase_list.remove(char)

    phrase_list_copy = phrase_list.copy()
    phrase_list_copy.reverse()

    if phrase_list == phrase_list_copy:
        return True
    else:
        return False