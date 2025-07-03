import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import PatternFill

resposta = requests.get('https://ufu.br/')
#print(resposta)

if(resposta.status_code == 200):
    soup = BeautifulSoup(resposta.content, 'html.parser')
    #print(soup.prettify())
    #print(soup.title.contents)
    barra_esquerda = soup.find('ul', class_ = 'sidebar-nav nav-level-0')
    #print(barra_esquerda)
    linhas_barra_esquerda = barra_esquerda.find_all('li', class_ = 'nav-item')

    iniciar_captura = False
    linhas_desejadas_barra_esquerda = []
    links_barra_esquerda = []
    for linha in linhas_barra_esquerda:
        if 'Graduação' in linha.text.strip():
            iniciar_captura = True
        
        if iniciar_captura:
            linhas_desejadas_barra_esquerda.append(linha.text.strip())
            links_barra_esquerda.append(linha.a.get('href'))
    print(linhas_desejadas_barra_esquerda)
    print(links_barra_esquerda)
        #print(linha.text)
    
    for link in links_barra_esquerda:
        print("https://ufu.br"+link)