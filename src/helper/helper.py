import json


class Helper:

    def get_config(key):
        # get value by key in config.json file
        conf_file = open("config.json")
        data = json.load(conf_file, )
        conf_file.close()
        return data[key]

    def is_ascending(list_value):
        previous = list_value[0]
        for number in list_value:
            if number < previous:
                return False
            previous = number
        return True
