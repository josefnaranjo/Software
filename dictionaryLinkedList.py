from abstract import DictGameAbstract

class _Node:
  # Initialize node object
  def __init__(self, key = None, data = None):
    self.key = key
    self.data = data
    self.next = None
  
class LinkedListDict(DictGameAbstract):
  
  # Initialize head, data, key
  def __init__(self):
    self.head = _Node()
    #self.__size = 0

  #def __len__(self):
    #return self._size()

    
  # Adding a new node
  def additem(self, key, data):
    #if self.head == None:
      #self.head = _Node(key, data)
      #self.__size +=1
    #else:
      #self._insert(self.head, key, data)
    new_node = _Node(key, data)
    current = self.head
      
    while current.next != None: # Traversing through the list
      current = current.next
    # Once at last element of the list, set next node equal to new node.
    current.next = new_node
   #self.__size +=1

  #def _insert(self, node, key, data):
    #if node.key == key:
      #node.data = data
    #else:
      #new_node = _Node(key, data)
      #current = self.head
      
      #while current.next != None: # Traversing through the list
        #current = current.next
    # Once at last element of the list, set next node equal to new node.
        #current.next = new_node
      
  # Get an element
  def getitem(self, key):
    #node = self._find(self.head, key)
    #if node == None:
      #raise KeyError("Items doesn't exist")
    #return node.data
    current = self.head

    while True:
      current = current.next
      if current.key == key:
        return current.data
      else:
        return None
  #def _find(self, node, key):
    #if node == None:
      #return None
    #if key == node.key:
      #return node
      
  # Delete an element from the list
  def popitem(self, data): 
    #value = self[key]
    #self.head = self._remove(self.head, key)
    #self._size -= 1
    #return value
    current = self.head

    while True:
      last = current
      current = current.next
      if current.data == data:
        last.next = current.next
        return True
        
  #def _remove(self, node, key):
    #assert node is not None, "Cannot remove non-existent key."
    #current = self.head

    #while True:
      #last = current
      #current = current.next
      #if current.key == key:
        #last.next = current.next
        #return
        
  # Total number of elements in the list
  def length(self): 
    current = self.head
    total = 0
    while current.next != None:
      total += 1
      current = current.next
    return total
    
  # Print elements in the list
  def print(self):
    arr = []
    count = 0
    string = ""
    
    current = self.head
    while current.next != None:
      current = current.next
      arr.append(current.data)
    
    for game in arr:
      string += "#" + str(count) + " -> " + str(game) + "\n"
      count += 1
      
    print (string)