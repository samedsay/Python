def get_math_function(operation):   # '+' or '-'
  def add(num1, num2):
    return num1 + num2
  def sub(num1, num2):
    return num1 - num2
  
  if operation == "+":
    return add
  elif operation == "-":
    return sub
 
add_function = get_math_function("+")
sub_function = get_math_function("-")

print( add_function(3, 5) )
print( sub_function(7, 2) )
