from yfinance import Ticker

def fetch_history(symbol, start_date, end_date):
    ticker = Ticker(symbol)
    history = ticker.history(start=start_date, end=end_date)
    # Convert the DataFrame to JSON format
    history = history.reset_index()  # This brings the date index into a column
    history_json = history.to_json(orient="records")

    return history_json 