#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com"
        
        # Fetch user details
        user_res = requests.get(f"{base_url}/users/{emp_id}")
        employee_name = user_res.json().get("name")
        
        # Fetch todos for the user
        todos_res = requests.get(f"{base_url}/todos", params={"userId": emp_id})
        todos = todos_res.json()
        
        total_tasks = len(todos)
        done_tasks = [t for t in todos if t.get("completed")]
        number_of_done_tasks = len(done_tasks)
        
        # Display output in the exact format required
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")