import json
from indicators import calculate_sma

# Load historical data
with open('history.json', 'r') as f:
    data = json.load(f)

# Extract the closing prices
closing_prices = [day['close'] for day in data['prices']]

# Step 2: Calculate indicators
sma = calculate_sma(closing_prices, 10)
