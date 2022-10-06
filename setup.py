import os
from clean_up import clean_up

def setup(config_file):
    for i in range(14):
        dir_name = config_file['fileExtensionNames'][i] 

        path = os.path.join(r'C:\Users\Rushabh\Downloads',  dir_name)

        os.makedirs(path)
            
    clean_up(config_file['fileExtensionNames'])
    