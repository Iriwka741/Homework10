#print("Hello teacher")
#print("Homework №10 Banul")

#Створити ієрархію класів для опису академії.
#Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д

class Person:
 def __init__(self, name, age):
    self.name = name
    self.age = age

class Teacher(Person):
 def __init__(self, name, age, subject):
     super().__init__(name, age)
     self.subject = subject

 def teach(self):
  print(f"{self.name} is teaching {self.subject}.")

class Student(Person):
 def __init__(self, name, age, grade):
     super().__init__(name, age)
     self.grade = grade

 def study(self):
   print(f"{self.name} is studying.")

class Subject:
 def __init__(self, name):
  self.name = name

class Academy:
 def __init__(self, name):
  self.name = name
  self.teachers = []
  self.students = []

 def add_teacher(self, teacher):
  self.teachers.append(teacher)

 def add_student(self, student):
  self.students.append(student)

 def list_teachers(self):
  print("Teachers:")
  for teacher in self.teachers:
    print(f"- {teacher.name}")

 def list_students(self):
  print("Students:")
  for student in self.students:
    print(f"- {student.name}")

#В даному класі Person - це базовий клас, від якого успадковується Teacher і Student.
#Клас Subject - це навчальний предмет, а клас Academy - це академія(навчальний заклад),
#який містить в собі списки викладачів та студентів.




