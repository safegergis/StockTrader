import json

def calculate_sma(json_data):
  data = json_data
  
  # Extract dates and closing prices
  dates = [day['Date'] for day in data]
  closing_prices = [day['Close'] for day in data]

  # Calculate short and long SMAs
  short_sma = []  # 20-day SMA
  long_sma = []   # 50-day SMA
  
  # Calculate SMAs
  for i in range(49, len(closing_prices)):
    short_window = closing_prices[i-19:i+1]
    long_window = closing_prices[i-49:i+1]
    short_sma.append(sum(short_window) / 20)
    long_sma.append(sum(long_window) / 50)

  # Initialize trading variables  
  position = 0  # 0 = no position, 1 = long
  initial_balance = 100000  # Initial capital
  balance = initial_balance
  shares = 0
  trades = []
  total_trades = 0
  winning_trades = 0
  
  # Simulate trading
  for i in range(1, len(short_sma)):
    date = dates[i+49]  # Offset by 49 due to SMA calculation
    current_price = closing_prices[i+49]
    
    # Buy signal - short SMA crosses above long SMA
    if short_sma[i] > long_sma[i] and short_sma[i-1] <= long_sma[i-1] and position == 0:
      shares = int(balance / current_price)  # Buy as many shares as possible
      cost = shares * current_price
      balance -= cost
      position = 1
      entry_price = current_price
      
      trades.append({
        "date": date,
        "type": "BUY",
        "shares": shares,
        "price": current_price,
        "amount": cost,
        "balance": balance,
        "return": ((balance + (shares * current_price)) - initial_balance) / initial_balance * 100
      })
      total_trades += 1
      
    # Sell signal - short SMA crosses below long SMA  
    elif short_sma[i] < long_sma[i] and short_sma[i-1] >= long_sma[i-1] and position == 1:
      proceeds = shares * current_price
      balance += proceeds
      position = 0
      
      trade_return = (current_price - entry_price) / entry_price * 100
      if trade_return > 0:
        winning_trades += 1
        
      trades.append({
        "date": date,
        "type": "SELL", 
        "shares": shares,
        "price": current_price,
        "amount": proceeds,
        "balance": balance,
        "return": (balance - initial_balance) / initial_balance * 100
      })
      shares = 0
      total_trades += 1

  # Calculate final metrics
  final_value = balance + (shares * closing_prices[-1])
  total_return = (final_value - initial_balance) / initial_balance * 100
  total_gain_loss = final_value - initial_balance
  
  metrics = {
    "initial_balance": initial_balance,
    "final_balance": final_value,
    "total_gain_loss": total_gain_loss,
    "total_return": total_return,
    "total_trades": total_trades,
  }

  return json.dumps(trades), json.dumps(metrics)
 