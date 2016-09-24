import json
import math


def load_data(filepath):
    data_json = open(filepath)
    data = json.load(data_json)
    return data


def get_biggest_bar(data):
    i = 0
    y = 0
    bar_guests = []
    while i < len(data):
        bar = data[i]['Cells']['SeatsCount']
        bar_guests.append(bar)
        i = i+1
    max = bar_guests[y]
    while y < len(bar_guests):
        if bar_guests[y] > max:
            max = bar_guests[y]
        y = y + 1
    index = bar_guests.index(max)
    name = data[index]['Cells']['Name']
    print ("Самый большой бар: "+name)
    print (max)


def get_smallest_bar(data):
    i = 0
    bar_guests = []
    while i < len(data):
        bar = data[i]['Cells']['SeatsCount']
        bar_guests.append(bar)
        i = i+1
    y = 0
    min = bar_guests[y]
    while y < len(bar_guests):
        if bar_guests[y] < min:
            min = bar_guests[y]
        y = y + 1
    index = bar_guests.index(min)
    name = data[index]['Cells']['Name']
    print ("Самый маленький бар: "+name)
    print (min)


def get_closest_bar(data, longitude, latitude):
    longitude = math.radians(longitude)
    latitude = math.radians(latitude)
    allcoordinates = []
    R = 6371
    i = 0
    while i < len(data):
        bars_longitude = math.radians(
            data[i]['Cells']['geoData']['coordinates'][0])
        bars_latitude = math.radians(
            data[i]['Cells']['geoData']['coordinates'][1])
        d = math.acos(
            (math.sin(bars_latitude) * math.sin(latitude)) +
            (math.cos(bars_latitude) *
             math.cos(latitude) * math.cos(bars_longitude-longitude)))
        distance = d*R
        allcoordinates.append(distance)
        i = i+1
    name = min(allcoordinates)
    name_bars = data[allcoordinates.index(name)]['Cells']['Name']
    print("Ближайшее заведение : " + name_bars)
    print(min(allcoordinates))
if __name__ == '__main__':
    data = load_data('barsjson.json')
    get_biggest_bar(data)
    get_smallest_bar(data)
    a = float(input('Введите долготу '))
    b = float(input('Введите широту '))
    get_closest_bar(data, a, b)