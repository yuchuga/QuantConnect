#MA of TSLA stocks
class Sleepy(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2022, 4, 10)
        self.SetCash(100000)
        self.AddEquity("TSLA", Resolution.Daily)
    
    def OnData(self, data):
        values = self.History(["TSLA"], 30, Resolution.Daily).close
        #self.Debug(values)
        MA21_Pre = values[8:31].mean()
        MA5_pre = values[24:31].mean()
        self.Debug(MA21_Pre)