import pandas as pd
import numpy as np
import talib as ta

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
            self.info['fib'] = []
            time_series = pd.to_datetime(origin['time'], unit='s')
            
            self.info['main']['price'] = origin['close']
            self.info['main'].set_index(time_series, inplace=True)

            self.info['main'].sort_index()
            self.fib = None
            
    def SMA(self, window=30):

        simple = ta.SMA(self.info['main']['price'].values, timeperiod=window)
        sma_name = "SMA_{}".format(window)
        self.info['main'][sma_name] = simple
        return self
        
    def RSI(self, window=14):
        try:
            self.rsi_count += 1
        except Exception:
            self.rsi_count = 0
        rsi_simple = ta.RSI(self.info['main']['price'].values, timeperiod=window)
        rsi_name = "RSI_{}".format(window)
        self.info['main'][rsi_name] = rsi_simple
        return self
    
    def EMA(self, window=30):

        ema_simple = ta.RSI(self.info['main']['price'].values, timeperiod=window)
        ema_name = "EMA_{}".format(window)
        self.info['main'][ema_name] = ema_simple
        return self
    
    def TripleEMA(self, window=30):
        # real = TEMA(close, timeperiod=30)
        try:
            self.tema_count += 1
        except Exception:
            self.tema_count = 0
        return self
    
    def BOLL(self, dev=2, window=30):
        upper, middle, lower = ta.BBANDS(self.info['main']['price'].values, timeperiod=window, nbdevup=dev)
        boll_name = "BOLL_{0}_{1}".format(dev, window)
        self.info['main'][boll_name+"_UP"] = upper
        self.info['main'][boll_name+"_MID"] = middle
        self.info['main'][boll_name+"_LOW"] = lower
        return self
    
    def ATR(self, window=40):
        atr = ta.ATR(self.origin['high'].values, self.origin['low'].values, self.origin['close'].values,timeperiod=window)
        atr_name = "ATR_{}".format(window)
        self.info['main'][atr_name] = atr
        return self

    
    def FIBBB(self, stdev=2, window=100):
        # Get EMA
        # Get real = STDDEV(close, timeperiod=5, nbdev=1)
        dev = ta.STDDEV(self.info['main']['price'].values, timeperiod=window, nbdev=stdev)
        basis = ta.EMA(self.info['main']['price'].values, timeperiod=window)
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
        
        fibframe = pd.DataFrame()
        fibframe["price"] = self.info['main']['price']
        fibframe["up1"] = upper_1
        fibframe["up2"] = upper_2
        fibframe["up3"] = upper_3
        fibframe["up4"] = upper_4
        fibframe["up5"] = upper_5
        fibframe["up6"] = upper_6
        fibframe["basis"] = basis
        fibframe["low1"] = lower_1
        fibframe["low2"] = lower_2
        fibframe["low3"] = lower_3
        fibframe["low4"] = lower_4
        fibframe["low5"] = lower_5
        fibframe["low6"] = lower_6
        
        time_series = pd.to_datetime(self.info['main']['time'], unit='s')
        fibframe.set_index(time_series, inplace=True)
        fibframe = fibframe.dropna()
        self.fib = fibframe
        return self
    
    def __getattr__(self, name):
        if name in ('main', 'fib'):
            if name == "main":
                return self.info[name].dropna()
            else:
                return self.fib
    