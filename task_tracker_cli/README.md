# TASK TRACKER CLI

Task Tracker CLI allows you to track your tasks directly from the terminal. You can add, delete, update, and list tasks.

## Installation

- Clone this repository to your local machine:

```bash
git@github.com:FilmG/BackendProjects.git
cd task-tracker-cli
```

## Usage

Add a new task

```bash
python main.py add <description>
```

Update Task

```bash
python main.py update <id> <description>
```

Delete Task

```bash
python main.py delete <id>
```

Marking status of task

```bash
python main.py mark-in-progress <id>
python main.py mark-done <id>
python main.py mark-todo <id>
```

List Tasks
```bash
python main.py list
python main.py list <todo, in-progress, done>
```


# This project is from roadmap.sh
https://roadmap.sh/projects/task-tracker
