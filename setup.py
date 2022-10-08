import os
import json
from clean_up import clean_up

config_file = json.load(open('config.json'))

def create_config(operating_system):
    home_dir = os.path.expanduser('~')
    downloads_path = os.path.join(home_dir, 'Downloads')

    with open('config.json', 'w') as f:
        config_file['firstTimeRun'] = False

        if operating_system == 'windows':
            config_file['os'] = 'windows'
        elif operating_system == 'linux':
            config_file['os'] = 'linux'
        
        config_file['downloadsPath'] = downloads_path

        json_obj = json.dumps(config_file)

        f.write(json_obj)

    create_dirs()

#creating folders inside the downloads folder
def create_dirs():
    for i in range(14):
        dir_name = config_file['fileExtensionNames'][i] 

        path = config_file['downloadsPath']

        folder_names = os.path.join(path,  dir_name)

        os.makedirs(folder_names)

        clean_up(config_file['fileExtensionNames'], path)

def setup():
    os_inp = input('If you use window please type: 1, if you use Linux please type: 2: ')

    if os_inp.isnumeric():
        if os_inp == '1':
            create_config('windows')
        elif os_inp == '2':
            create_config('linux')
        else:
            setup()
    else:
        setup()