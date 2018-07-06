import requests

def get_deviations(key ,transportmode, linenumber, siteid):
    if transportmode=='BUS':
        transportcode='bus'
    elif transportmode=='MET':
        transportcode='metro'
    elif transportmode=='TRN':
        transportcode='train'
    elif transportmode=='SHP':
        transportcode='ship'
    elif transportmode=='TRM':
        transportcode='tram'
    else:
        transportcode=''
    transportcode=''
    loc_url = 'http://api.sl.se/api2/deviations.json'
    loc_params = {
        'key': key,
        'transportmode': transportcode,
        'linenumber': linenumber,
        'siteid': siteid,
    }
    resp = requests.get(url = loc_url, params = loc_params)
    if resp:
        data = resp.json()
        if data['StatusCode'] == 0:
            return data['ResponseData']
        else:
            raise RuntimeError('Error occured. StatusCode:', data['StatusCode'])

def find_deviations (transportmode, linenumber, siteid):
    data=get_deviations('d12038ad5e5842129dc374e796fe0b08',transportmode,linenumber,siteid)
    #return data
    array=[]
    
    for i in data:
        if 'arbete' in i['Details']:
            array.append(i)
   # return array
            return True
            
            #print('nothing')

#print(find_deviations('','1',''))
def get_stopid(searchstring):
    loc_url = 'http://api.sl.se/api2/typeahead.json'
    loc_params = {
        'key': '7408afe257884be1b392fdfe1e1055c3',
        'searchstring': searchstring,
    }
    resp = requests.get(url = loc_url, params = loc_params)
    if resp:
        data = resp.json()
        if data['StatusCode'] == 0:
            return data['ResponseData'][0]['SiteId']
        else:
            raise RuntimeError('Error occured. StatusCode:', data['StatusCode'])

def test_for_deviations (journeys):
    deviationfree_journeys=[]
    for tripId in journeys:
        for legList in [tripId['LegList']['Leg']]:
            legListErrors=0
            for leg in legList:
                if 'category' not in leg:
                   transportmode = "WALK"
                else:  
                    transportmode = leg['category']
                if transportmode == "WALK":
                    continue
                s = leg['name'].replace('X', '').split(' ')
                linenumber = s[2]
                siteid = get_stopid(leg['Origin']['name'])
                if find_deviations (transportmode, linenumber, siteid):
                    print("Deviation found")
                    legListErrors=legListErrors+1
                """else:
                    deviationfree_journeys.append(leg)"""
                    #print("No deviation found")
            if legListErrors<1:
                deviationfree_journeys.append(legList)
            else:
                print("Journey had too many deviations")
    return deviationfree_journeys