# Unpacking Multiple Returns
def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper

the_scream, the_whisper = scream_and_whisper("Hello World!")

# Positional Argument Unpacking
from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"
myTuple = [path_segment_1, path_segment_2, path_segment_3]
print("/".join(myTuple))

def myjoin(*segments):
  myTuple = []
  for segment in segments:
    myTuple.append(segment)
  joinedString = "/".join(myTuple)
  return joinedString

# Keyword Argument Unpacking
print("My Youtube channel name is {name} and I'm feeling {feeling}.".format(
name = "samedify", feeling = "happy and determined"))

from products import create_product
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

create_products(
  Baseball = 3, Shirt = 14, Guitar = 70)


