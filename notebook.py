"""Module for creating notes and notebooks"""
import datetime

last_id = 0 #The next available id for all new notes

class Note:
    """Represent a single not in the notebook."""
    def __init__(self, memo, tags=''):
        """Initialize a new note with memo and optional tags.
        Automatically set the note id and creation date."""
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Check if the note matches the filter text.
        Return True if there is a match and False otherwise."""
        return filter in self.memo or filter in self.tags


class Notebook:
    """Represent a collection of notes."""
    def __init__(self) -> None:
        """Initialize a notebook with an empty list of notes."""
        self.notes = []
    
    def new_note(self, memo, tags=''):
        """Create a new note and add it to the list."""
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        """Find the note with given id."""
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
    
    def modify_memo(self, note_id, memo):
        """Find the note with the given id and change its memo to the given value."""
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        """Find the note with the given id and change its tags to the given value."""
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter):
        """Find all notes that match the filter text."""
        return [note for note in self.notes if note.match(filter)]
