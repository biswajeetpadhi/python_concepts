# Merge two linked list in a sorted manner 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def merge(self, left, right):
        # Base case: If either list is empty, return the other list
        if not left or not right:
            return left or right

        # Create a dummy node and a current pointer to build the merged list
        dummy = curr = ListNode(0)

        # Merge the lists by comparing the values of the nodes
        while left and right:
            # Compare the values of the current nodes in both lists
            if left.val < right.val:
                # If the value in the left list is smaller, append it to the merged list
                curr.next = left
                left = left.next
            else:
                # If the value in the right list is smaller or equal, append it to the merged list
                curr.next = right
                right = right.next
            # Move the current pointer forward in the merged list
            curr = curr.next

            # Print the current value being merged
            print("Merging:", curr.val)

        # Append any remaining nodes from either list
        curr.next = left or right

        # Return the merged list
        return dummy.next

# Create two sorted linked lists: 1 -> 3 -> 5 and 2 -> 4 -> 6
list1 = ListNode(1, ListNode(3, ListNode(5)))
list2 = ListNode(2, ListNode(4, ListNode(6)))

# Print the merged list
current = Solution().merge(list1, list2)
while current:
    print(current.val, end=" -> ")
    current = current.next

