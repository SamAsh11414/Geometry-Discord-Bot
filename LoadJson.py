import json, os

def JsonToken():
    with open('Token.json') as f:
        data = json.load(f)
        TOKEN = data['TOKEN']
        Tdata = []
        Tdata.append({"TOKEN": TOKEN})
    return Tdata