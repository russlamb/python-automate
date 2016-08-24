
import requests
#res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res = requests.get('https://automatetheboringstuff.com/files/errorpage.txt')

try:
    res.raise_for_status()
except Exception as ex:
    print('There was a problem: %s' % (ex))

if res.status_code == requests.codes.ok:
    print(len(res.text))
    print(res.text[:250])
else:
    print("bad status")