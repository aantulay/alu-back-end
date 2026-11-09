#!/usr/bin/python3
"""
Python script to export employee TODO data in CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(base_url + "users/{}".format(emp_id)).json()
    todos = requests.get(base_url + "todos", params={"userId": emp_id}).json()
    username = user.get("username")

    file_name = "{}.csv".format(emp_id)

    with open(file_name, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                emp_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])