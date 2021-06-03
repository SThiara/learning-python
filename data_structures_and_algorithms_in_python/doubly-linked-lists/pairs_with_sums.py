  def pairs_with_sum(self, sum_val):  
    cur_node = self.head
    values = []
    sum_pairs = []
    while cur_node:
      values.append(cur_node.data)
      cur_node = cur_node.next
    i = 0
    while i <= len(values) - 1:
      init = values[i]
      i += 1
      for val in values[i:]:
        if init + val == sum_val:
          sum_pairs.append("(" + str(init) + "," + str(val) + ")")
      
    return sum_pairs