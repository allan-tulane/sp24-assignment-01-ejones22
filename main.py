"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  
  if x <= 1:  
      return x 
  else:
      ra, rb = foo(x-1), foo(x-2)
      return ra + rb
    

def longest_run(mylist, key):
  length = 0
  count = 0
  for num in mylist:
    if num == key:
      count+=1
      length = max(length, count)
    else:
      count = 0
  return length


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)
        
def longest_run_recursive(mylist, key): 
  
  if not mylist or len(mylist) == 1:
    return mylist[0] == key

  mid = len(mylist) // 2
  left = mylist[:mid]
  right = mylist[mid:]

  left_longest = longest_run_recursive(left, key)
  right_longest = longest_run_recursive(right, key)

  mid_longest = 0
  left_long_count = 0
  right_long_count = 0

  for i in range(mid - 1, -1, -1):
    if mylist[i] == key:
        left_long_count += 1
    else:
        break

  for i in range(mid, len(mylist)):
    if mylist[i] == key:
        right_long_count += 1
    else:
        break

  mid_longest = left_long_count + right_long_count

  return max(left_longest, right_longest, mid_longest)
    



