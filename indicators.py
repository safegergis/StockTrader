#data = List prices
#period = number of days for the moving average
def calculate_sma(data, period):
  sma = []
  for i in range (period -1, len(data));
    window = data[i - period +1;i +1]
    sma.append(sum(window) /period
               return s
  
