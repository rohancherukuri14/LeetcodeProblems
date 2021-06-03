def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    total = 0
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if len(s) == 1:
        return values[s]
    for i in range(0, len(s) - 1):
        roman_num = s[i]
        next_roman_num = s[i+1]
        val = values[roman_num]
        next_val = values[next_roman_num]
        if val < next_val:
            total -= val
        else:
            total += val
    total += next_val
    return total