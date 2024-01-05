import requests
import json
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch TODO list for the employee
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [{'username': user_data['username'], 'task': task['title'], 'completed': task['completed']} for task in todo_data if task['completed']]

    # Display progress information
    print(f"Employee {user_data['name']} is done with tasks ({len(completed_tasks)}/{len(todo_data)}):")
    print(f"\t{user_data['name']}:{len(completed_tasks)}/{len(todo_data)}")

    # Display completed tasks titles
    for task in completed_tasks:
        print(f"\t\t{task['task']}")

    return user_data['id'], completed_tasks

def export_to_json(data):
    filename = "todo_all_employees.json"

    with open(filename, 'a') as jsonfile:
        jsonfile.seek(0)
        content = jsonfile.read()
        if content:
            existing_data = json.loads(content)
        else:
            existing_data = {}

        user_id, tasks = data
        existing_data[user_id] = tasks
        jsonfile.seek(0)
        json.dump(existing_data, jsonfile, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        data = get_employee_todo_progress(employee_id)
        export_to_json(data)
    except ValueError:
        print("Please provide a valid integer for employee ID.")
        sys.exit(1)
