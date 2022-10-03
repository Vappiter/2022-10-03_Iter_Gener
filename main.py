from traitlets import Instance


nested_list = [
	['a', ['q',True, [33,'dsad'],False],'b', 'c', [3,9,18]],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

def flat_list(lst, res=[]):
  for var1 in lst:
    flat_list(var1) if isinstance(var1, list) else res.append(var1)
  return res


class FlatIterator():
  
  def __init__(self, my_list):
    self.cl_list = my_list
    
  def __iter__(self):
    self.cursor = -1 
    self.one_list = flat_list(self.cl_list)
    self.len_list = len (self.one_list)
    return self

  def __next__(self):
    self.cursor += 1  
    if self.cursor < self.len_list:  
     return self.one_list [self.cursor] 
    else:
        raise StopIteration 
      
def my_generator(lst):
  test_lst = flat_list(lst)
  var1 = 0
  while var1 < len(test_lst):
    yield test_lst[var1]
    var1 += 1
    
if __name__ == '__main__': 
 for item in FlatIterator(nested_list):
   print(item)
 my_flat_list = [item for item in FlatIterator(nested_list)]  
 print (my_flat_list)
test = my_generator(nested_list)
print (test)
for item1 in test:
  print (item1)  