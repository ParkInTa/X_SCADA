import json
from pprint import pprint

data1 = {
        "portal_site":[
        {
            "name": "다음",
            "url": "http://www.daum.net"
        },
        {
            "name": "네이버",
            "url": "http://www.naver.com"
        }
    ],
    "mcu": {
        "core":"BCM2877"
    },
    "smartPhone":"IPhone",
    "memory": {
        "name":"Samsung-LPDDR4"
    }
}

print('\n--------------jso dump---------------\n')
json_str = json.dumps(data1)
print('json data:', json_str)
print('\n----------jso 파싱-------------\n')
data = json.loads(json_str)
pprint(data)

print(data['portal_site'][0]['name'])
print(data['portal_site'][1]['url'])
print(data['mcu']['core'])
print(data['smartPhone'])