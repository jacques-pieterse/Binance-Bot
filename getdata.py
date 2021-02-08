from binance.client2 import Client
import config
import csv


client = Client(config.API_KEY, config.API_SECRET)

candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2020")

data = open("1day.csv", "w", newline='' )

candlewriter = csv.writer(data, delimiter=',')

processedcandles = []

for data in candles:
    candle = {
        data[0] / 1000,
        data[1],
        data[2],
        data[3],
        data[4],
        data[5],
        data[6]
    }
    processedcandles.append(candle)

for candlestick in processedcandles:
    candlewriter.writerow(candlestick)

