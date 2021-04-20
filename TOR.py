from requests import get
from pandas import read_csv as pd
from pandas import DataFrame
from re import match
from bs4 import BeautifulSoup
from urllib import urlopen
from os import remove
import ssl



def TOR():
    
    try:
        link = "https://www.dan.me.uk/tornodes"
    
        html = urlopen(link,context=ssl._create_unverified_context()).read()
        soup = BeautifulSoup(html, 'html.parser')
        csv = open("TOR1.csv", "a")
    
        for script in soup(["script", "style"]):
            script.decompose()

        strips = list(soup.stripped_strings)

        for x in range(len(strips)):
            csv.write(strips[x].encode('utf-8')+'\n')

        csv.close()

        df = pd('TOR1.csv',header=None,sep='\t')
        df = df[0].str.split('|').str[0]
        pattern = r'\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b'
        d=[]

        for i in range(len(df)):
            if match(pattern,df[i]):
                d.append(df[i])

        df = DataFrame(d)
        df.to_csv('TOR.csv',header=False,index=False)
        remove('TOR1.csv')
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    TOR()