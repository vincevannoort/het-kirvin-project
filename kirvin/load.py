import json
from urllib import request


def load():
    base_url = "https://opendata.cbs.nl/ODataApi/odata/83451NED/UntypedDataSet"
    url = f"{base_url}?$filter=((KenmerkenBaan+eq+%2710000++%27)+or+(KenmerkenBaan+eq+%27100460+%27))+and+((BedrijfstakkenBranchesSBI2008+eq+%27T001081%27)+or+(BedrijfstakkenBranchesSBI2008+eq+%27389100+%27)+or+(BedrijfstakkenBranchesSBI2008+eq+%27422400+%27))+and+((Perioden+eq+%272023MM01%27)+or+(Perioden+eq+%272023MM02%27)+or+(Perioden+eq+%272023MM03%27))"

    with request.urlopen(url) as file:
        data_json = json.load(file)

    data = data_json["value"]

    return data
