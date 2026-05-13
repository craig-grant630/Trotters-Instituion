from data_storage import FileHandler

class StudyBuddyApp:
    def __init__(self):
        store = FileHandler()

        if store.required_campus_data_needed():
            # give required data (campuses)
            store.set_required_campus_data()
        if store.required_programme_data_needed():
            # give required data (programmes)
            store.set_required_programme_data()

        self.programmes = store.read_file(store.PROGRAMMES_FILE)
        self.campuses = store.read_file(store.CAMPUS_FILE)
        self.students = store.read_file(store.STUDENTS_FILE)

    def add_student(self):
        pass