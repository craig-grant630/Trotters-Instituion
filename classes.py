# https://dev.to/dpills/python-secure-password-management-hashing-and-encryption--1246 Encryption of passwords for later

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

# Use class method in order to create new students from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data['student_id'], data['name'], data['programme_code'], data['campus_code'],
                   data['year_of_study'], data['password'])

    def __repr__(self):
        return f"Student ({self.student_id}), {self.name}"

class Campus:
    def __init__(self, campus_code, name):
        self.campus_code = campus_code.upper()
        self.name = name

    def to_dict(self):
        return self.__dict__

    # Use class method in order to create new campus from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data['campus_code'], data['name'])

    def __repr__(self):
        return f"Campus ({self.campus_code}, {self.name})"

class Module:
    def __init__(self, module_code, name, year):
        self.module_code = module_code.upper()
        self.name = name
        self.year = year

    def to_dict(self):
        return self.__dict__

    # Use class method in order to create new module from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data['module_code'], data['name'], data['year'])

    def __repr__(self):
        return f"Module ({self.module_code}, {self.name}, year = {self.year})"