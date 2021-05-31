def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if(len(s) <= 1):
        return s
    longest = ''
        
    for i in range(0, len(s)):
        val = s[i]
        next_index = s.find(val, i+1)
        while(next_index > -1):
            length = next_index - i + 1
            if length > len(longest):
                checkSub = s[i:next_index+1]
                if checkSub[::-1] == checkSub:
                    longest = checkSub
            next_index = s.find(val, next_index+1)
    if len(longest) > 0:
        return longest
    else:
        return s[0]

