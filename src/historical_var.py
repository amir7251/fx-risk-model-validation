import csv

dated_returns = []

with open('data/processed/gbpusd_returns.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        previous_date = row[0]
        current_date = row[1]
        daily_return = float(row[2])

        dated_returns.append([previous_date, current_date, daily_return])

historical_window = dated_returns[:500]
print('window size:', len(historical_window))
print('first observation in window:', historical_window[0])
print('last observation in window;', historical_window[-1])

print('number of returns:', len(dated_returns))
print('first return:', dated_returns[0])