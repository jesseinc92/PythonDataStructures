def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    swapped_string = str()

    for letter in phrase:
        if letter == to_swap:
            swapped_string += letter.swapcase()
        elif letter == to_swap.upper() or letter == to_swap.lower():
            swapped_string += letter.swapcase()
        else:
            swapped_string += letter
    

    return swapped_string