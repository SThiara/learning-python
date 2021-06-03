    def is_circular_linked_list(self, input_list):
        if input_list.head:
            node_hash = [input_list.head]
            current = input_list.head
            while current.next:
                if current.next in node_hash:
                    return True
                node_hash.append(current.next)
                current = current.next
        return False
    
    # def is_circular_linked_list(self, input_list):
    #   if input_list.head:
    #     cur = input_list.head
    #     while cur.next:
    #       cur = cur.next
    #       if cur.next == input_list.head:
    #         return True
    #     return False
    #   else:
    #     return False