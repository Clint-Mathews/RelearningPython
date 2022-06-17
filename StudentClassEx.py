class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 -100
    def getGrade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def addStudent(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def averageGrade(self):
        total =0
        for student in self.students:
            total += student.getGrade()
        return total/len(self.students)

s1 = Student("Clint1",24,100)
s2 = Student("Clint2",21,10)
s3 = Student("Clint3",22,80)
s4 = Student("Clint4",25,40)
s5 = Student("Clint5",27,86)
s6 = Student("Clint6",28,91)


course = Course("Science",2)
course.addStudent(s1)
course.addStudent(s2)

print(course.students)
print(course.averageGrade())