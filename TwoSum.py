def TwoSumDict(nums, target):
    #runtime: 40ms
    #memory: 14.3 MB
    checked = {}
    for i, num in enumerate(nums):
        check = target - num
        if check in checked:
            return [checked[check], i]
        else:
            checked[num] = i
def TwoSumBrute(nums, target):
    #runtime: 1636ms
    #memory: 13.9 MB
    for i in range(0, len(nums)):
        val = nums[i]
        otherVal = target - val
        checkArr = nums[0:i] + nums[i+1:]
        try:
            checkIndex = checkArr.index(otherVal)
        except ValueError:
            checkIndex = -1
        if checkIndex >= i:
            checkIndex += 1
        if checkIndex >= 0:
            return [min(i, checkIndex), max(i, checkIndex)]

print(TwoSumDict([-1,-2,-3,-4, -5], -8))
print(TwoSumBrute([-1,-2,-3,-4, -5], -8))


          

