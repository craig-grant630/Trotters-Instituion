import os
import json

class FileHandler:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        # make data directory for JSON files if not there
        os.makedirs(self.data_dir, exist_ok=True)

    def path(self, filename):
        return os.path.join(self.data_dir, filename)

    def read_file(self, filename):
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



