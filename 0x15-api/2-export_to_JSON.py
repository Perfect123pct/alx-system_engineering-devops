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
    completed_tasks = [{'task': task['title'], 'completed': task['completed'], 'username': user_data['username']} for task in todo_data if task['completed']]

    # Display progress information
    print(f"Employee {user_data['name']} is done with tasks ({len(completed_tasks)}/{len(todo_data)}):")
    print(f"\t{user_data['name']}:{len(completed_tasks)}/{len(todo_data)}")

    # Display completed tasks titles
    for task in completed_tasks:
        print(f"\t\t{task['task']}")

    # Export data to JSON
    export_to_json(employee_id, completed_tasks)

def export_to_json(user_id, completed_tasks):
    filename = f"{user_id}.json"

    with open(filename, 'w') as jsonfile:
        json.dump({user_id: completed_tasks}, jsonfile, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for employee ID.")
        sys.exit(1)
