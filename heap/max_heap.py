import math

class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value): #PUSH
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self): #Pop
    if len(self.storage) > 1:
      self.storage[len(self.storage)-1], self.storage[0] = self.storage[0], self.storage[len(self.storage)-1]
      max = self.storage.pop()
      self._sift_down(0)
    elif len(self.storage) == 1:
      max = self.storage.pop()
    else:
      max = False
    return max

  def get_max(self): #AKA PEEK
    if self.storage[0]:
      return self.storage[0]
    else:
      return False

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent =(index - 1)//2
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
      else:
        break

  def _sift_down(self, index):
    left = index * 2 + 1
    right = index * 2 + 2
  
    largest = index

    if len(self.storage) > left and self.storage[largest] < self.storage[left]:
      largest = left
    if len(self.storage) > right and self.storage[largest] < self.storage[right]:
      largest = right
    if largest != index:
      self.storage[index], self.storage[largest] = self.storage[largest], self.storage[index]
      self._sift_down(largest)