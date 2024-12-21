import json
from datetime import datetime

def save_to_json(file_path, data):
    with open(file_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile)

def get_oldest_city(data):
    current_year = datetime.now().year
    oldest_city = min(data, key=lambda city: current_year - data[city])
    return oldest_city

cities = {
    "Київ": 482,
    "Львів": 1256,
    "Одеса": 1794,
    "Дніпро": 1776,
    "Харків": 1654,
    "Запоріжжя": 952,
    "Чернівці": 1408,
    "Івано-Франківськ": 1662
}

json_file = 'cities.json'
save_to_json(json_file, cities)

oldest_city = get_oldest_city(cities)
print(f"Місто з найбільшим віком: {oldest_city}")
