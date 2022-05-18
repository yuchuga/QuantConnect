# Step 1: Import Libraries
import numpy as np
import pandas as pd

# Step 2: Initialize
class TransdimensionalNadionCoil(QCAlgorithm): #QC database
    def Initialize(self):
        self.SetStartDate(2021, 1, 14)
        self.AddEquity("AAPL", Resolution.Daily)
        self.AddEquity("SPY", Resolution.Daily)

#Step 3: Call Historical Data
    def OnEndOfAlgorithm(self):
        history_spy = self.History(self.Symbol("SPY"), 30, Resolution.Daily) #historical data for 30days
        history_spy = history_spy["close"].tolist() #convert to list
        spy_abs_return = (history_spy[-1]-history_spy[0]) / history_spy[0] #absolute return
        
        history_aapl = self.History(self.Symbol("AAPL"), 30, Resolution.Daily) #Repeat for Tesla
        history_aapl = history_aapl["close"].tolist()
        aapl_abs_return = (history_aapl[-1]-history_aapl[0]) / history_aapl[0]
        
        self.Debug(spy_abs_return) #print statement
        self.Debug(aapl_abs_return)
        
    #Step 4: Create Dataframe
        df = pd.DataFrame()
        df["SPY_Price"] = history_spy
        df["AAPL_Price"] = history_aapl
        
        #Calculate % change & store in dataframe
        df["SPY_returns"] = df["SPY_Price"].pct_change()
        df["AAPL_returns"] = df["AAPL_Price"].pct_change()
        
        self.Debug(df)

    # Step 5: Calculate values for BAS
        # Mean of Daily returns
        spy_daily_ret = df["SPY_returns"].mean()
        aapl_daily_ret = df["AAPL_returns"].mean()

        self.Debug('spy_mean_ret: {}'.format(spy_daily_ret))
        self.Debug('aapl_mean_ret: {}'.format(aapl_daily_ret))

        #Variance
        spy_var = df["SPY_returns"].var()
        aapl_var = df["AAPL_returns"].var()
        
        #CoVariance
        covariance = df["SPY_returns"].cov(df["AAPL_returns"])
        self.Debug('covariance: {}'.format(covariance))
        
        #Correlation
        correlation = df["SPY_returns"].corr(df["AAPL_returns"])
        self.Debug('Correlation: {}'.format(correlation))

        #Std Deviation
        spy_std = df["SPY_returns"].std()
        aapl_std = df["AAPL_returns"].std()
        self.Debug('Std deviation of AAPL: {}'.format(spy_std))

        #AAPL beta
        AAPL_beta = covariance / spy_var
        self.Debug('AAPL beta: {}'.format(AAPL_beta))
        
        #AAPL alpha
        AAPL_alpha = aapl_abs_return - AAPL_beta * spy_abs_return
        self.Debug('AAPL alpha: {}'.format(AAPL_alpha))
        
        #AAPL Sharpe Ratio 
        AAPL_SR = aapl_daily_ret/aapl_std * (252**0.5) #Annualised Mean Returns
        self.Debug('AAPL Sharpe Ratio: {}'.format(AAPL_SR))

