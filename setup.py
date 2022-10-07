import os
import json
from clean_up import clean_up

config_file = json.load(open('config.json'))
#creating folders inside the downloads folder
def create_dirs(config_file):
    for i in range(14):
        dir_name = config_file['fileExtensionNames'][i] 

        path = r'C:\Users\Rushabh\Downloads' 

        folder_names = os.path.join(path,  dir_name)

        os.makedirs(folder_names)

    while True:         
        clean_up(config_file['fileExtensionNames'])

#writes the windows config.json
def windows_setup():
    home_dir = os.path.expanduser('~')
    downloads_path = os.path.join(home_dir, 'Downloads')

    with open('config.json', 'w') as f:
        config_file['firstTimeRun'] = False
        config_file['os'] = 'windows'
        config_file['downloadsPath'] = downloads_path

        json_obj = json.dumps(config_file)

        f.write(json_obj)

    clean_up(config_file['fileExtensionNames'], config_file['downloadsPath'])

def linux_setup():
    pass

def setup():
    os_inp = input('If you use window please type: 1, if you use Linux please type: 2: ')

    if os_inp.isnumeric():
        if os_inp == '1':
            windows_setup()
        elif os_inp == '2':
            linux_setup()
        else:
            setup()
    else:
        setup()