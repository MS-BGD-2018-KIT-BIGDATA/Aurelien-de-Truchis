"""high level support for doing this and that."""
# coding: utf8

# In[23]:

import requests
import requests
import pandas as pd
from bs4 import BeautifulSoupfrom bs4
import time


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


def createDic(ListOfString, ListOfInt3x):
    Dic = {}
    for i in range(1, len(ListOfString)):
        Dic[ListOfString[i]] = [ListOfInt3x[3 * i - 3],
                                ListOfInt3x[3 * i - 2], ListOfInt3x[3 * i - 1]]
    return(Dic)


def getListofUsers(url):
    soup = getSoupFromURL(url)
    Users_css = soup.select("th + td")
    Users = [x.get_text().split(" ")[0]for x in Users_css]
    return(Users)


def getMeanStarsUser(user):
    url = 'https://api.github.com/search/repositories?q=user:'
    + user + '&sort=stars'
    content = requests.get(url)
    data = content.json()
    try:
        liste = [data['items'][i]['stargazers_count']
                 for i in range(len(data['items']))]
    except KeyError:
        return 0
    else:
        if len(liste) == 0:
            return 0
        else:
            return(sum(liste) / len(liste))


def getListofMeanStars(ListofUsers):
    ListofMeanStars = []
    Dict = {}
    for i in range(0, int(len(ListOfUsers) / 10)):
        ListofMeanStars = ListofMeanStars + \
            [getMeanStarsUser(x) for x in ListOfUsers[i * 10:(i + 1) * 10]]
        time.sleep(60)
    Dict = dict(zip(ListofUsers, ListofMeanStars))
    return(Dict)


# In[22]:

url = 'https://gist.github.com/paulmillr/2657075'
ListOfUsers = getListofUsers(url)


# In[24]:

getListofMeanStars(ListOfUsers)

# In[128]:

dictionary = dict(zip(getListofUsers(url), ListOfMean))
