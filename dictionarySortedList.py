from abstract import DictGameAbstract

class SortedListDict(DictGameAbstract):
  def __init__(self):
    self.__game_sort = []
    
  def getitem(self, key):
    pass

  def additem(self, key, data):
    self.__game_sort[key] = data
    self.mergeSort(self.__game_sort, 0, len(self.__game_sort)-1)

  def popitem(self, key):
    pass

  def length(self):
    pass
    
  def mergeSort(arr, l, r):
    if l < r:
    
      #Same as (l + r)//2, but avoids Overflow for large l and h.
      m = (l + (r - 1))//2
    
      # Sort first and second halves.
      mergeSort(arr, l, m)
      mergeSort(arr, m + 1, r)
      merge(arr, l, m, r)
  
  def merge(arr, l, m, r):
    n1 = m - l + 1   # Calculate size of left subarray
    n2 = r - m       # Calculate size of right subarray
    
    # Create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    
    # Copy data to temp arrays L[] and R[]
    for i in range (0, n1):
      L[i] = arr[l + i]
      
    for j in range (0, n2):
      R[j] = arr[m + 1 + j]
    
    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray.
    j = 0  # Initial index of second subarray.
    k = l  # Initial index of merged subarray.
    while i < n1 and j < n2:
      if L[i] <= R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1
    
    while i < n1:  # L is not empty.
      arr[k] = L[i]
      i += 1
      k += 1
    
    while j < n2:  # R is not empty.
      arr[k] = R[j]
      j += 1
      k += 1