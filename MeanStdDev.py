import numpy as np

class VirtualBlackAlpaca(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2020, 12, 1)
        self.SetEndDate(2020, 12, 31)
        self.SetCash(100000)
        self.AddEquity("TSLA", Resolution.Daily)
        self.prices = []
        
    def OnData (self, data):
        close_price = (data["TSLA"].Close)
        self.prices.append(close_price)
        
    def OnEndOfAlgorithm(self):
        mean = np.mean(self.prices)
        std_dev = np.std(self.prices)
        
        self.Debug("The mean is : " + str(mean))
        self.Debug("The standard deviation is : " + str(std_dev))
