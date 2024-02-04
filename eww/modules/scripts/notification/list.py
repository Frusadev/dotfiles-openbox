import json
import os


def write_data() -> str:
    cmd: str = "dunstctl history > history.json"
    os.system(f"cd . && {cmd}")
    content: str = ""
    with open("history.json", "r+") as history:
        y = history.readlines()
        for s in y:
            content = content + s
    return content


"This function will parse the json data, and return the yuck output"


def parse_data() -> str:
    data = {}
    # Load the json data
    with open("history.json", "r+") as history:
        data = json.load(history)
    # Construct the yuck output
    """The yuck output will be presented like this:

        (notif :title "title" :content "Content" :time "time")
    """
    notifications = data["data"][0]
    yuck_output = ""

    for notification in notifications:
        title: str = notification["summary"]["data"]
        content: str = notification["body"]["data"]
        id = notification["id"]["data"]
        app_name = notification["appname"]["data"]
        yuck_output = (
            yuck_output
            + f'(notif :title "{title}" :content "{content}" :id {id} :app_name {app_name} )'
        )
    return yuck_output


print(write_data())
print(parse_data())