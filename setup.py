import json
import os # syntax: os.system("cmd do something")
import pygetwindow as gw
import time
path_this = os.path.dirname(__file__)

def tabs_setup_machine():
    pass

def displays_setup_machine():
    with open(os.path.join(path_this, "setup.json"), 'r') as json_file:
        data = json.load(json_file)
        display_number = data["meta"][0]["display_number"]

        for i in range(display_number):
            os.system("start "+path_this+f"\movable.bat {i+1}")

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