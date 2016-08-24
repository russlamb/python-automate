
import requests
import os

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#res = requests.get('https://automatetheboringstuff.com/files/errorpage.txt')

try:
    res.raise_for_status()
except Exception as ex:
    print('There was a problem: %s' % (ex))
    sys.exit()

playFile = open('RomeoAndJuliet.txt','wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
print("file downloaded!")

print(os.path.abspath(playFile.name))
