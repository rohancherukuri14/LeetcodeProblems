# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ret = ListNode(0)
        tail = ret
        carry = 0
        while l1 or l2 or carry:
            if l1:
                currL1 = l1.val
            else:
                currL1 = 0
            if l2:
                currL2 = l2.val
            else:
                currL2 = 0
            currSum = currL1 + currL2 + carry
            if (currSum > 9):
                currSum -= 10
                carry = 1
            else:
                carry = 0
            
            tail.next = ListNode(currSum)
            tail = tail.next
            
            if (l1):
                l1 = l1.next
            else:
                l1 = None
            if (l2):
                l2 = l2.next
            else:
                l2 = None
        return ret.next