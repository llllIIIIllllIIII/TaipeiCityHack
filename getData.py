import json

def getEventList():
    data = openJson("mock_event_list")
    return data
    
def getEventInfo(eventId):
    eventId = int(eventId)
    
    data = openJson("mock_event_list")
    data = data["event"][eventId-1]
    
    return data

def getRoomInfo(eventId,RoomId):

    data = openJson("mock_room_info")
    
    return data[eventId][int(RoomId)-1]
    
def getRoomList(eventId):
    data = openJson("mock_room_info")
    return data[eventId]

def openJson(fileName : str):
    with open(f'mock_data/{fileName}.json','r',encoding='utf-8') as file :
        data = json.load(file)
    return data

print(getRoomList("01"))