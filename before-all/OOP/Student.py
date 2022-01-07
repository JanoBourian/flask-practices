class Student:
    def __init__(self, name='username', age=0, grades = ()):
        self.name = name
        self.age = age
        self.grades = grades
        self.average = self.average_function()
    
    def average_function(self):
        return sum(self.grades)/len(self.grades)
    
    # def __str__(self):
    #     return f"""
    # name: {self.name}
    # age: {self.age}"""
    
    def __repr__(self):
        return f"<Person({self.name!r}, {self.age})>"

# Practices
student = Student(name="janobourian", age=31, grades=(10, 10, 9, 8, 7))
print(student)
print(student.name)
print(student.age)
print(student.grades)
print(student.average)
print(student)