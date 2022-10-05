from geopy.geocoders import Nominatim

address = "Charles I, Charing Cross, St. James's, Covent Garden, City of Westminster, Greater London, England, SW1A 2DX, United Kingdom"
cords = ""

def geoCode(address):
    geolocator = Nominatim(user_agent="GrowYourSaplings")
    location = geolocator.geocode(address)
    lat = location.latitude
    lon = location.longitude
    cords_coded = (lat,lon)
    return cords_coded

def revGeoCode(cords):
    geolocator = Nominatim(user_agent="GrowYourSaplings")
    location = geolocator.reverse(cords)
    address_coded = location.address
    return address_coded

cords = (geoCode(address))
print (cords)
address = (revGeoCode(cords))
print (address)


