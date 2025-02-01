class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify result list handling
        dummy = ListNode()
        cur = dummy  # Pointer to construct the result list
        carry = 0  # To handle values greater than 9
        
        # Iterate while there are nodes in l1, l2, or there's a carry left
        while l1 or l2 or carry:
            # Get the values of the current nodes (or 0 if the list is shorter)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Compute the sum of current digits + carry
            val = v1 + v2 + carry
            carry = val // 10  # Extract carry (e.g., 15 -> carry = 1)
            val = val % 10  # Extract the digit to store (e.g., 15 -> store 5)
            
            # Add this value to our new linked list
            cur.next = ListNode(val)
            cur = cur.next  # Move pointer forward
            
            # Move to the next nodes in l1 and l2 if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # The result starts from dummy.next since dummy was just a placeholder
        return dummy.next