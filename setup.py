import json
import os # syntax: os.system("cmd do something")
import pygetwindow as gw
import time
path_this = os.path.dirname(__file__)
key = "]dkafsjfgpioawehgji=-0]"

def tabs_setup_machine():
    print("\n")
    with open(os.path.join(path_this, "setup.json"), 'r') as json_file:
        data = json.load(json_file)
        for i in range(data["meta"][0]["display_number"]):
            row_of_links = ""
            for link in data["tabs"][i]:
                row_of_links += link + ", "
            row_of_links = row_of_links[:-2]
            print(f"Display {i+1}: "+row_of_links)

    print("To edit display's tabs, type in the display's number. To exit, type 'exit'.")
    todo = input("")
    if todo in ["1", "2", "3"]:
        pass
    elif todo == "exit":
        exit()
    else:
        print("Please input a display number :)")
        tabs_setup_machine()
    print(f"\nInput a list of tabs you want to be assigned to display number {todo}")
    print("Please follow this syntax:\nlink1, link2, link3")
    print("In words: separate the links with a comma and then a space\nDon't add a comma after the last link")
    new_tabs = input("C'mon, I believe in You!\n")

    try:
        new_tabs_array = new_tabs.split(", ")
    except:
        print("Congratulation, you played yourself\nTry again, but this time... do better.\nI believe in you <3")
        tabs_setup_machine()

    data["tabs"][int(todo)-1] = new_tabs_array

    with open(os.path.join(path_this, "setup.json"), 'w') as json_file: 
        json.dump(data, json_file)
    print("\nChanges saved!\n")


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
    print("\nChanges saved!\n")


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