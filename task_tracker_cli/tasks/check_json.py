from pathlib import Path
import json

file_name = Path('data.json')

class JsonManager:
    # Check json file
    def __init__(self):
        if not file_name.exists():
            file_name.write_text(json.dumps({}))
            print("Json File not Found.\n json file created.")
        self.stored_task = self.load_json()

    def load_json(self):
        with file_name.open('r') as file:
            try:
                return json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                self.stored_task = {}

    def save_json(self, data):
        with file_name.open('w') as file:
            json.dump(data, file, indent=4)

