import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

from phonenumbers import carrier
number = "+919020105891"
key = 'd25e29efb4a148b9996e225b64ae12ba'
ch_number = phonenumbers.parse(number)
your_location=geocoder.description_for_number(ch_number, "en")
print(your_location)
service_provider = phonenumbers.parse(number, "en")
print(carrier.name_for_number(service_provider, "en"))
geocoder = OpenCageGeocode(key)
query = str(your_location)
result = geocoder.geocode(query)
#print(result)


lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print(lat,lng)