var chart = LightweightCharts.createChart(document.body, {
	width: 600,
  height: 300,
	layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
});

var candleSeries = chart.addCandlestickSeries({
  upColor: '#0fec3f',
  downColor: '#ec0000',
  borderDownColor: '#ec0000',
  borderUpColor: '#0fec3f',
  wickDownColor: '#ec0000',
  wickUpColor: '#0fec3f',
});

fetch('http://localhost:5000/history')
	.then((r) => r.json())
	.then((response) => {
		console.log(response)

		candleSeries.setData(response);
	})


var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_1h");

binanceSocket.onmessage = function (event) {
	var message = JSON.parse(event.data);

	var candlestick = message.k;

	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	})
}

