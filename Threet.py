from requests import get
from pandas import read_csv as pd
from pandas import DataFrame




def Threat():
    try:
        url = 'https://reputation.alienvault.com/reputation.data'
        r = get(url, allow_redirects=True)

        open('Threet.csv', 'wb').write(r.content)

        df = pd('Threet.csv',header=None)
    
        df = df[0].str.split('#').str[0]
        df.to_csv('Threet.csv',index=False,header=False)
    except Exception as e:
        print(str(e))
    


  
if __name__ == '__main__':
    Threat()
    

       
   