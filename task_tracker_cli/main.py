import argparse
from datetime import datetime
from tasks.task import Task

def main():

    tasks_status = ['todo', 'in-progress', 'done']

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    # Update Task
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="Task ID")

    # Delete Task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # Update status of Task
    # Todo Status
    updateTask_todo_parser = subparsers.add_parser("mark-todo", help="Update a task")
    updateTask_todo_parser.add_argument('id', type=int, help='Task ID')
    # Done Status
    updateTask_done_parser = subparsers.add_parser("mark-done", help="Update a task")
    updateTask_done_parser.add_argument('id', type=int, help='Task ID')
    # In-progress Status
    updateTask_inprogress_parser = subparsers.add_parser("mark-in-progress", help="Update a task")
    updateTask_inprogress_parser.add_argument('id', type=int, help='Task ID')

    # List Task
    listTask_parser = subparsers.add_parser("list", help="List all tasks")
    listTask_parser.add_argument('status', choices=tasks_status, default=None, nargs='?', help='Task status')

    arg = parser.parse_args()
    tasks = Task()
    if arg.command == "add":
        tasks.add_task(arg.description)
    elif arg.command == "update":
        tasks.update_task(arg.id, arg.description)
    elif arg.command == "delete":
        tasks.delete_task(arg.id)
    elif arg.command == "mark-done" or arg.command == "mark-in-progress" or arg.command == "mark-todo":
        tasks.update_status(arg.id, arg.command)
    elif arg.command == "list":
        tasks.list_tasks(arg.status)

if __name__ == "__main__":
    main()