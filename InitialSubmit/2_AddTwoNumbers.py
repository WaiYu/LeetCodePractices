# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    answer = ListNode(l1.val + l2.val)
    increment = int(answer.val / 10)
    answer.val = answer.val % 10
    if (l1.next == None) and (l2.next == None):
      if (increment):
        answer.next = ListNode(1)
      return answer
    if (l1.next == None):
      l1.next = ListNode(increment)
    elif ((l2.next == None) and (l1.next != None)):
      l2.next = ListNode(increment)
    else:
      if (increment):
        l1.next.val += 1
    answer.next = self.addTwoNumbers(l1.next, l2.next)
    
    return answer
    
