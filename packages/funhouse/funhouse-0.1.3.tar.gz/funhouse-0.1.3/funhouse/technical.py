import pandas as pd
import numpy as np
import talib as ta


# Idea. Use context to temporarily sort the item

class TA:
    """
        TA is the class that will convert all of the price information into a technical analysis pandas    
    """
    def __init__(self, origin):
        
        if not isinstance(origin, pd.DataFrame):
            raise TypeError("Not a dataframe")
        else:
            col_list = list(origin.columns)
            self.origin = origin
            self.info = {}
            self.info['main'] = pd.DataFrame()
            self.fib = pd.DataFrame()
            # Get a list of columns
            # Figure out which ones are most similar to time
            # Pick one
            # Try to get the datetime using for loop until it has either run out of not failed
            # Place the date-time into a variable
            available = []
            time_names = ['date', 'time', 'datetime', 'timestamp']
            
            time_candidate = False

            for tname in time_names:
                if tname in col_list:
                    time_candidate = True
                    available.append(tname)
            if time_candidate is False:
                raise AttributeError("You lack a variable that is specified to time please include: [date, time, datetime, timestamp]")
            time_series = None

            for avail in available:
                try:
                    time_series = pd.to_datetime(origin[avail], unit='s')
                except:
                    pass
            
            if time_series is None:
                raise AttributeError("None of your time items were formatted correctly")
                # time_series = pd.to_datetime(origin['time'], unit='s')
            
            self.info['main']['price'] = origin['close']
            self.info['main'].set_index(time_series, inplace=True)
            # self.info['main'].sort_index()
            self.fib['price'] = origin['close']
            self.fib.set_index(time_series, inplace=True)
            # self.fib.sort_index()

    def reverse(self, l):
        """

        """
        # print(type(l))
        return list(reversed(l))
            
    def SMA(self, window=30):
        temp = self.info['main'].sort_index()
        simple = ta.SMA(temp['price'].values, timeperiod=window)

        # Reverse before placing in
        
        sma_name = "SMA_{}".format(window)
        self.info['main'][sma_name] = self.reverse(simple)
        return self
        
    def RSI(self, window=14):
        try:
            self.rsi_count += 1
        except Exception:
            self.rsi_count = 0

        temp = self.info['main'].sort_index()
        rsi_simple = ta.RSI(temp['price'].values, timeperiod=window)
        rsi_name = "RSI_{}".format(window)
        self.info['main'][rsi_name] = self.reverse(rsi_simple)
        return self
    
    def EMA(self, window=30):
        temp = self.info['main'].sort_index()
        ema_simple = ta.RSI(temp['price'].values, timeperiod=window)
        ema_name = "EMA_{}".format(window)
        self.info['main'][ema_name] = self.reverse(ema_simple)
        return self
    
    def TripleEMA(self, window=30):
        # real = TEMA(close, timeperiod=30)
        try:
            self.tema_count += 1
        except Exception:
            self.tema_count = 0
        return self
    
    def BOLL(self, dev=2, window=30):
        temp = self.info['main'].sort_index()
        upper, middle, lower = ta.BBANDS(self.info['main']['price'].values, timeperiod=window, nbdevup=dev)
        boll_name = "BOLL_{0}_{1}".format(dev, window)
        self.info['main'][boll_name+"_UP"] = upper
        self.info['main'][boll_name+"_MID"] = middle
        self.info['main'][boll_name+"_LOW"] = lower
        return self
    
    def ATR(self, window=40):
        temp = self.origin.sort_index()
        atr = ta.ATR(temp['high'].values, temp['low'].values, temp['close'].values,timeperiod=window)
        atr_name = "ATR_{}".format(window)
        self.info['main'][atr_name] = atr
        return self

    
    def FIBBB(self, stdev=2, window=100):
        # Get EMA
        # Get real = STDDEV(close, timeperiod=5, nbdev=1)
        temp = self.origin.sort_index()
        # print(temp.index.values)
        dev = ta.STDDEV(temp['close'].values, timeperiod=window, nbdev=stdev)
        basis = ta.EMA(temp['close'].values, timeperiod=window)
        upper_1= basis + (0.236*dev)
        upper_2= basis + (0.382*dev)
        upper_3= basis + (0.5*dev)
        upper_4= basis + (0.618*dev)
        upper_5= basis + (0.764*dev)
        upper_6= basis + (1*dev)
        lower_1= basis - (0.236*dev)
        lower_2= basis - (0.382*dev)
        lower_3= basis - (0.5*dev)
        lower_4= basis - (0.618*dev)
        lower_5= basis - (0.764*dev)
        lower_6= basis - (1*dev)
        
        self.fib["price"] = self.origin['close']
        self.fib["up1"] = self.reverse(upper_1)  
        self.fib["up2"] = self.reverse(upper_2)
        self.fib["up3"] = self.reverse(upper_3)
        self.fib["up4"] = self.reverse(upper_4)
        self.fib["up5"] = self.reverse(upper_5)
        self.fib["up6"] = self.reverse(upper_6)
        self.fib["basis"] = self.reverse(basis)
        self.fib["low1"] = self.reverse(lower_1)
        self.fib["low2"] = self.reverse(lower_2)
        self.fib["low3"] = self.reverse(lower_3)
        self.fib["low4"] = self.reverse(lower_4)
        self.fib["low5"] = self.reverse(lower_5)
        self.fib["low6"] = self.reverse(lower_6)
        
        # time_series = pd.to_datetime(self.origin['time'], unit='s')
        # fibframe.set_index(time_series, inplace=True)
        self.fib = self.fib.dropna()
        # self.fib = fibframe
        return self
    
    def __getattr__(self, name):
        if name in ('main', 'fib'):
            if name == "main":
                return self.info[name].dropna()
            else:
                return self.fib
    