from student import Student
from course import Course


def main():
    st1 = Student('Iliyan', 82111, 6.00)
    st2 = Student('Ivan', 82096, 4.00)
    st3 = Student('Georgi', 82013, 5.50)
    st4 = Student('Elena', 82001, 3.00)
    st5 = Student('Nikolai', 89191, 5.75)

    students = [st1, st2, st3, st4, st5]

    course = Course(students)
    print(course.avg_grade())
    course.print_course() 

main()