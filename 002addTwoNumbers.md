## 题目描述

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照**逆序**的方式存储的，并且它们的每个节点只能存储**一位**数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

## Solution

### 1.使用带头结点和进位标志位的新链表逐位相加，步骤如下：

- 创建一个带头结点的空链表
- 初始化进位标志符carry为0
- 将p,q初始化为l1和l2的头部
- 遍历链表l1和l2直至它们的尾端：
    - 将x设为结点p的值，若p已经到达l1的末尾，将其值置为0
    - 将y设为结点q的值，若q已经到达l2的末尾，将其值置为0
    - sum = x + y + carry
    - 更新carry = sum//10
    - 创建一个值为(sum%10)的新结点，并将当前结点指向新结点
    - 将当前结点前进到下一个节点
    - 将p和q前进到下一个节点
- 如果carry为1，在当前结点尾部追加一个值为1的新结点
- 返回头结点的下一个结点

```
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        res = head
        carry = 0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            res.next = ListNode(s%10)
            res = res.next
            carry = 0 if s < 10 else 1
            if (l1 != None):
                l1 = l1.next
            if (l2 != None):
                l2 = l2.next
        if (carry == 1):
            res.next = ListNode(1)
        return head.next
```
设链表l1和l2的节点个数分别为M和N，则时间复杂度O(max(M,N)), 附加空间复杂度O(max(M,N)), 运行时间104ms, 内存消耗13.3MB.

### 2.

```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummy;
        int carry = 0;
        while (p != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            
            int s = x + y + carry;
            curr.next = new ListNode(s % 10);
            curr = curr.next;
            carry = s / 10;
            
            if (p!=null) p = p.next;
            if (q!=null) q = q.next;
        }
        if (carry>0) curr.next = new ListNode(carry);
        return dummy.next;
    }
}
```
时间复杂度, 附加空间复杂度, 运行时间, 内存消耗.

### 3.

```
class Solution {

}
```
时间复杂度, 附加空间复杂度, 运行时间, 内存消耗.