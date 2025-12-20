import json

class Task:
    def __init__(self, task_id, title, completed=False):
        self.task_id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.task_id, "title": self.title, "completed": self.completed}

class TodoManager:
    def __init__(self):
        # We use this variable to tell Python which file to look for
        self.filename = "todos.json"
        self.tasks = []
        self.load_from_json()

    def load_from_json(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                # Converting dicts back into Task objects
                self.tasks = [Task(t['id'], t['title'], t['completed']) for t in data]
        except:
            self.tasks = []

    def save_to_json(self):
        with open(self.filename, "w") as file:
            # Converting Task objects into dicts for storage
            data_to_save = [t.to_dict() for t in self.tasks]
            json.dump(data_to_save, file, indent=4)

    def add_task(self, title):
        new_id = self.tasks[-1].task_id + 1 if self.tasks else 1
        self.tasks.append(Task(new_id, title))
        self.save_to_json()

    def update_task(self, task_id, new_title=None, new_status=None):
        for t in self.tasks:
            if t.task_id == task_id:
                if new_title: t.title = new_title
                if new_status is not None: t.completed = new_status
                break
        self.save_to_json()

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        self.save_to_json()