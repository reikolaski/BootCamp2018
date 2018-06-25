from itertools import combinations

def count_sets(cards):
    """Return the number of sets in the provided Set hand.
    Parameters:
        cards (list(str)) a list of twelve cards as 4-bit integers in
        base 3 as strings, such as ["1022", "1122", ..., "1020"].
    Returns:
        (int) The number of sets in the hand.
    Raises:
        ValueError: if the list does not contain a valid Set hand, meaning
            - there are not exactly 12 cards,
            - the cards are not all unique,
            - one or more cards does not have exactly 4 digits, or
            - one or more cards has a character other than 0, 1, or 2.
"""
    if len(cards) != 12:
        raise ValueError("there are not exactly 12 cards")
    if len(set(cards)) != 12:
        raise ValueError("the cards are not all unique")
    for card in cards:
        if len(card) != 4:
            raise ValueError("one or more cards does not have exactly 4 digits")
    for i in set(''.join(cards)):
        if int(i) not in (0, 1, 2):
            raise ValueError("one or more cards has a character other than 0, 1, or 2")
    count = 0
    for combo in combinations(cards, 3):
        if is_set(combo[0], combo[1], combo[2]):
            count += 1
    return count

def is_set(a, b, c):
    """Determine if the cards a, b, and c constitute a set.
    Parameters:
        a, b, c (str): string representations of 4-bit integers in base 3.
            For example, "1022", "1122", and "1020" (which is not a set).
    Returns:
        True if a, b, and c form a set, meaning the ith digit of a, b,
            and c are either the same or all different for i=1,2,3,4.
        False if a, b, and c do not form a set.
    """
    for i in range(4):
        if not sum([int(a[i]), int(b[i]), int(c[i])]) % 3 == 0:
            return False
    return True