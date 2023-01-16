import json
from urllib.request import urlopen


def getData():
    URL = "https://api.data.gov.sg/v1/transport/carpark-availability"
    response = urlopen(URL)

    lotnumber = input("Please enter the carpark lot ID: ")
    data_json = json.loads(response.read())


    data_json1 = data_json['items']
    data_json2 = data_json1[0]

    data_json3 = data_json2['carpark_data']

    for x in data_json3:
        currentID = x['carpark_number']
        if currentID == lotnumber:
            obj = x['carpark_info']
            obj1 = obj[0]
            availableLots = obj1['lots_available']
            totalLots = obj1['total_lots']

    answer = "Out of "+totalLots+" lots, there are "+availableLots+" lots free!!"

    return answer

















