from student import Student


class Course:
    def __init__(self, students):
        self.students = students

    def avg_grade(self):
        result = 0

        for st in self.students:
            result += st.grade

        return result / len(self.students)

    def print_course(self):
        for st in self.students:
            st.print_student()