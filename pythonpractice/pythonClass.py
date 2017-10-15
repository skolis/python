class Student:
  def __init__(self, first, last, marks):
    self.first = first
    self.last = last
    self.marks = marks
    self.email = first + '.' + last + '@school.com'


  def fullname(self):
    return '{} {}'.format(self.first, self.last)

  def percent(self):
    self.marks = int(self.marks * 1.05)


#std_1 = Student('raj', 'sir', 99)
#std_2 = Student('kanth', 'kalyan', 90)



class avg (Student):
  perc_rise = 1.10

  def __init__ (self, first, last, marks, prog_lang):
    super().__init__(first, last, marks)
    self.prog_lang = prog_lang

std_1 = avg('sam', 'sir', 69, 'python')

print (std_1.prog_lang)
print (std_1.marks * avg.perc_rise)

print(std_1.email)
