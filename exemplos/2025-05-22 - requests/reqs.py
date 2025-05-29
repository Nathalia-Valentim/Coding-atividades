import requests

r = requests.get('https://httpbin.org')
conteudo = r.text

with open('httpbin.html', 'w', encoding='utf-8') as arquivo_html:    
    arquivo_html.write(conteudo)