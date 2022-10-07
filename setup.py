import os
from clean_up import clean_up

def setup(config_file):
    for i in range(14):
        dir_name = config_file['fileExtensionNames'][i] 

        path = r'C:\Users\Rushabh\Downloads' 

        folder_names = os.path.join(path,  dir_name)

        os.makedirs(folder_names)

    while True:         
        clean_up(config_file['fileExtensionNames'])
    