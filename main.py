import json
import os # syntax: os.system("cmd do something")
import pygetwindow as gw
import time

# this function creates an array of n arrays
def array_definition():
    setup = []
    for i in range(windows_number):
        setup.append([])
    return setup



# this function is responsible for opening the windows
def opener(sorted_tabs):
    basic_batch = 'start chrome.exe --new-window'
    tab_strings = [basic_batch, basic_batch, basic_batch]
    for window_num in range(len(sorted_tabs)):
        for i in sorted_tabs[window_num]:
            tab_strings[window_num] += " "
            tab_strings[window_num] += i
    for i in range(windows_number):
        os.system(tab_strings[i])
    return



# open the json and unpack the data
with open('setup.json', 'r') as json_file: # don't delete the 'with' idk why but has to be here
    data = json.load(json_file)
    meta_arr = data['meta'] 
    global windows_number 
    windows_number = meta_arr[0]['windows_num']
    windows_arr = data['windows']
    setup_arr = data['setup']



# this is just here, it collects the array_definition 's return
tabs_setup_array = array_definition() # array of arrays of tabs



# this sorts the setup array into separate arrays in the tabs array

# this is probably stupid and the whole JSON should be reworked but i need to put
# beta in production already
for i in setup_arr:
    match i['window']:
        case 1:
            tabs_setup_array[0].append(i['link'])
        case 2:
            tabs_setup_array[1].append(i['link'])
        case 3:
            tabs_setup_array[2].append(i['link'])
        case _:
            print("Error 01: Tab assigned to non-existent window ("+str(i['window'])+"). \nTab '"+str(i['link'])+"' discarded. \nFor mor info contact your administrator.\n\n")

# opener(tabs_setup_array)
os.system("start chrome.exe --new-window diki.pl")
time.sleep(2)

diki = gw.getWindowsWithTitle("Słownik angielsko-polski, słownik angielski online - Diki - Google Chrome")[0]
diki.move(-1500, 0)
diki.resizeTo(1920, 1200)
diki.maximize()