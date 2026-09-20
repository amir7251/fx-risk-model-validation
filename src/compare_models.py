import csv

historical_results = []

with open('data/processed/historical_var_backtest.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        historical_results.append(row)

print('historical results loaded:', len(historical_results))