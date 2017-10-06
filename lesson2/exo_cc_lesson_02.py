
# coding: utf-8

# In[21]:

import requests
from bs4 import BeautifulSoup

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

def getDiscountBrand (Brand):
    soup = getSoupFromURL('https://www.cdiscount.com/search/10/'+ Brand +'.html#_his_')
    Discount = soup.find_all(class_ = "ecoBlk")
    ListeMontantsDiscount = list(map(lambda x: int(x.get_text().split(" ")[1].replace(u'€', u'').replace(u' ', u'')), Discount ))
    return(sum(ListeMontantsDiscount))

getDiscountBrand('Acer')

