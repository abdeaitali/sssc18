################################
###  Planner module
################################

## used packages
import requests

# get the station id from the name
def get_siteid(searchstring, key):
    loc_url = 'http://api.sl.se/api2/typeahead.json'
    loc_params = {
        'key': key,
        'searchstring': searchstring,
    }
    resp = requests.get(url = loc_url, params = loc_params)
    if resp:
        data = resp.json()
        if data['StatusCode'] == 0:
            return data['ResponseData'][0]['SiteId']
        else:
            raise RuntimeError('Error occured. StatusCode:', data['StatusCode'])

# get the trip leg id from the station pairs id
def get_tripList(originId, destId, key):
    loc_url = 'http://api.sl.se/api2/TravelplannerV3/trip.json'
    loc_params = {
        'key': key,
        'originId': originId,
        'destId': destId,
    }
    resp = requests.get(url = loc_url, params = loc_params)
    if resp:
        data = resp.json()
        if data['Trip']:
            return data['Trip']
        else:
            raise RuntimeError('Error: no trips found')