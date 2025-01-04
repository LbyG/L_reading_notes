from typing import List, Optional
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 创建一个最小堆，用于存储每个链表的当前节点
        heap = []
        # 使用dummy节点简化头节点的处理
        dummy = ListNode(0)
        curr = dummy
        
        # 将所有链表的第一个节点加入堆中
        # 由于heap中不能直接比较ListNode，我们存储(val, i, node)元组
        # i用于在val相同时保证稳定性
        for i, head in enumerate(lists):
            if head:
                heappush(heap, (head.val, i, head))
        
        # 不断从堆中取出最小值，并将下一个节点加入堆中
        while heap:
            val, i, node = heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next 