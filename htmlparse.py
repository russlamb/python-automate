
import requests
import os
import bs4

res = requests.get('http://nostarch.com')

try:
    res.raise_for_status()
except Exception as ex:
    print('There was a problem: %s' % (ex))
    sys.exit()

noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))

exampleHtml = open('example.html','wb')
for chunk in res.iter_content(100000):
    exampleHtml.write(chunk)
exampleHtml.close()

print(os.path.abspath(exampleHtml.name))
