class Student:
    def __init__(self, student_id, name, programme_code, campus_code, year_of_study, password):
        self.student_id = student_id
        self.name = name
        self.programme_code = programme_code.upper()
        self.campus_code = campus_code.upper()
        self.year_of_study = year_of_study
        self.password = password

    def to_dict(self):
        return self.__dict__