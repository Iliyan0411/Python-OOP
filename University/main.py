from Group.student import Student
from Group.group import Group


def main():
    st1 = Student('Iliyan', 82111, 6.00)
    st2 = Student('Ivan', 82110, 2.00)
    st3 = Student('Spasimira', 82096, 6.00)
    st4 = Student('Asen', 82022, 4.50)
    st5 = Student('Georgi', 82013, 2.00)
    st6 = Student('Nikol', 82017, 5.25)

    group_1 = Group()
    group_1.add_student(st1)
    group_1.add_student(st2)
    group_1.add_student(st3)
    group_1.add_student(st4)
    group_1.add_student(st5)
    group_1.add_student(st6)

    # print(group_1.average())

    # gst = group_1.good_students()
    gst = group_1.best_students()
    for st in gst:
        st.print_student()

    # group_1.add_student(Student('Stoyan', 81999, 4.40))
    # group_1.remove_student(82096)

    # group_1.print_group()


main()