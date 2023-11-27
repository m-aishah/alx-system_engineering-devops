#!/usr/bin/python3
'''Exports TODO list info of a given employee to CSV format.'''
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Get username
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Get todo list
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    file_name = str(user_id) + ".csv"

    # Export todo list info to csv
    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for t in todos:
            writer.writerow(
                    [user_id, username, t.get("completed"), t.get("title")]

                    )
