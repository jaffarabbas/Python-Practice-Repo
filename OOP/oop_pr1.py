class Student:
    #constructer
    def __init__(self,name,age,grade):
       self.name = name
       self.age = age
       self.grade = grade

    def getAverageGrade():
        return int(self.grade)
    
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

    def getGrade(self):
        value = 0
        for student in Student:
            value += student.getAverageGrade()

        return value / len(self.Students)

class Test:
     def tester(self):
        i = 1
        num = []
        number_of_students = int(input('Number of students : '))
        while(True):
            if(i<=number_of_students):
                name = input('Student Name : ')
                age = int(input('age : '))
                grade = int(input('Grade : '))
                num.append(Student(name, age, grade))
                i+=1
            else:
                break

        # print('do you want to enroll those students in courses y or n')
        course = Course('DSA',number_of_students) 
        print('Couse : DSA','\n Number of students : ',number_of_students)
        
        for i in range(0,number_of_students):
            if(course.add_Students(number_of_students)):
                print('Student : ',number_of_students,'\nStudent name : ',num[i].name,'\nStudent Age : ',num[i].age,'\nStudent Grade : ',num[i].grade,'\n\n')
        
        #getAverageGrade
        print("Average Grade : ",course.getGrade())
def main():
    test = Test()
    test.tester()
        
if __name__ == '__main__':
    main()
    