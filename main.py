import json
import os # syntax: os.system("cmd do something")
import pygetwindow as gw
import time

with open(os.path.join(os.path.dirname(__file__), "setup.json"), 'r') as json_file:
    data = json.load(json_file)
    display_number = data["meta"][0]["display_number"]
    displays = data["displays"]
    tabs = data["tabs"]

os.system("taskkill /F /IM discord.exe")
for i in range(display_number):
    basic_batch = "start chrome.exe --new-window "
    for shit in tabs[i]:
        basic_batch += shit + " "
    os.system(basic_batch)
    time.sleep(0.5)
    active_window = gw.getActiveWindow()
    active_window.restore()
    active_window.moveTo(displays[i]["x_coord"], displays[i]["y_coord"])
    active_window.maximize()