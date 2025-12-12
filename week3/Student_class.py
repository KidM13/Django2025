class Student:
    def set_grade(self,grade):
        self.__grade=grade
    def get_grade(self):
        return self.__grade
    
student1=Student()
student1.set_grade(90)
print(student1.get_grade())