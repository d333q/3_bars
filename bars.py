import json
import math
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_content:
        return json.load(json_content)


def get_biggest_bar(data):
    allseatscount = []
    for seatscount in data:
        allseatscount.append(seatscount['Cells']['SeatsCount'])
    namebar = data[allseatscount.index(max(allseatscount))]['Cells']['Name']
    seatscount = max(allseatscount)
    return namebar, seatscount


def get_smallest_bar(data):
    allseatscount = []
    for seatscount in data:
        allseatscount.append(seatscount['Cells']['SeatsCount'])
    namebar = data[allseatscount.index(min(allseatscount))]['Cells']['Name']
    seatscount = min(allseatscount)
    return namebar, seatscount


def get_closest_bar(data, longitude, latitude):
    longitude = math.radians(longitude)
    latitude = math.radians(latitude)
    allcoordinates = []
    earth_radius = 6371
    for coordinates_data in data:
        bars_longitude = math.radians(
            coordinates_data['Cells']['geoData']['coordinates'][0])
        bars_latitude = math.radians(
            coordinates_data['Cells']['geoData']['coordinates'][1])
        calculation = math.acos(
            (math.sin(bars_latitude) * math.sin(latitude)) +
            (math.cos(bars_latitude) *
             math.cos(latitude) * math.cos(bars_longitude-longitude)))
        distance = calculation*earth_radius
        allcoordinates.append(distance)
    namebar = data[allcoordinates.index(min(allcoordinates))]['Cells']['Name']
    seatscount = min(allcoordinates)
    return namebar, seatscount


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
