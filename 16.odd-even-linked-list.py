"""
May 16, 2020
Odd Even Linked List
"""


def oddEvenList(head):
    if head == None:
        return head
    oddHead = head
    pointer = head.next
    while (pointer != None):
        if pointer.next == None:
            break
        temp = pointer.next  # 5
        temp2 = oddHead.next  # 2
        oddHead.next = temp  # 3 -> 5
        pointer.next = temp.next  # 4 -> NULL
        temp.next = temp2  # 5 -> 2
        pointer = pointer.next  # 4
        oddHead = oddHead.next  # 3
    return head
