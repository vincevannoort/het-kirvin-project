import requests


def load():
    base_url = "https://opendata.cbs.nl/ODataApi/odata/83451NED/TypedDataSet"
    url = f"{base_url}?$filter=((KenmerkenBaan+eq+%2710000++%27)+or+(KenmerkenBaan+eq+%273000+++%27)+or+(KenmerkenBaan+eq+%274000+++%27))+and+((Perioden+eq+%272023MM01%27)+or+(Perioden+eq+%272023MM02%27)+or+(Perioden+eq+%272023MM03%27))"

    response = requests.get(url)
    data_json = response.json()
    data = data_json["value"]

    return data
