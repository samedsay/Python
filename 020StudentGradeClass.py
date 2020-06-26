class Student:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
  def __repr__(self):
    return "{name} is {year}th grade.".format(name = self.name, year = self.year)
  
  def get_average(self):
    average = 0
    for grade in self.grades:
      average += float(grade.get_score())
    average = float(average / len(self.grades))
    return average
  
  def is_passing(self,average):
    if self.get_average() > 65:
      return "Passing score."
    else:
      return "Failed."

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65
  def __init__(self,score):
    self.score = score
  def get_score(self):
    return self.score
  
grade1 = Grade(50)
grade2 = Grade(60)
grade3 = Grade(80)
grade4 = Grade(75)
pieter.add_grade(grade1)
pieter.add_grade(grade2)
pieter.add_grade(grade3)
pieter.add_grade(grade4)

pieter.attendance["01/01/2020"] = True
pieter.attendance["08/01/2020"] = False
pieter.attendance["15/01/2020"] = True
pieter.attendance["22/01/2020"] = False
pieter.attendance["29/01/2020"] = True
pieter.attendance["06/02/2020"] = True
pieter.attendance["13/02/2020"] = False

print(pieter.get_average())
print("Is Pieter passing the course?")
print(pieter.is_passing(pieter.get_average()))
print(pieter.attendance)

