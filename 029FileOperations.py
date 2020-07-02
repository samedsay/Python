# READING A FILE
with open("welcome.txt") as text_file:
  text_data = text_file.read()
print(text_data)

# READING LINES
with open("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)
    
# READING A LINE
with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
print(first_line)

# WRITING A FILE
with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("4Me")
  
# APPENDING TO A FILE
with open("cool_dogs.txt", "a") as cool_dogs_file:
  cool_dogs_file.write("Air Buddy")
  
# READING A CSV FILE
import csv
with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
