import requests
#URL: http://api.sl.se/api2/TravelplannerV3/trip.json?key=<KEY>&originId=9192&destId=1002&searchForArrival=0 
# http://api.sl.se/api2/TravelplannerV3/trip.json?key=8bc841d39f604e29a41b3be9ec21ed1f&originId=9204&destid=9305&passlist=1
def get_tripplan(originId, destId, key):
    loc_url = 'http://api.sl.se/api2/TravelplannerV3/trip.json'
    passlist=1
    loc_params = {
        'key': key,
        'originId': originId,
        'destId': destId,  
        'passlist':passlist,
    }
    resp = requests.get(url = loc_url, params = loc_params)
    if resp:
        data = resp.json()
    trip = data['Trip']
    num = len(trip)
    trip_list = []
    for i in range(0, num):
        trip_list.append(trip[i]['LegList'])
    return trip
    
originId =  9204
destId = 9509
key = '704e7ca1e6e248029c86e38ebc0f12a4'

print(get_tripplan(originId, destId, key))

