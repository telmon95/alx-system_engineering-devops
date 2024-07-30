#!/usr/bin/python3
"""Script to retrieve TODO list progress of a given employee from REST API."""
import requests
import sys


def get_employee_info(user_id):
    """Retrieve user information from the API."""
    url = 'https://jsonplaceholder.typicode.com/'
    response = requests.get(url + 'users/{}'.format(user_id))
    if response.status_code != 200:
        print("Error: Failed to retrieve user information.")
        sys.exit(1)
    return response.json()


def get_todo_list(user_id):
    """Retrieve TODO list for the given user ID from the API."""
    url = 'https://jsonplaceholder.typicode.com/'
    response = requests.get(url + 'todos', params={'userId': user_id})
    if response.status_code != 200:
        print("Error: Failed to retrieve TODO list.")
        sys.exit(1)
    return response.json()


def main():
    """Main function to fetch and display employee's TODO list progress."""
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    user_info = get_employee_info(employee_id)
    todo_list = get_todo_list(employee_id)
    completed_tasks = [task for task in todo_list if task['completed']]
    total_tasks = len(todo_list)
    print("Employee {} is done with tasks({}/{}):".format(
        user_info['name'], len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task['title']))


if __name__ == '__main__':
    main()
