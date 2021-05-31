def lengthOfLongestSubstring(s):
    longest = 0
    check = []
    for i in range(0, len(s)):
        val = s[i]
        if val not in check:
            check.append(val)
            l = len(check)
            if l > longest:
                longest = l
        else:
            while val in check:
                check.pop(0)
            check.append(val)
    return longest
