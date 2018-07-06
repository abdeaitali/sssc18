########################
### MAIN PROGRAM
########################

### IMPORTS
import sys
from plan import get_siteid # get station id from name
from plan import get_tripList # get trip ref from pair of station id

from deviation import test_for_deviations

def main(departure_station, arrival_station):
    ## Abdou's key
    KEY_PLANNER = 'b3c091d5ffdf49d2b2bfaea153c905d9'
    KEY_LOCATER = 'cf745532e18d426f8f3a40933f2fbc51'
    
    ### INPUT
    #departure_station = "Solna Centrum"
    #arrival_station = "Tekniska högskolan"
    #departure_station = sys.argv[1]
    #arrival_station   = sys.argv[2]
    
    ### TRIP Planner 4.0
    # get id of stations
    depId=get_siteid(departure_station,KEY_LOCATER)
    arrId=get_siteid(arrival_station,KEY_LOCATER)
    
    # get list of trips
    tripList=get_tripList(depId,arrId, KEY_PLANNER)
    tripListNoDeviation = list()
    tripsNoDeviation = test_for_deviations(tripList)
    
    ### RESULTS (as a list of journeys without deviations)
    #print(tripsNoDeviation)
    if len(tripsNoDeviation)==0:
        print("We are sorry, but there are no routes without deviations for you.")
        print("This route works, but might be a bit crowded:")
        #print(tripList[0]['LegList']['Leg'])
        for j in tripList[0]['LegList']['Leg']:
            if j['type']=='WALK':
                print('Transfer from '+j['Origin']['name']+' to '+j['Destination']['name'])
            else:    
                print("With: "+ j['Product']['name'])
                print("From: "+ j['Origin']['name'])
                print("To: "+ j['Destination']['name'])
            if j['Destination']['name'].lower() == arrival_station.lower():
                break
            """print("With: "+ j[0]['name'])
            print("From: "+ j[0]['Origin']['name'])
            print("To: "+ j[0]['Destination']['name'])"""
    else:
        print("We found a comfortable trip for you!")
        #for i in tripsNoDeviation:
        """print("With: "+ tripsNoDeviation[0]['name'])
        print("From: "+ tripsNoDeviation[0]['Origin']['name'])
        print("To: "+ tripsNoDeviation[0]['Destination']['name'])"""
        #print(len(tripsNoDeviation))
        for i in tripsNoDeviation[0]:
            if i['type']=='WALK':
                print('Transfer from '+i['Origin']['name']+' to '+i['Destination']['name'])
            else:    
                print("With: "+ i['Product']['name'])
                print("From: "+ i['Origin']['name'])
                print("To: "+ i['Destination']['name'])
            if i['Destination']['name'].lower() == arrival_station.lower():
                break
    # output one random tripsNoDeviation

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

