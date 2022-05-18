class VentralTachyonGearbox(QCAlgorithm):
    
    def Initialize(self):
        self.SetStartDate(2018, 1, 1) # Set Start Date
        self.SetCash(100000) # Set Strategy Cash
        self.AddForex("EURUSD", Resolution.Daily, Market.Oanda)
        self.rsi = self.RSI("EURUSD", 14)
        self.macd = self.MACD("EURUSD", 12, 26,9 , MovingAverageType.Exponential, Resolution.Daily)
        
        self.back_1 = None
        self.back_2 = None 
        self.current = None
        
        self.entry_price = None
        
    def OnData(self, data):
        '''OnData event is the primary entry point for your alforithm.
        Each new data point will be pumped in here.
        Arguments:
             data: Slice object keyed by symbol containing the stock data 
        '''
        
        self.back_2 = self.back_1
        self.back_1 = self.current
        self.current = data["EURUSD"].Close
        
        if self.rsi.IsReady:
            self.Debug("RSI Ready")
        
        if self.back_2 == None or self.back_1 == None or self.current == None: return
    
        # trading conditions if not invested in EURUSD
        if self.back_1 > self.back_2 and self.current > self.back_1 
        and self.rsi.Current.Value < 70 and (self.macd.Current.Value > self.macd.Signal.Current.Value):
            if not self.Securities["EURUSD"].Invested:
                self.SetHoldings("EURUSD", 0.1) # invest 10% of our capital
                self.entry_price = self.current
                
        # exit conditions if we are invested in EURUSD
        if self.Securities["EURUSD"].Invested:
            if self.current <= self.entry_price - 0.0005:
                self.liquidate("EURUSD", "stop-loss")
            elif self.current >= self.entry_price + 0.0010:
                self.liquidate("EURUSD", "take-profit")