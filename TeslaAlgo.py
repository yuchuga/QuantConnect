class SGUS(QCAlgorithm):
    
    def Initialize(elf):
        self.SetStartDate(2022, 4, 15)
        self.SetEndDate(2022, 4, 23)
    # update the AddEquity to request Tesla data
    self.tsla = self.AddEquity("TSLA", Resolution.Daily)
    
    def OnData(self, data):
        self.Debug("Number of shares: " + str(self.Portfolio["TSLA"].Invested))