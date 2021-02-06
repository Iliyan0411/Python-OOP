from Group.student import Student

class Group:
    def __init__(self, students, group_id) -> None:
        self.students = students
        self.group_id = group_id

    def average(self):
        avg = 0
        for student in self.students:
            avg += student.grade

        return avg / len(self.students)

    def good_students(self):
        gst = []

        for student in self.students:
            if student.good_student():
                gst.append(student)
        
        return gst

    def print_group(self):
        for student in self.students:
            student.print_student()

    def add_student(self, new_student):
        self.students.append(new_student)

    def remove_student(self, fn):
        updated_students = []

        for student in self.students:
            if student.fn != fn:
                updated_students.append(student)

        self.students = updated_students