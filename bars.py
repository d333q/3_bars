import json
import math
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as data_json:
        return json.load(data_json)


def get_biggest_bar(data):
    i = 0
    y = 0
    bar_guests = []
    while i < len(data):
        bar_guests.append(data[i]['Cells']['SeatsCount'])
        i = i+1
    max = bar_guests[y]
    while y < len(bar_guests):
        if bar_guests[y] > max:
            max = bar_guests[y]
        y = y + 1
    index_bar = bar_guests.index(max)
    name_bar = data[index_bar]['Cells']['Name']
    return name_bar, max


def get_smallest_bar(data):
    i = 0
    bar_guests = []
    while i < len(data):
        bar_guests.append(data[i]['Cells']['SeatsCount'])
        i = i+1
    y = 0
    min = bar_guests[y]
    while y < len(bar_guests):
        if bar_guests[y] < min:
            min = bar_guests[y]
        y = y + 1
    index_bar = bar_guests.index(min)
    name_bar = data[index_bar]['Cells']['Name']
    return name_bar, min


def get_closest_bar(data, longitude, latitude):
    longitude = math.radians(longitude)
    latitude = math.radians(latitude)
    allcoordinates = []
    earth_radius = 6371
    i = 0
    while i < len(data):
        bars_longitude = math.radians(
            data[i]['Cells']['geoData']['coordinates'][0])
        bars_latitude = math.radians(
            data[i]['Cells']['geoData']['coordinates'][1])
        calculation = math.acos(
            (math.sin(bars_latitude) * math.sin(latitude)) +
            (math.cos(bars_latitude) *
             math.cos(latitude) * math.cos(bars_longitude-longitude)))
        distance = calculation*earth_radius
        allcoordinates.append(distance)
        i = i+1
    index_bar = min(allcoordinates)
    name_bar = data[allcoordinates.index(index_bar)]['Cells']['Name']
    return name_bar, min(allcoordinates)


if __name__ == '__main__':
    data = load_data(input('Введите название файла со списком баров '))
    print('\nСамый большой бар: {0}, количество посетителей {1}'.format(
        get_biggest_bar(data)[0], get_biggest_bar(data)[1]))
    print('Самый маленький бар: {0}, количество посетителей {1}'.format(
        get_smallest_bar(data)[0], get_smallest_bar(data)[1]))
    print('\nЧтобы узнать ближайший бар введите ваши координаты в градусах:')
    longitude = float(input('Долгота: '))
    latitude = float(input('Широта: '))
    print('\nБлижайшее заведение {0} расстояние до него {1:f} км'.format(
        get_closest_bar(data, longitude, latitude)[0],
        get_closest_bar(data, longitude, latitude)[1]))
