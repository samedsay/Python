# Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return the middle element.
# If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(lst):
  lenLst = len(lst)
  if(lenLst % 2 == 1):
    return lst[lenLst//2]
  else:
    average = (lst[lenLst//2] + lst[lenLst//2-1]) // 2
    return average

print(middle_element([5, 2, -10, -4, 4, 5]))
