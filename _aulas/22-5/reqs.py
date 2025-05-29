import requests
r = requests.get('https://httpbin.org')

with open('httpbin.html', 'w') as arwuivo_html:
    arwuivo_html.write(r.text)