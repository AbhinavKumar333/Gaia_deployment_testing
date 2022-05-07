import xmltodict, json


def convertToJson(xml):
    try:
        o = xmltodict.parse(xml)
        return json.dumps(o)
    except Exception as e:
        return {'exception':e}
