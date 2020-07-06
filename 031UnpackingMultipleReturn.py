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
# join all three of the paths here!
print("/".join(myTuple))

def myjoin(*segments):
  myTuple = []
  for segment in segments:
    myTuple.append(segment)
  joinedString = "/".join(myTuple)
  return joinedString
