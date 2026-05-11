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
