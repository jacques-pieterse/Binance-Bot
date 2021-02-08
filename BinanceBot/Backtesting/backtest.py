import backtrader as bt

cerebro = bt.Cerebro()


data = bt.feeds.GenericCSVData(dataname='1day.csv', dtformat=2)


cerebro.adddata(data)

cerebro.run()

cerebro.plot()