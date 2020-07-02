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
