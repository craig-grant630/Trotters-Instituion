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

# Register validations
    #=========================================================================================================
    def check_register_credentials(self, student_id, password1, password2, campus_code, programme_code, year, name):
        if student_id in self.students:
            return False, "WARNING: \n Student ID already exists within the system."
        if not (student_id.isdigit() and len(student_id) == 10):
            return False, "WARNING: \n Student ID must be 10 digits"
        if not password1:
            return False, "WARNING: \n Password is empty. Please enter."
        if not password2:
            return False, "WARNING: \n Please confirm password."
        if password1 != password2:
            return False, "WARNING: \n Passwords do not match."
        if not programme_code:
            return False, "WARNING: \n Program Code must be provided."
        if not campus_code:
            return False, "WARNING: \n Campus Code must be provided."
        if not year:
            return False, "WARNING: \n Year of Study must be provided via dropdown."
        if not name:
            return False, "WARNING: Name must be provided."

        for programme in self.programmes.values():
            if programme_code == programme.programme_code:
                if campus_code not in programme.campus_codes:
                    return False, "WARNING: \n Campus is not available for this Programme"
        return True, None

    def add_student(self, student_id, name, password1, campus_code, programme_code, year):

        student = Student(student_id, name, programme_code, campus_code, year, password1)
        self.students[student_id] = student
        self.store.save_students(self.students)