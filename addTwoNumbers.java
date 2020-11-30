public class addTwoNumbers {
    /**
     * Definition for singly-linked list. public class ListNode { int val; ListNode
     * next; ListNode() {} ListNode(int val) { this.val = val; } ListNode(int val,
     * ListNode next) { this.val = val; this.next = next; } }
     */
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1.val == 0 && l1.next == null)
            return l2;
        if (l2.val == 0 && l1.next == null)
            return l1;

        ListNode dummyHead = new ListNode();
        ListNode curr = dummyHead;
        int carry = 0;
        while (l1 != null && l2 != null) {
            curr.next = new ListNode((l1.val + l2.val + carry) % 10);
            carry = (l1.val + l2.val + carry) / 10;

            l1 = l1.next;
            l2 = l2.next;
            curr = curr.next;
        }

        while (l1 != null) {
            curr.next = new ListNode((l1.val + carry) % 10);
            carry = (l1.val + carry) / 10;
            curr = curr.next;
            l1 = l1.next;
        }

        while (l2 != null) {
            curr.next = new ListNode((l2.val + carry) % 10);
            carry = (l2.val + carry) / 10;
            curr = curr.next;
            l2 = l2.next;
        }

        if (carry != 0)
            curr.next = new ListNode(carry);

        return dummyHead.next;
    }

    /*
     * l1: 2->4->3 l2: 5->6->4 carry:1 dummyhead: () -> 7 -> 0 -> 8 curr: 7 -> 0 ->
     * 8
     * 
     */
}
