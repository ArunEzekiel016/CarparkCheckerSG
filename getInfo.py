import json
from urllib.request import urlopen

global data_json
data_json = None
def getData(text):
    if(data_json is None):
        URL = "https://api.data.gov.sg/v1/transport/carpark-availability"
        response = urlopen(URL)
        data_json = json.loads(response.read())

    data_json1 = data_json['items']
    data_json2 = data_json1[0]

    data_json3 = data_json2['carpark_data']

    for x in data_json3:
        currentID = x['carpark_number']
        if currentID == text:
            obj = x['carpark_info']
            obj1 = obj[0]
            availableLots = obj1['lots_available']
            totalLots = obj1['total_lots']

    answer = "Out of "+totalLots+" lots, there are "+availableLots+" lots free!!"

    return answer

# answer_str = json.dumps(getData())
# print(answer_str)


















