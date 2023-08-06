from requests import get
import json

class Activity:
    activity = ""
    accessibility = 0.0
    type = ""
    participants = 0
    price = 0.0
    link = ""
    key = 0

    def __init__(self, activity, accessibility, type, participants, price, link, key):
        self.activity = activity
        self.accessibility = accessibility
        self.type = type
        self.participants = participants
        self.price = price
        self.link = link
        self.key = key
    
    def hasLink(self):
        if(self.link != ""):
            return True
        else:
            return False


def getRandomActivity():
    res = get("http://boredapi.com/api/activity/")
    raw_data = res.content
    data = json.loads(raw_data)
    if("error" in data):
        raise Exception(data["error"])
    if("link" in data):
        link = data["link"]
    else:
        link = ""
    return Activity(
        activity = data["activity"],
        accessibility = data["accessibility"],
        type = data["type"],
        participants = data["participants"],
        price = data["price"],
        link = link,
        key = data["key"]
    )

def getActivityFromKey(key):
    res = get("http://boredapi.com/api/activity?key=" + str(key))
    raw_data = res.content
    data = json.loads(raw_data)
    if("error" in data):
        raise Exception(data["error"])
    if("link" in data):
        link = data["link"]
    else:
        link = ""
    return Activity(
        activity = data["activity"],
        accessibility = data["accessibility"],
        type = data["type"],
        participants = data["participants"],
        price = data["price"],
        link = link,
        key = data["key"]
    )

def getActivityFromType(type):
    res = get("http://boredapi.com/api/activity?type=" + type)
    raw_data = res.content
    data = json.loads(raw_data)
    if("error" in data):
        raise Exception(data["error"])
    if("link" in data):
        link = data["link"]
    else:
        link = ""
    return Activity(
        activity = data["activity"],
        accessibility = data["accessibility"],
        type = data["type"],
        participants = data["participants"],
        price = data["price"],
        link = link,
        key = data["key"]
    )

def getActivityFromParticipants(participants):
    res = get("http://boredapi.com/api/activity?participants=" + str(participants))
    raw_data = res.content
    data = json.loads(raw_data)
    if("error" in data):
        raise Exception(data["error"])
    if("link" in data):
        link = data["link"]
    else:
        link = ""
    return Activity(
        activity = data["activity"],
        accessibility = data["accessibility"],
        type = data["type"],
        participants = data["participants"],
        price = data["price"],
        link = link,
        key = data["key"]
    )

def getActivityFromPrice(price):
    res = get("http://boredapi.com/api/activity?price=" + str(price))
    raw_data = res.content
    data = json.loads(raw_data)
    if("error" in data):
        raise Exception(data["error"])
    if("link" in data):
        link = data["link"]
    else:
        link = ""
    return Activity(
        activity = data["activity"],
        accessibility = data["accessibility"],
        type = data["type"],
        participants = data["participants"],
        price = data["price"],
        link = link,
        key = data["key"]
    )

def getActivityFromPriceRange(min, max):
    res = get("http://boredapi.com/api/activity?minprice="+str(min)+"&maxprice="+str(max))
    raw_data = res.content
    data = json.loads(raw_data)
    if("error" in data):
        raise Exception(data["error"])
    if("link" in data):
        link = data["link"]
    else:
        link = ""
    return Activity(
        activity = data["activity"],
        accessibility = data["accessibility"],
        type = data["type"],
        participants = data["participants"],
        price = data["price"],
        link = link,
        key = data["key"]
    )

def getActivityFromAccessibility(accessibility):
    res = get("http://boredapi.com/api/activity?accessibility=" + str(accessibility))
    raw_data = res.content
    data = json.loads(raw_data)
    if("error" in data):
        raise Exception(data["error"])
    if("link" in data):
        link = data["link"]
    else:
        link = ""
    return Activity(
        activity = data["activity"],
        accessibility = data["accessibility"],
        type = data["type"],
        participants = data["participants"],
        price = data["price"],
        link = link,
        key = data["key"]
    )

def getActivityFromAccessibilityRange(min, max):
    res = get("http://boredapi.com/api/activity?minaccessibility="+str(min)+"&maxaccessibility="+str(max))
    raw_data = res.content
    data = json.loads(raw_data)
    if("error" in data):
        raise Exception(data["error"])
    if("link" in data):
        link = data["link"]
    else:
        link = ""
    return Activity(
        activity = data["activity"],
        accessibility = data["accessibility"],
        type = data["type"],
        participants = data["participants"],
        price = data["price"],
        link = link,
        key = data["key"]
    )