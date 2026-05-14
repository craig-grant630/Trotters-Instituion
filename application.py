from data_storage import FileHandler
from classes import Student

class StudyBuddyApp:
    def __init__(self):
        self.store = FileHandler()

        if self.store.required_campus_data_needed():
            # give required data (campuses)
            self.store.set_required_campus_data()
        if self.store.required_programme_data_needed():
            # give required data (programmes)
            self.store.set_required_programme_data()

        self.programmes = self.store.load_programmes()
        self.campuses = self.store.load_campuses()
        self.students = self.store.load_students()
