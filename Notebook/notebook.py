import datetime

last_id = 0

class Note:
    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation = datetime.date.today()

        global last_id
        self.id = last_id
        last_id += 1

    def match(self, filter):
        return filter in self.memo or filter in self.tags

    def print_note(self):
        print(f'--- {self.tags}')
        print(self.memo, '\n')


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note_id == note.id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if note_id == note.id:
                note.tags = tags
                break

    def search(self, filter):
        result = []

        for note in self.notes:
            if note.match(filter):
                result.append(note)

        return result
