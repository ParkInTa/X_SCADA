import json
from pprint import pprint

with open('test.json') as dataFile
    data = json.load(dataFile)
pprint(data)

print('\n----------json 파싱--------------\n')
print('걸그룹 %s 정보:' %data['name'], end= '\n\n')
print('멤버: ')
for index, member in enumerate(data['members']):
    if(index >0):
        print(',', end='')
    print(member, end='')
    
print('\n\n[앨범 목록')
for album, title in data['albums'].items():
    print(' ** %s: %s' % (album, title))