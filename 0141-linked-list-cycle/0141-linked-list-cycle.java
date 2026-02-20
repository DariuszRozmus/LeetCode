/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null){
            return false;
        }
        List<ListNode> list = new ArrayList();
        list.add(head);
        ListNode cur = head.next;
        int cnt = 0;

        while(cur != null){
            for (ListNode node : list){
                if(node.equals(cur)){
                    return true;
                }
            }
            list.add(cur);
            cur = cur.next;
        }
        return false;
    }
}