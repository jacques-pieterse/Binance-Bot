from types import MethodType
from flask_cors import CORS
from flask import Flask, render_template, request, flash, redirect, jsonify, make_response
import config, csv
from binance.client2 import Client
from decimal import Decimal


app = Flask(__name__)
CORS(app)
app.secret_key=b'najkfnjkangnajkgngajkgnkFKA'
 
client = Client(config.API_KEY, config.API_SECRET, tld='com')

@app.route('/')
def index():
    fbal = client.coinfutures_account_balance()
    exchange_info = client.coinfutures_exchange_info()
    symbolpack = exchange_info['symbols']

    return render_template('index.html', my_balances=fbal, symbols=symbolpack)

@app.route('/buy', methods=['POST'])
def buy():
    try:
        order = client.coinfutures_create_order(symbol=request.form['symbol'], 
            side='BUY',
            type='MARKET',
            quantity=request.form['quantity'])
    except Exception as e:
        flash(e.message, 'error')

    return redirect('/')

@app.route('/sell')
def sell():
    return 'Sell'

@app.route('/settings')
def settings():
    return 'Settings'

@app.route('/history')
def history():
    candles = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Jan, 2020")

    processedcandles = []

    for data in candles:
        candle = {
            "time": data[0] / 1000,
            "open": data[1],
            "high": data[2],
            "low": data[3],
            "close": data[4]
        }
        processedcandles.append(candle)

    return jsonify(processedcandles)

