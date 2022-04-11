# Să se scrie un program care gestionează o listă de mașini. O mașină este reprezentată ca dicționar
# și conține următoarele chei:
# id (identificator unic) - se va genera de către program (îl generați programatic)
# brand
# model
# hp (horse power)
# price

import csv
import json
from random import randint

cars = [
    {
        'id': randint(0, 1000),
        'brand': 'MERCEDES',
        'model': 'S',
        'hp': '177',
        'price': 4700
    },
    {
        'id': randint(0, 1000),
        'brand': 'AUDI',
        'model': 'A4',
        'hp': '111',
        'price': 800
    },
    {
        'id': randint(0, 1000),
        'brand': 'BMW',
        'model': 'M8',
        'hp': '575',
        'price': 5500
    },
    {
        'id': randint(0, 1000),
        'brand': 'VW',
        'model': 'GOLF',
        'hp': '99',
        'price': 500
    },
    {
        'id': randint(0, 1000),
        'brand': 'VW',
        'model': 'PASSAT',
        'hp': '140',
        'price': 2000
    },
    {
        'id': randint(0, 1000),
        'brand': 'VW',
        'model': 'ARTEON',
        'hp': '201',
        'price': 5100
    },
]

with open('input.csv','w') as my_files:
    writer = csv.writer(my_files)
    keys = cars[0].keys()
    writer.writerow(keys)
    for car in cars:
        writer.writerow(car.values())

with open('car.json', 'w') as json_file:
    json.dump(cars, json_file, indent=2)