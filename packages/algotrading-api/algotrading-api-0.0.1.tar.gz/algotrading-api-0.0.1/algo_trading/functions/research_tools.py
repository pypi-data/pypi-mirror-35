
import pandas as pd
from datetime import datetime
    
def get_data_from_av(tk):
    """
    Gets a stock's daily full price history using the Alpha Vantage API.
    
    Parameters
    ----------
    tks : str
        Stock ticker.
    """
    api_key = "P493CCT5PMCKV6HY"
    date_parser = lambda x : datetime.strptime(x, "%Y-%m-%d")
    url = ("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&"
           "symbol="+tk+"&apikey="+api_key+"&outputsize=full&datatype=csv")
    data = pd.read_csv(url, index_col=0, parse_dates=True, date_parser=
                       date_parser)
    data.columns = ["Open", "High", "Low", "Close", "Volume"]
    data.index.name = "Date"
    # flip data so that recent data is at bottom
    return data.iloc[::-1]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    