# Hi, here's your problem today. This problem was recently asked by Twitter:

# You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.

# Here's your starting point:

class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
    res = None
    next = None

    while len(lists) > 0:
        mini = -1
        for i, l in enumerate(lists):
            if mini == -1 or l.val < lists[mini].val:
                mini = i
        
        vmin = lists[mini].val
        lists[mini] = lists[mini].next
        if not lists[mini]: del lists[mini]

        if not res: 
            res = Node(vmin)
            next = res
        else:
            next.next = Node(vmin)
            next = next.next

    return res

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print (merge([a, b]))
# 123456