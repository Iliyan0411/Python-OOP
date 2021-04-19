from Group.student import Student

class Group:
    def __init__(self, students=[], group_id=1):
        self.students: list(Student) = students
        self.group_id = group_id


    def add_student(self, new_student):
        new_pos = 0

        for student in self.students:
            if student.grade < new_student.grade:
                new_pos += 1
            else:
                break
        
        self.students.insert(new_pos, new_student)


    def remove_student(self, fn):
        for i in range(0, len(self.students)):
            if(self.students[i].fn == fn):
                self.students.pop(i)
                break


    def average(self):
        avg = 0
        for student in self.students:
            avg += student.grade

        return avg / len(self.students)


    def good_students(self):
        def good(student):
            return student.grade >= 3

        return filter(good, self.students)


    def print_group(self):
        for student in self.students:
            student.print_student()


    def best_students(self):
        bst = []

        for i in range(len(self.students)-1, -1, -1):
            bst.append(self.students[i])
            
            if i > 0 and self.students[i].grade != self.students[i-1].grade:
                return bst
            
    
