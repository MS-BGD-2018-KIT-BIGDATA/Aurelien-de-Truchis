import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import scrapy
import re


def getSoupFromURL(url, method='get', data={}):

    if method == 'get':
        res = requests.get(url)
    elif method == 'post':
        res = requests.post(url, data=data)
    else:
        return None
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup
    else:
        return None


def getListofCarsurlonePage(region, page):
    url = 'https://www.leboncoin.fr/voitures/offres/' + \
        region + '/?o=' + page + '&q=renault%20zoe'
    soup = getSoupFromURL(url)
    return(['https:' + soup.select("main#main section#listingAds  ul  li a")[j]['href']
            for j in range(len(soup.select("main#main section#listingAds  ul  li a")))])


def getListofCarUrl(region):
    ListeofCarurl = []
    for i in range(1, 10):
        if not getListofCarsurlonePage(region, str(i)):
            break
        else:
            ListeofCarurl.extend(getListofCarsurlonePage(region, str(i)))
    return (ListeofCarurl)


ListUrl = getListofCarUrl('ile_de_france')


def getPro(url):
    soup = getSoupFromURL(url)
    if not soup.select('span.ispro'):
        return ('particulier')
    else:
        return('ispro')


def getVersion(url):
    soup = getSoupFromURL(url)
    pattern = re.compile('(?<=Zoe|zoé) [a-zA-Z]{1,6}', re.IGNORECASE)
    if not pattern.findall(soup.select('h1')[0].getText()):
        return ('NA')
    else:
        return(pattern.findall(soup.select('h1')[0].getText())[0].lower())


def getPrice(url):
    soup = getSoupFromURL(url)
    return(soup.select('h2.item_price.clearfix')[0]['content'])


def getKM(url):
    soup = getSoupFromURL(url)
    pattern = re.compile('[0-9 ]{1,6} (?=KM)', re.IGNORECASE)
    return(pattern.findall("-".join(str(soup.select('div h2 span.value')[i]) for i in range(len(soup.select('div h2 span.value')))))[0])


def getphoneNumber(url):
    soup = getSoupFromURL(url)
    pattern = re.compile('(0[1-68]([-. ]?[0-9]{2}){4})', re.IGNORECASE)
    if not pattern.findall(soup.select('div.line.properties_description')[0].getText()):
        return("NaN")
    else:
        return(pattern.findall(soup.select('div.line.properties_description')[0].getText())[0][0])


df = pd.DataFrame({'Price': pd.Series([getPrice(ListUrl[i - 1]) for i in range(1, len(ListUrl))], index=range(len(ListUrl) - 1)),
                   'Kilomètres': pd.Series([getKM(ListUrl[i - 1]).replace(" ", "") for i in range(1, len(ListUrl))], index=range(len(ListUrl) - 1)),
                   'PhoneNumber': pd.Series([getphoneNumber(ListUrl[i - 1]) for i in range(1, len(ListUrl))], index=range(len(ListUrl) - 1)),
                   'Version': pd.Series([getVersion(ListUrl[i - 1]).strip() for i in range(1, len(ListUrl))], index=range(len(ListUrl) - 1))})


def getPriceArgus(kilo, version):
            region = 78150
            url = 'https://www.lacentrale.fr/cote-auto-renault-zoe-' + version + '+charge+rapide-2013.html'
            soup = getSoupFromURL(url,method='post',data = {'km':int(kilo),'zipcode':region,'month':10})
            return(soup.select('span.jsRefinedQuot')[0].getText())
