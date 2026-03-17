def analyze_stock_prices(prices):
    total_price = 0
    count = 0
    for price in prices.values():
        total_price += price
        count += 1
    average_price = total_price / count

    volatility_days = []
    for date, price in prices.items():
        if price > average_price * 1.05:
            volatility_days.append((date, "High Volatility"))
        elif price < average_price * 0.95:
            volatility_days.append((date, "Low Volatility"))
        else:
            volatility_days.append((date, "Stable"))
    return average_price, volatility_days

stock_prices = {
    "14-03-2026": 100.0,
    "15-03-2026": 105.0,
    "16-03-2026": 95.0,
    "17-03-2026": 90.0,
    "18-03-2026": 107.0,
    "19-03-2026": 110.50,
    }

average_price, volatility_days = analyze_stock_prices(stock_prices)
print(f"Average Price: {average_price}")
print("\nVolatility Days:")
for date, status in volatility_days:
    print(f"  {date}: {status}")

print("\nList of Volatility Days:", volatility_days)