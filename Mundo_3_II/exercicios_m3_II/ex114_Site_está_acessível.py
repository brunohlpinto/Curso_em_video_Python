import requests


url = 'https://www.google.pt/?hl=pt-PT'

try:
    pagina = requests.get(url)
    print('A página foi acedida com sucesso.')
except requests.exceptions.ConnectionError as erro:
    print('ERRO. O site não está disponível neste momento.')

# solução GG

"""import urllib
import urllib.request


try:
    site = urllib.request.urlopen('https://www.google.pt/?hl=pt-PT')
except:
    print('O site não está acessível neste momento.')
else:
    print('Consegui acessar o site com sucesso')
    print(site.read())"""
