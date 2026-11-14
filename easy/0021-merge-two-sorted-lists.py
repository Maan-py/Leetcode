"""
Soal    : 21. Merge Two Sorted Lists
Tanggal : 2026-11-14
Pola    : Linked List (dummy + tail)
Ide     : Bandingkan depan list1 dan list2, sambung yang lebih kecil ke
          tail, lalu majukan list itu. Kalau salah satu habis, sambung
          sisa yang lain langsung. Hasil = dummy.next.
Buntu   : - Ide ketemu lewat main kartu (ambil yang lebih kecil dari depan).
          - else salah: list1.next = list2.val (harusnya tail.next = list2,
            .val itu angka, bukan node); list2 tidak maju; tail = tail.next
            masuk ke else (harus sejajar if/else).
          - Kode akhir dituliskan Claude. Perlu ditulis ulang sendiri.
Waktu   : O(n + m), tiap node disambung sekali
Memori  : O(1), hanya dummy dan tail
Status  : Selesai (dibantu, perlu review)
"""

from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Node palsu sebagai "pengait" awal barisan baru (nanti dibuang)
        dummy = ListNode()
        # tail = ujung barisan baru, tempat node berikutnya disambung
        tail = dummy

        # Selama A dan B dua-duanya masih ada isinya
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1   # sambung node A ke barisan baru
                list1 = list1.next  # A maju
            else:
                tail.next = list2   # sambung node B ke barisan baru
                list2 = list2.next  # B maju

            # ujung barisan baru pindah ke node yang baru disambung
            tail = tail.next

        # Salah satu sudah habis -> sambung sisa yang lain langsung
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        # Lewati dummy
        return dummy.next


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

    print(ke_list(s.mergeTwoLists(buat_linked_list([1, 2, 4]), buat_linked_list([1, 3, 4]))))  # [1, 1, 2, 3, 4, 4]
    print(ke_list(s.mergeTwoLists(buat_linked_list([]), buat_linked_list([]))))  # []
    print(ke_list(s.mergeTwoLists(buat_linked_list([]), buat_linked_list([0]))))  # [0]
