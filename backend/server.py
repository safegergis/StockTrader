from flask import Flask, request, jsonify
from yfinance import Ticker
from flask_cors import CORS
from trading_strategy import calculate_sma
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = '*'


@app.route("/fetch_history", methods=["GET"])
def fetch_history():
    symbol = request.args.get("symbol")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    ticker = Ticker(symbol)
    history = ticker.history(start=start_date, end=end_date)
    # Convert the DataFrame to JSON format
    history = history.reset_index()  # This brings the date index into a column
    history_json = history.to_json(orient="records")

    return history_json

@app.route("/run_backtest", methods=["POST"])
def run_backtest():
    json_data = request.json
    trades, metrics = calculate_sma(json_data)
    return jsonify(trades, metrics)
