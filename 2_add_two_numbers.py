from typing import Optional

# Definition for singly-linked list.
# Note - Keep the ListNode class definition Commented while copying it to leet code.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None) -> None:
        self.val: int = val
        self.next: Optional['ListNode'] = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists.
        Each node contains a single digit, and digits are stored in reverse order.

        Example:
            Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
            Output: 7 -> 0 -> 8
            Explanation: 342 + 465 = 807

        Args:
            l1 (Optional[ListNode]): Head of the first linked list.
            l2 (Optional[ListNode]): Head of the second linked list.

        Returns:
            Optional[ListNode]: Head of the new linked list representing the sum.
        """

        dummy_head: ListNode = ListNode(0)         # Placeholder head node
        current_node: ListNode = dummy_head         # Pointer to build result list
        carry: int = 0                              # Carry for values > 9

        # Process until both lists and carry are exhausted
        while l1 is not None or l2 is not None or carry != 0:
            # Get node values or 0 if list has ended
            value1: int = l1.val if l1 is not None else 0
            value2: int = l2.val if l2 is not None else 0

            # Calculate digit sum and carry
            total: int = value1 + value2 + carry
            sum_value: int = total % 10
            carry = total // 10

            # Create a new node with computed digit
            new_node: ListNode = ListNode(sum_value)
            current_node.next = new_node
            current_node = new_node

            # Move to next nodes
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # Return the next node after dummy head
        return dummy_head.next
