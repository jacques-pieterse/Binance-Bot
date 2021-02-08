# Used Languages:
- Python
- HTML
- JS

# Used Libraries
## -Python:
    - python-binance
    - Flask
## -JS
    - lightweight charts from TradingView

# Tasks

## Finished tasks :
- Creating a frontend layout using lightweight charts and html
- Created routes for main page, buy, sell and settings wtih Flask
- Display chart and balance on app main
- Edited and save a new copy of binance.client library as client2 with coin futures included
- Pulls and displays balance on main for coin futures from data endpoint
- Display a settings widget for indicators (only display/No backend) on main
- Display a buy order book with adjustable quantity and symbol dropdown on main
- buy and sell routes combined with binance api and have working backends
- backend pulls all historical 1H data from 1 Jan 2020 until now
- backend logs historical data on /history route
- chart pulls historical data from /history route
- chart pulls new data straight from websocket (1H candlestick data/ BTCUSDT)
- chart updates with new data from websocket
- Style a bit of the HTML content (No css folder yet)

## To do:
- Create a manual way to place and edit indicator on chart
- Create a way to change symbol data that chart displays
- Find a strategy/indicators to place on chart and give signals
- send signal to to bot that will put down 2% of my account balance as quantity for trade
- send order to binance API to execute
- create user data stream to stream events like account balance or order details
- improve the chart over time
- Create css file to style app
- create the same for a USDT futures account
- find solution to run code on cloud 24/7

