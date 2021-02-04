from notebook import Notebook


def main():
    n = Notebook()

    n.new_note('I love Spasi')
    n.new_note('I ask who are you?')
    n.new_note('Baby birthday')
    n.new_note('Trip in Russia')

    matches = n.search('I')
    for m in matches: m.print_note()



main()