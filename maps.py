from geopy.geocoders import Nominatim

def locate(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    #print(location.address)
    #Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
    #print((location.latitude, location.longitude))
    return((location.latitude, location.longitude))
#(40.7410861, -73.9896297241625)
