#!/usr/bin/python3
"""
A script that returns information about an
employee's TODO list progress using a REST API.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = int(sys.argv[1])
        base_url = "https://jsonplaceholder.typicode.com"

        user_res = requests.get("{}/users/{}".format(base_url, emp_id))
        todos_res = requests.get("{}/todos".format(base_url),
                                 params={"userId": emp_id})

        user_name = user_res.json().get("name")
        todos = todos_res.json()

        total_tasks = len(todos)
        done_tasks = [t for t in todos if t.get("completed")]
        number_of_done_tasks = len(done_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            user_name, number_of_done_tasks, total_tasks))

        for task in done_tasks:
            print("\t {}".format(task.get("title")))
