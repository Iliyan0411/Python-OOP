from Group.group import Group


class Menu:
    def __init__(self):
        gnum = self.user_input(1,10)

        self.group = Group([], gnum)
        self.choices = {
            1: self.show_group,
            2: self.add_student,
            3: self.remove_student,
            4: self.modify_group,
            5: self.average_grade,
            6: self.passed_students,
            7: self.best_students,
            8: self.quit
        }

    
