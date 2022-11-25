# import json
#
# data = {"Spain": "Madrid"}
#
# with open("Spain.json", "w") as f:
#     json.dump(data, f)
#
# json_string = json.dumps(data)
# print("^", json_string)


#-------------------------------------------------

import json
from random import choice

def gen_person():
    name = ''
    tel = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    while len(name) != 7:
        name += choice(letters)
    while len(tel) != 10:
        tel += choice(nums)

    person = { 'name': name, 'tel': tel  }
    return person

def write_json(person_dict):

    dict_key = " "
    letters = "1234567890"

    while len(dict_key) != 4:  # --------generator of dict keys
        dict_key += choice(letters)
    try:
        data = json.load(open("persons.json"))
        # print("DATA", data)
    except FileNotFoundError:
        data = {}

    data[dict_key] = person_dict
    print("Final_data", data)

    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)

    # json_string = json.dumps(data)
    # print("---", json_string)


for i in range(1):
    write_json(gen_person())











