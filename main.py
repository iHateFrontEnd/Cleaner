from clean_up import clean_up
from setup import setup
import json

def main():
    config_file = json.load(open('config.json'))

    if config_file['firstTimeRun'] == True:
        with open('config.json', 'w') as f:
            config_file['firstTimeRun'] = False
            json_obj = json.dumps(config_file)

            f.write(json_obj)
            print('Done')

        setup(config_file['fileExtensionNames'])
    else:
        clean_up(config_file['fileExtensionNames'])


if __name__ == '__main__':
    main()