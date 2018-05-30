class Student:
    age = None
    first_name = None
    last_name = None
    klass = None


student1 = Student()
student1.age=27
student1.first_name = 'Omer'
student1.last_name = 'Akram'
student1.klass = 'BCS'


student2 = Student()
student2.age=24
student2.first_name = 'Asim'
student2.last_name = 'Farooq'
student2.klass = 'ADSE'


student3 = Student()
student3.age=25
student3.first_name = 'Bilal'
student3.last_name = 'Khan'
student3.klass = 'LLB'

students = [student1, student2,student3]

for student in students:
    if student.klass != 'BCS':
        print(student.first_name)

