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
    print_name_function()
  return wrapper()

def print_my_name():
  print("Mike")
  
def print_joen_name():
  print("Joen")
  
decorated_function = title_decorator(print_my_name)
decorated_function()

# Decorators

def title_decorator(print_name_function):
  def wrapper():
    print("Professor:")
    print_name_function()
  return wrapper
  
@title_decorator
def print_my_name():
  print("Mike")
  
@title_decorator
def print_joen_name():
  print("Joen")
 
print_my_name()
print_joen_name()

  
# Decorators w/ Parameters

def title_decorator(print_name_function):
  def wrapper(*args, **kwargs):
    print("Professor:")
    print_name_function(*args, **kwargs)
  return wrapper
  
@title_decorator
def print_my_name(name, age):
  print(name + " you are " + str(age))
  
print_my_name("Smd", 23)
  
@title_decorator
def print_joen_name(name):
  print(name)
  
print_joen_name("Joen")





