import sys
from Notebook.notebook import Note, Notebook

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                1: self.show_notes,
                2: self.search_notes,
                3: self.add_note,
                4: self.modify_note,
                5: self.quit
                }

    def display_menu(self):
        print("""
        Notebook Menu

        1. Show all notes
        2. Search notes
        3. Add new note
        4. Modify note
        5. Quit
        """)

    def _user_input(self, minNum, maxNum, text):
        choice = -1

        while choice < minNum or choice > maxNum:
            try:
                choice = int(input(text))
            except:
                continue
        
        return choice

    def run(self):
        while True:
            self.display_menu()
            
            choice = self._user_input(1, 5, 'Enter an option: ')
            
            action = self.choices.get(choice)
            action()

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            note.print_note()

    def search_notes(self):
        filter = input('Search for: ')
        notes = self.notebook.search(filter)

        self.show_notes(notes)

    def add_note(self):
        memo = input('Enter a memo: ')
        tags = input('Enter tags: ')

        self.notebook.new_note(memo, tags)

    def modify_note(self):
        id = int(input('Enter an id: '))
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")

        self.notebook.modify_memo(id, memo)
        self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)
