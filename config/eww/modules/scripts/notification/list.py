import json
import os


def write_data() -> str:
    cmd: str = (
        "dunstctl history > ~/.config/eww/modules/scripts/notification/history.json"
    )
    os.system(f"cd . && {cmd}")
    content: str = ""
    with open(
        "/home/frusadev/.config/eww/modules/scripts/notification/history.json", "r+"
    ) as history:
        y = history.readlines()
        for s in y:
            content = content + s
    return content


"This function will parse the json data, and return the yuck output"


def parse_data() -> str:
    data = {}
    # Load the json data
    with open(
        "/home/frusadev/.config/eww/modules/scripts/notification/history.json", "r+"
    ) as history:
        data = json.load(history)
    # Construct the yuck output
    notifications = data["data"][0]
    yuck_output = ""

    for notification in notifications:
        title: str = notification["summary"]["data"]
        content: str = notification["body"]["data"]
        id = notification["id"]["data"]
        yuck_output = (
            yuck_output
            + f'(notification :id {id} :title "{title}" :content "{content}")\n'
        )
    return (
        """(box
            :orientation "v"
            :space-evenly "false"
            :spacing 10
        """ +
        yuck_output +
        ")"
    )


write_data()
print(parse_data())
