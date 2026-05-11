import os
import json
from classes import Campus, Module, Programme

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
            # Use method from Campus class to change into a dictionary and append to the list for storage
            campus_dict = c.to_dict()
            result.append(campus_dict)
        return self.write_file(FileHandler.CAMPUS_FILE, result)

#=======================================================================================================================
    # Programme Save and write to programme JSON file
    def programme_save(self, programmes):
        result = []
        for p in programmes.values():
            # Use method from programmes class to change into a dictionary
            programmes_dict = p.to_dict()
            result.append(programmes_dict)
        return self.write_file(FileHandler.PROGRAMMES_FILE, result)

#=======================================================================================================================
    # Check if required data and starting data is required methods
    def required_campus_data_needed(self):
        result = False
        if not os.path.exists(self.path(FileHandler.CAMPUS_FILE)) or len(self.read_file(FileHandler.CAMPUS_FILE)) <= 0:
            result = True
        return result

    def required_programme_data_needed(self):
        result = False
        if not os.path.exists(self.path(FileHandler.PROGRAMMES_FILE)) or len(self.read_file(FileHandler.PROGRAMMES_FILE)) <= 0:
            result = True
        return result
#========================================================================================================================
    #Sample Data implemented methods - Required Data (Programmes and Campuses), Testing Data (Students)
    def set_required_campus_data(self):

        campuses = {"PCK": Campus("PCK", "Peckham"),
                    "NYC": Campus("NYC", "New York"),
                    "PAR": Campus("PAR", "Paris")}

        self.save_campuses(campuses)

    def set_required_programme_data(self):

        # campus codes for programmes
        all_campuses = ["PCK", "NYC", "PAR"]
        uk_campuses = ["PCK"]

        # Modules for Programmes
        # bent modules - BA Entrepreneurship
        bent_modules = [Module("BENT11", "Introduction to Entrepreneurship", 1),
                        Module("BENT12", "Planning for Business", 1),
                        Module("BENT13", "Financial Literacy", 1),
                        Module("BENT21", "Market Research", 2),
                        Module("BENT22", "Design Thinking", 2),
                        Module("BAENT23", "Business Models", 2),
                        Module("BENT31", "Entrepreneurship Project", 3)]

        programmes = {
            "BAENT": Programme("BAENT","BA Entrepreneurship", all_campuses, bent_modules)
        }

        self.programme_save(programmes)




