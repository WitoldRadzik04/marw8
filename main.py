import json
import os

def array_definition():
    num = meta_arr[0]['windows_num'] # 0 because it always has just one dict
    setup = []
    for i in range(num):
        setup.append([])
    return setup

def opener(tabs_setup_array):
    basic_batch = 'start chrome.exe'
    tab_strings = [basic_batch, basic_batch, basic_batch]
    tab_strings[0]

    return True # i guess this might later cause bugs but let's leave it here for now

with open('setup.json', 'r') as json_file: #don't delete the 'with' idk why but has to be here
    data = json.load(json_file)
    meta_arr = data['meta'] 
    windows_arr = data['windows']
    setup_arr = data['setup']
    
tabs_setup_array = array_definition() #array of arrays of tabs

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

