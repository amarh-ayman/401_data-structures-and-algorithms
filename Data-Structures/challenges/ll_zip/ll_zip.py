
def zipping(list1, list2):
        item1 = list1.head
        item2 = list2.head
    
        if not item1:
            list1.head = list2.head
            return list1.head
        if not item2:
            list2.head = list1.head
            return list1.head
        
        pointer = item2.next
    
        while item1.next and item2.next:
            item2.next = item1.next
            item1.next= item2
            item1 = item2.next
            item2 = pointer
            pointer = pointer.next
    
        if not item1.next:
            item1.next = item2
            return list1.head

        if not item2.next:
            item2.next = item1.next
            item1.next = item2
            return list1.head


