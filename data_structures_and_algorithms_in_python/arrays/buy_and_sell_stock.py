def buy_and_sell_stock_once(prices):
  max_value = max(prices)
  max_index = prices.index(max_value)
  min_value = min(prices)
  min_index = prices.index(min_value)
  if max_index > min_index:
    return max_value - min_value
  
  max_profit = 0
  for i in range(len(prices)):
    for j in range((i+1), len(prices)):
      if prices[j] - prices[i] > max_profit:
        max_profit = prices[j] - prices[i]
  return max_profit
    