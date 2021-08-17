from math import floor

class Array:
  def __init__(self):
    self.data = {}
    self.length = 0
  
  def append(self, value):
    self.data[self.length] = value
    self.length += 1

  def pop(self):
    del self.data[self.length - 1]
    self.length -= 1

  def unshift(self):
    if self.data[0]:
      del self.data[0]
      self.length -= 1
      self.reindex(1)
  
  def reindex(self, initial):
    for i in range(initial, self.length + 1):
      self.data[i - 1] = self.data[i]
    del self.data[self.length]

  def delete(self, value):
    for i in range(self.length):
      if(self.data[i] == value): 
        del self.data[i]
        self.length -= 1
        self.reindex(i+1)
        return i

  def reverse(self):
    base = self.length - 1
    until = floor(self.length / 2)
    for i in reversed(range(until, self.length)):
      targetKey = base - i
      targetValue = self.data[targetKey]
      currentValue = self.data[i]
      self.data[i] = targetValue
      self.data[targetKey] = currentValue


  def log(self):
    print(self.data, self.length)

array = Array()
array.append('0')
array.append('1')
array.append('2')
array.append('3')
array.append('4')
array.append('5')
array.append('5')
array.reverse()
array.log()

# # reverse
