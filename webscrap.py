import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime



tickers=input('ticker_list(separate with comma): ')
s_date=input('start_Date(yyyy,mm,dd):')
e_date=input('end_Date(yyyy,mm,dd):')

Date=datetime.datetime.now().strftime('%Y%m%d')




tickers = tickers.split(",")


for ticker in tickers:
    
    def today(ticker):
        
        reference="https://ca.finance.yahoo.com/quote/{}?p={}".format(ticker,ticker)
        page = requests.get(reference)
        soup = BeautifulSoup(page.content,"lxml")
        left = soup.find_all('table')[0] 
        right = soup.find_all('table')[1] 
        Leftdictionary={'date':Date}
        Rightdictionary={'date':Date}
        
        for row in left.find_all('tr'):
        
            columns = row.find_all('td')
            Leftdictionary[columns[0].get_text()]=columns[1].get_text()
        
        
        for row2 in right.find_all('tr'):
        
            columns = row2.find_all('td')
            Rightdictionary[columns[0].get_text()]=columns[1].get_text()
     
        return Leftdictionary, Rightdictionary
    
    
    def data_mgt(ticker,s_date,e_date,today):
    
        from yahoo_historical import Fetcher
        
        data = Fetcher(str(ticker), [int(s_date[0:4]),int(s_date[5:7]),int(s_date[8:10])], [int(e_date[0:4]),int(e_date[5:7]),int(e_date[8:10])])
        
        data=(data.getHistorical())
        
        Left, Right=today(ticker)
        
        Open=Left.get('Open','none')
        High='NA'
        Low='NA'
        Close='NA'
        Adj_Close='NA'
        Volume=Left.get('Volume','none')
        toDate=datetime.datetime.now().strftime('%Y-%m-%d')
        d={'Open':[Open],'High':[High],'Low':[Low],'Close':[Close],'Adj Close':[Adj_Close],'Volume':[Volume]}
        today=pd.DataFrame(data=d,index=[str(toDate)])
      
        data=data.append(today,ignore_index=True)
        
        return data
    
    data=data_mgt(ticker,s_date,e_date,today)
    data.to_csv('/Users/mac/Desktop/finance/archive/{}at{}.csv'.format(ticker,Date))
