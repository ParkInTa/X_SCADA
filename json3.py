import urllib.request
import json
import datetime,pprint
url ='https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1'


with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())
    print(data)
    
print('\n\n-----------json 파싱----------------\n')
name= data['name']
print('도시명: ', name)

dt= data['dt']
print('수신시간: ')
print(datetime.datetime.fromtimestamp(int(dt)).strftime('%y-%m-%d %H:%M:%S'))
print('\n')

main = data['main']
temp = main['temp']
print('온도: ',int(temp) - 273.15)
print('\n')

weather = data['weather']
main = weather[0]
print(main['main'])
print(main['description'])