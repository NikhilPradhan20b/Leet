# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(50000)
        new_node = head
        temp = ''
        while new_node is not None:
            temp+=str(new_node.val)
            new_node = new_node.next
        temp = str(int(temp)*2)
        new_head = ptr = ListNode()
        for i in range(len(temp)):
            new_head.val = int(temp[i])
            if i<len(temp)-1:
                new_head.next = ListNode()
                new_head = new_head.next
        return ptr       