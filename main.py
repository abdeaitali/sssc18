########################
### MAIN PROGRAM
########################

### IMPORTS
from plan import get_siteid # get station id from name
from plan import get_tripList # get trip ref from pair of station id

from deviation import test_for_deviations

## Abdou's key
KEY_PLANNER = 'b3c091d5ffdf49d2b2bfaea153c905d9'
KEY_LOCATER = 'cf745532e18d426f8f3a40933f2fbc51'

### INPUT
#departure_station = "Tekniska hogskolan"
#arrival_station = "Odenplan"
departure_station = "Tekniska hogskolan"
arrival_station = "Solna Centrum"


### TRIP Planner 4.0
# get id of stations
depId=get_siteid(departure_station,KEY_LOCATER)
arrId=get_siteid(arrival_station,KEY_LOCATER)

# get list of trips
tripList=get_tripList(depId,arrId, KEY_PLANNER)
tripListNoDeviation = list()
tripsNoDeviation = test_for_deviations(tripList)

### RESULTS (as a list of journeys without deviations)
print(tripsNoDeviation)
if len(tripsNoDeviation)==0:
    print("We are sorry, but there are no routes without deviations for you.")
    print("With: "+ tripList[0]['name'])
    print("From: "+ tripList[0]['Origin']['name'])
    print("To: "+ tripList[0]['Destination']['name'])
else:
    print("We found a comfortable trip for you!")
    #for i in tripsNoDeviation:
    """print("With: "+ tripsNoDeviation[0]['name'])
    print("From: "+ tripsNoDeviation[0]['Origin']['name'])
    print("To: "+ tripsNoDeviation[0]['Destination']['name'])"""
    print(len(tripsNoDeviation))
    for i in tripsNoDeviation:    
        print("With: "+ i['Product']['name'])
        print("From: "+ i['Origin']['name'])
        print("To: "+ i['Destination']['name'])
        if i['Origin']['name'] == departure_station:
            break
# output one random tripsNoDeviation