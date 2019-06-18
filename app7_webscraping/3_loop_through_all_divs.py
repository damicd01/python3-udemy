#we now iterate through all the items and get the price

import requests
from bs4 import BeautifulSoup

r=requests.get("http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content
soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

#all[0].find_all("h4",{"class":"propPrice"})

#print(str(all[0].find_all("h4",{"class":"propPrice"})).replace('\n','').replace('[<h4 class="propPrice">','').replace('<span class="IconPropertyFavorite16"></span></h4>]','').replace(' ',''))

for item in all:
    print(str(item.find("h4",{"class":"propPrice"})).replace('\n','').replace('<h4 class="propPrice">','').replace(' ','').replace('<spanclass="IconPropertyFavorite16"></span></h4>',''))
