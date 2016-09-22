import json
from pprint import pprint

def load_data(filepath):
    with open(filepath) as json_file:
        json_data = json.loads(json_file.read())
        return json_data
        #print(json_data[2]["Cells"]["Name"])
        #data = json_data[2]["Cells"]["Name"]
        #print (data)        

def get_biggest_bar(data):
    name=[]
    guests=[]
    i=0
    while i<515:
        name.append(data[i]["Cells"]["Name"])
        guests.append(data[i]["Cells"]["SeatsCount"])
        i=i+1
        #pprint (name)
    print(guests.index(max(guests)))
        
    #while i<514:
     #   for key, value in data[i]["Cells"]["geoData"].items():
      #      print ('%s: %s' % (key, value))
       #     i=i+1
    
def get_smallest_bar(data):
    pass


def get_closest_bar(data, longitude, latitude):
    pass


if __name__ == '__main__':
    data = load_data('barsjson.json')
    get_biggest_bar(data)