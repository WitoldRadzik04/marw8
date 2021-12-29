import json
import os # syntax: os.system("cmd do something")
import pygetwindow as gw
import time
path_this = os.path.dirname(__file__)
key = "]dkafsjfgpioawehgji=-0]"
def tabs_setup_machine():
    pass

def displays_setup_machine():
    with open(os.path.join(path_this, "setup.json"), 'r') as json_file:
        data = json.load(json_file)
        display_number = data["meta"][0]["display_number"]

        for i in range(display_number):
            os.system(f'start "{key}{i+1}" '+path_this+f'\movable.bat {i+1}')

    input("Move windows 1 - 3 to their correspoding displays' centers, then focus this window and click enter ")
    for i in range(display_number):
        current_movable = gw.getWindowsWithTitle(key+str(i+1))[0] 
        data["displays"][i]["x_coord"] = current_movable.left
        data["displays"][i]["y_coord"] = current_movable.top

    with open(os.path.join(path_this, "setup.json"), 'w') as json_file: 
        json.dump(data, json_file)


def main_thread():
    task = input()
    match task:
        case 'tabs': 
            tabs_setup_machine()
            exit()
        case 'displays':
            displays_setup_machine()
            exit()
        case _:
            print("\nIncorrect statement.\nIf you are having trouble with something, contact Math Princess on Discord\nTo set the tabs up type 'tabs'\nTo set the displays up type 'displays'\n")
            main_thread()

print("Please select a mode\nTo set the tabs up type 'tabs'\nTo set the displays up type 'displays'")
main_thread()