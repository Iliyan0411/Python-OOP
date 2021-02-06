import datetime

last_id = 0

class Note:
    def __init__(self, memo, tags):
        self.memo = memo
        self.tags = tags
        self.creation = datetime.date.today()

        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags

    def print_note(self):
        print(f'{self.id}) {self.tags} \t [{self.creation}]')
        print(self.memo, '\n')


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags):
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note

        return None

    def modify_memo(self, note_id, memo):
        self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        self._find_note(note_id).tags = tags

    def search(self, filter):
        result = []

        for note in self.notes:
            if note.match(filter):
                result.append(note)

        return result