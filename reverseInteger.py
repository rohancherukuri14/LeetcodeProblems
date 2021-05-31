def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    rev = 0
    place = 0
    length = len(str(x)) - 1
    neg = False
    if (x < 0):
        neg = True
        length -= 1
        x = abs(x)
    while(x > 0):
        rev += (x%10) * (10**(length-place))
        x = x//10
        place += 1
    if (rev < -(2**31)) or (rev >= 2**31):
        rev = 0
    if neg:
        return rev * -1
    return rev
