import os
import json
from classes import Campus

class FileHandler:

    CAMPUS_FILE = 'campuses.json'
    STUDENTS_FILE = 'students.json'
    PROGRAMMES_FILE = 'programmes.json'
#=======================================================================================================================
    # Initialise paths and set read and write methods
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        # make data directory for JSON files if not there else do nothing
        os.makedirs(self.data_dir, exist_ok=True)

    def path(self, filename):
        # create the path to the JSON files
        return os.path.join(self.data_dir, filename)

    def read_file(self, filename):
        # Read the JSON files and return
        filepath = self.path(filename)
        if not os.path.exists(filepath):
            return []
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except ValueError:
            return []

    def write_file(self, filename, data):
        filepath = self.path(filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

#=======================================================================================================================
    # Campuses save
    def save_campuses(self, campuses):
        result = []
        for c in campuses.values():
            # Use method from Campus class to change into a dictionary
            campus_dict = c.to_dict()
            result.append(campus_dict)
        return self.write_file(FileHandler.CAMPUS_FILE, result)

#=======================================================================================================================

    def required_campus_data_needed(self):
        result = False
        if not os.path.exists(self.path(FileHandler.CAMPUS_FILE)) or len(self.read_file(FileHandler.CAMPUS_FILE)) <= 0:
            result = True
        return result

    def set_required_campus_data(self):

        campuses = {"PCK": Campus("PCK", "Peckham"),
                    "NYC": Campus("NYC", "New York"),
                    "PAR": Campus("PAR", "Paris")}

        self.save_campuses(campuses)
        pass




