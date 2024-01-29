# To find which day if we buy and sell the stock will 
# get maximum profit...
def sellDay(price):
    maxProfit = 0
    minPrice = float('inf')
    for i in range(len(price)):
        if (price[i] < minPrice):
            minPrice = price[i]
        elif price[i] - minPrice > maxProfit:
            maxProfit = price[i] - minPrice
    return maxProfit
        
price = [7, 4, 1, 3, 6, 16]
result = sellDay(price)
print(result)
