# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodey = ListNode(3)
        position = 2
        
        posCount = 0
        reset = head
        while head.next != None:
            print
            head = head.next
            if posCount == position-2:
                temp = head.next
                head.next = nodey
                nodey.next = temp
                
            posCount+=1
        
        head = reset
        print(head.val)
        while head.next != None:
            head = head.next
            print(head.val)