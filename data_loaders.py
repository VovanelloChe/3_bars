import csv
import json


def load_from_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_handler:
        return json.load(file_handler)

if __name__ == '__main__':
    print(load_from_json('test.json'))
#def load_from_csv(filepath):
#    with open(filepath, 'r') as file_handler:
#        return list(csv.reader(file_handler))
