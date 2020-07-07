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

print(add_function(3, 5))
print(sub_function(7, 2))

# Decorating Functions

def title_decorator(print_name_function):
  def wrapper():
    print("Professor:")
    print_name_function
  return wrapper()

def print_my_name():
  print("Mike")
  
def print_joen_name():
  print("Joen")
  
decorated_function = title_decorator(print_my_name)
decorated_function()


