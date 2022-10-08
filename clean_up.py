from time import *
import os

def clean_up(file_extensions, path):
    while True:
        files = os.listdir(path)

        try:
            for i in file_extensions:
                files.remove(i)
        except ValueError:
            pass

        for file in files:
            sleep(1)
            print('sleep 1') #This statement is only for reference when program in under development

            for extension in file_extensions:
                sleep(0.2)
                print('sleep 2') #This statement is only for reference when program in under development

                if(file.endswith(extension)):
                    current_file_location = os.path.join(path, file)
                    new_file_location = os.path.join(path, extension, file)

                    os.replace(current_file_location, new_file_location)    
                    break

        print("Done!") #This statement is only for reference when program in under development

        sleep(2.5)