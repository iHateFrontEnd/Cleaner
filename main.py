from clean_up import clean_up
from setup import setup
import json

def main():
    config_file = json.load(open('config.json'))

    if config_file['firstTimeRun'] == True:
        setup()
    else:
        print(config_file)
        clean_up(config_file['fileExtensionNames'], config_file['downloadsPath'])


if __name__ == '__main__':
    main()