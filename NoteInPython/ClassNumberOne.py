from datetime import datetime as dt
class Note:
    id=0
    def __init__(self):
        Note.id=Note.id+1
        self._header=""
        self._note_body=""
        self._create_date_time=dt.now();

    def get_ID(self):
        return Note.id

    def set_header(self, header):
        self._header=header

    def get_header(self):
        return self._header

    def set_note_body(self, note_body):
        self._note_body=note_body

    def get_note_body(self):
        return self._note_body

    def set_date_time(self, date_time):
        self._create_date_time = date_time

    def get_date_time(self):
        return self._create_date_time

    def display_info(self):
       return f"Id:{Note.id}, Header:{self._header}, Note Body:{self._note_body}, Date Time:{self._create_date_time}"







