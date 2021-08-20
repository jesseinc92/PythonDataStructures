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

    VOWELS = 'aeiou'

    index = []
    vowel = []

    for i in range(len(s)):
        if s[i] in VOWELS:
            index.append(i)
            vowel.append(s[i])

    vowel.reverse()
    string = list(s)
    s = ''

    for i in range(len(index)):
        string[index[i]] = vowel[i]

    for i in range(len(string)):
        s += string[i]

    return s