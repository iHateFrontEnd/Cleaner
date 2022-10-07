import os
from time import *

def clean_up(file_extensions, path):
    while True:
        files = os.listdir(path)

        for i in file_extensions:
            files.remove(i)

        for file in files:
            sleep(0.3)

            for extension in file_extensions:
                sleep(0.3)

                if(file.endswith(extension)):
                    current_location = os.path.join(path, file)
                    new_location = os.path.join(path, extension, file)

                    os.replace(current_location, new_location)    
                    break

        print("Done!") #This statement is only for reference when program in under development

        sleep(2.5)
        
