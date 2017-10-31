# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#import sys
#
#Ticker=sys[1]
#sdate=sys[2]
#edate=sys[3]
ticker=input('ticker_list: ')
s_date=input('Start_Date(yyyy-mm-dd): ')
e_date=input('End_Date(yyyy-mm-dd): ')


if __name__ == "__main__":
    def data_mgt(ticker,s_date,e_date):
     
        import datetime
        from yahoo_finance import Share
        yahoo=Share(str(ticker))
        #print(yahoo.get_price())
        
        #from yahoo_historical import Fetcher
        ##data = Fetcher("AAPL", [2017,10,29], [2017,10,30])#str(ticker), start=str(s_date), end=str(e_date))
        #data = Fetcher(str(ticker), [str(s_date)], [str(e_date)])
        
        #data=(data.getHistorical())
        
        #
        from pandas_datareader import data as pdr
        
        import fix_yahoo_finance as yf
        yf.pdr_override() 
        
        data = pdr.get_data_yahoo(str(ticker), start=str(s_date), end=str(e_date))
        
        import pandas as pd
        Date=datetime.datetime.today().strftime('%Y-%m-%d')
        Open='NA'
        High='NA'
        Low='NA'
        Close=yahoo.get_price()
        Adj_Close='NA'
        Volume=yahoo.get_volume()
        d={'Open':[Open],'High':[High],'Low':[Low],'Close':[Close],'Adj Close':[Adj_Close],'Volume':[Volume]}
        today=pd.DataFrame(data=d,index=[str(Date)])
      
        data=data.append(today)
