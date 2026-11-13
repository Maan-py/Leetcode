"""
Soal    : 206. Reverse Linked List
Tanggal : 2026-11-13
Pola    :
Ide     :
Buntu   :
Waktu   : O()
Memori  : O()
Status  : Belum
"""

from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev


if __name__ == "__main__":
    s = Solution()

    # Ubah list Python biasa jadi linked list: [1, 2, 3] -> 1 -> 2 -> 3
    def buat_linked_list(angka):
        head = None
        for x in reversed(angka):
            head = ListNode(x, head)
        return head

    # Ubah linked list jadi list Python biasa supaya bisa di-print
    def ke_list(head):
        hasil = []
        cur = head
        while cur is not None:
            hasil.append(cur.val)
            cur = cur.next
        return hasil

    print(ke_list(s.reverseList(buat_linked_list([1, 2, 3, 4, 5]))))  # [5, 4, 3, 2, 1]
    print(ke_list(s.reverseList(buat_linked_list([1, 2]))))  # [2, 1]
    print(ke_list(s.reverseList(buat_linked_list([]))))  # []
