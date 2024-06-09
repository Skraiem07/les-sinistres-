import numpy as np
import requests
import xlwt
from bs4 import BeautifulSoup
from lxml import etree, html
import re
import pandas as pd 
import datetime
import warnings

from datetime import datetime
from datetime import timedelta
import winsound
warnings.filterwarnings('ignore')
def web_scraping(code,mois,annee,ville):
    url='https://www.infoclimat.fr/climatologie-mensuelle/'+code+"/"+mois+"/"+annee+"/"+ville+'.html'
    req=requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser',from_encoding="iso-8859-1")
    date =[]
    precip =[]
    l=soup.find_all("a", {"class": "tipsy-trigger-right","target":"_blank"} )
    nombre = len(l)
    s=soup.find_all("td", {"style": "white-space: nowrap"} )
    h=2
   
    
    nombreneige=len(s)
    if(2*nombre>nombreneige):
        h=1
    
    
    
    for j in range(0,nombre):
        string=soup.find_all("a", {"class": "tipsy-trigger-right","target":"_blank"} )[j].text
        m= re.sub("\n| ","",string)
        date.append(m)
        
        string2=soup.find_all("td", {"style": "white-space: nowrap"} )[j*h].find_all("span", {"style": "font-weight:bold;display:inline-block;font-size:16px"} )[0].text
        precip.append(string2)
    dict = {'Date': date, 'Precip': precip}  
    df = pd.DataFrame(dict)

    return df
