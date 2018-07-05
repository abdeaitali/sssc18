def get_stop_list(originId, destid, key):
    import requests
    loc_url = 'http://api.sl.se/api2/TravelplannerV3/trip.json'
    loc_params = {
            'key':key,
            'originId':originId,
            'destid':destid,
            'passlist':1,
    }
    resp = requests.get(url = loc_url, params = loc_params)
    data = resp.json()
    J1 = data['Trip'][0] # (5 joruneies, len is 5)
    JNS = []
    for i in range(0, len(data['Trip'])):
        JI = []
        JN = data['Trip'][i]
        for j in range(0, len(JN['LegList']['Leg'])):
            if 'Stops' not in JN['LegList']['Leg'][j]:
                JI.append(JN['LegList']['Leg'][j]['Origin']['name'])
                JI.append(JN['LegList']['Leg'][j]['Destination']['name'])
            else:
                trans = JN['LegList']['Leg'][j]['Stops']['Stop']
                for k in range(0, len(trans)):
                    stops = trans[k]['name']
                    JI.append(stops)
        JI2 = []
        [JI2.append(x) for x in JI if x not in JI2]
        JII = {str('J' + str(i)):JI2}
        JNS.append(JII)
        
    return(JNS)


key = '8bc841d39f604e29a41b3be9ec21ed1f'
originId = 9204
destid = 9305
print(get_stop_list(originId, destid, key))
