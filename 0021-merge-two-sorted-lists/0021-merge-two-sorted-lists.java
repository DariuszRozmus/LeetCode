/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null || list2 == null){
            if (list2 == null && list1 != null){
                return list1;
            } else{
                return list2;
            }
        } else {
            ListNode cur1 = list1;
            ListNode cur2 = list2;
            ListNode head;
            ListNode hcur;
            if (cur1.val < cur2.val){
                head = cur1;
                cur1 = cur1.next;
            } else {
                head = cur2;
                cur2 = cur2.next;
            }
            hcur = head;
            while (cur1 != null && cur2 != null){
                if (cur1.val < cur2.val){
                    hcur.next = cur1;
                    cur1 = cur1.next;
                } else {
                    hcur.next = cur2;
                    cur2 = cur2.next;
                }
                hcur = hcur.next;
                
            }
            if (cur1 == null){
                hcur.next = cur2;
            } else {
                hcur.next = cur1;
            }
            return head;
        }
    }
}