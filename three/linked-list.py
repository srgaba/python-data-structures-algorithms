class Node: 
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self, value):
    node = Node(value)
    self.head = node
    self.tail = node
    self.size = 1

  def add(self, value):
    node = Node(value)
    self.tail.next = node
    self.tail = node
    self.size += 1

  def unshift(self):
    self.head = self.head.next
    self.size -= 1

  def delete(self, value):
    if self.head.data == value:
      return self.unshift()
    node = self.head
    while node:
      if node.next:
        if node.next.data == value:
          nextOfNext = node.next.next
          if nextOfNext:
            node.next = nextOfNext
          else:
            node.next = None
            self.tail = node
          self.size -= 1
        return
      else: 
        node = node.next 

  def reverse(self):
    first = self.head
    second = self.head.next
    while first and second: 
      tmp = second.next
      second.next = first
      first = second
      second = tmp
    self.head.next = None
    self.tail = self.head
    self.head = first  

  def print(self):
    node = self.head
    while node:
      print('Data: %s Next: %s ' % (node.data, (node.next.data if node.next else None)))
      node = node.next
    print('Head: %s Tail: %s' % (self.head.data, self.tail.data))

linkedList = LinkedList(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)

linkedList.reverse()

linkedList.print()