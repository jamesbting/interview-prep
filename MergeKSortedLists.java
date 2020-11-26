import java.util.*;

public class MergeKSortedLists {

    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();

        for (ListNode curr : lists) {
            while (curr != null) {
                heap.offer(curr.val);
                curr = curr.next;
            }
        }

        ListNode dummyHead = new ListNode(0);
        ListNode curr = dummyHead;
        while (!heap.isEmpty()) {
            int nextVal = heap.poll();
            curr.next = new ListNode(nextVal);
            curr = curr.next;
        }

        return dummyHead.next;
    }
}
