import os
import sys
import pickle

home:str = "frusadev"

path:str = f"/home/{home}/.config/eww/"

def open_notification(id:int):
    with open(f"{path}/openned.not", "wb") as openned:
        pickle.dump(id, openned)

def get_openned_notification():
    if os.path.exists(f"{path}openned.not"):
        with open(f"{path}openned.not", "rb") as openned:
            print(pickle.load(openned))
    else:
        print("none")

def close_notifications():
    os.remove(path + "openned.not")

def main():
    if sys.argv[1] == "open":
        open_notification(int(sys.argv[2]))

    elif sys.argv[1] == "get":
        get_openned_notification()
    
    elif sys.argv[1] == "ca":
        close_notifications()

main()
