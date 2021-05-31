def isPalindrome1(x):
    #Runtime: 36 ms
    #Memory: 13.4 MB
    s = str(x)
    return s[::-1] == s


def isPalindrome2(x):
    #Runtime: 64 ms
    #Memory: 13.5 MB
    rev = 0
    length = len(str(x)) - 1
    place = 0
    x_cop = x
    while (x > 0):
        rev += (x%10) * (10 ** (length-place))
        x = x // 10
        place += 1
    return x_cop == rev

print(isPalindrome2(121))


