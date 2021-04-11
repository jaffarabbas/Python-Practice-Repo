class Student:
    #constructer
    def __init__(self,name,age,grade):
       self.name = name
       self.age = age
       self.grade = grade

    def getAverageGrade(self):
        return self.grade
    
    #methods instanceself.


class Course:
    def __init__(self,name,maxStudents):
           self.name = name
           self.maxStudents = maxStudents
           self.Students = []


    def add_Students(self,students):
            if(len(self.Students) < self.maxStudents):
                self.Students.append(students)
                return True
            return False

    def getAverageGrade(self):
        value = 0
        for student in self.Students:
            value += student.getAverageGrade()

        return value / len(self.Students)

class Test:
     def tester(self):
        i = 0
        num = []
        number_of_students = int(input('Number of students : '))
        while(True):
            if(i<=number_of_students):
                name = input('Student Name : ')
                age = int(input('age : '))
                grade = input('Grade : ')
                num.append(Student(name, age, grade))
                i+=1
            else:
                break

        print('do you want to enroll those students in courses y or n')
        course = Course('DSA',number_of_students) 
        print('Couse : DSA','\n Number of students : ',number_of_students)
        
        for i in range(number_of_students):
            print(course.add_Students(number_of_students))
def main():
    test = Test()
    test.tester()
        
if __name__ == '__main__':
    main()
    