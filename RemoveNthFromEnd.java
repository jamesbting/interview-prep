public class RemoveNthFromEnd {
    /**
     * Definition for singly-linked list. public class ListNode { int val; ListNode
     * next; ListNode() {} ListNode(int val) { this.val = val; } ListNode(int val,
     * ListNode next) { this.val = val; this.next = next; } }
     */
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head.next == null)
            return null;
        ListNode fast = head;
        ListNode slow = head;

        for (int i = 0; fast != null && i < n; i++)
            fast = fast.next;
        if (fast == null)
            return head.next;
        ListNode prev = null;
        while (fast != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next;
        }

        prev.next = slow.next;
        return head;
    }
    /*
     * n=2 1->2->3->4->5 prev: 3->4->5 slow: 4->5 fast:
     * 
     * prev.next = slow.next;
     */
}
