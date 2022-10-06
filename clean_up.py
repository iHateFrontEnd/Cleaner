import os

def clean_up(file_extensions):
    path = r"C:\Users\Rushabh\Downloads"

    files = os.listdir(path)

    for i in file_extensions:
        files.remove(i)


    for file in files:
        for extension in file_extensions:
            if(file.endswith(extension)):
                current_location = os.path.join(path, file)
                new_location = os.path.join(path, extension, file)

                os.replace(current_location, new_location)    
                break

    print('Done!')