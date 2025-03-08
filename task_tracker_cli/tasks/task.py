from tasks.check_json import JsonManager
from datetime import datetime

json = JsonManager()
class Task:
    def __init__(self):
        self.json_data = json.load_json()
        if not isinstance(self.json_data, list):
            self.json_data = []

    def add_task(self, task_description):
        task_id = len(self.json_data)+1
        self.json_data.append({
            'id': task_id,
            'description': task_description,
            'status': 'todo',
            'createdAt': datetime.now().isoformat(),
            'updatedAt': datetime.now().isoformat()
        })
        json.save_json(self.json_data)
        print(f"Task added successfully (ID: {task_id})")

    def delete_task(self, value):
        if not any(task['id'] == value for task in self.json_data):
            raise ValueError(f"Task with id {value} not found")

        self.json_data = [task for task in self.json_data if task['id'] != value]
        json.save_json(self.json_data)
        print(f"Deleted Task {value}")

    def update_task(self, key, value):
        if not any(task['id'] == key for task in self.json_data):
            raise ValueError(f"Task with id {key} not found")

        for item in self.json_data:
            if item['id'] == key:
                item['task'] = value
                json.save_json(self.json_data)
                print(f"Updated Task {value}")
                print(item)
                break

    def update_status(self, key, value):
        if not any(task['id'] == key for task in self.json_data):
            raise ValueError(f"Task with id {key} not found")


        self.json_data = [{**task, 'status': value, 'updatedAt': datetime.now().isoformat()} if task['id'] == key else task for task in self.json_data]
        json.save_json(self.json_data)
        print(f"Updated status of task id {key} to {value}")

    def list_tasks(self, filter):
        if filter is not None:
            self.json_data = [task for task in self.json_data if task['status'] == filter]
        for item in self.json_data:
            print(item)

