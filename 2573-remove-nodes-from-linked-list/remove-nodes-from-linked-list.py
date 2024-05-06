# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = head
        arr = []
        stack= []
        while new_node is not None:
            arr.append(new_node.val)
            new_node = new_node.next
        for i in range(len(arr)):
            if stack:
                if stack[-1]>arr[i]:
                    stack.append(arr[i])
                else:
                    while stack:
                        if stack[-1]<arr[i]:
                            stack.pop()
                        else:
                            break
                    stack.append(arr[i])
            else:
                stack.append(arr[i])
        if not stack:
            return head
        else:
            new_head = ptr = ListNode()
            for i in range(len(stack)):
                ptr.val = stack[i]
                if i<len(stack)-1:
                    ptr.next = ListNode()
                    ptr = ptr.next
            
            return new_head
        