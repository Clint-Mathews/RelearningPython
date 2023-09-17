# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def printNodes(node: ListNode):
    while node != None:
        print(node.val, "->")
        node = node.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = list2
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
                temp.next = list2
                if prev != None:
                    prev.next = temp
                else:
                    current = temp
                prev = temp
            else:
                prev = list2
                list2 = list2.next

        if list1 != None:
            prev.next = list1

        return current




if __name__=='__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    sol = Solution()
    updatedNode = sol.mergeTwoLists(node1, node2)
    print("updatedNode")
    printNodes(updatedNode)