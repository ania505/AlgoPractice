# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
       
        point1 = head
        point2 = head
        while head.next != None:
            point2 = point2.next;
            # head = head.next
            # if head.next == None:
            #     point2 = head
        
        while point1 != point2:
            if point1.val != point2.val:
                return False
            point1 = point1.next
            point2 = point2.prev
            if point1.prev == point2 and point2.next == point1:
                break
        return True
    
    
        print(head.val)
        while head.next != None:
            head = head.next
            print(head.val)