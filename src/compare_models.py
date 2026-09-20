import csv

historical_results = []

with open('data/processed/historical_var_backtest.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        historical_results.append(row)

filtered_results = []

with open('data/processed/filtered_var_backtest.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        filtered_results.append(row)

print('filtered results loaded:', len(filtered_results))

filtered_periods = []

for result in filtered_results:
    period = [result[0], result[1]]
    filtered_periods.append(period)

matched_historical_results = []

for result in historical_results:
    period = [result[0], result[1]]

    if period in filtered_periods:
        matched_historical_results.append(result)

print('matched historical results:', len(matched_historical_results))

historical_breach_count_95 = 0
historical_breach_count_99 = 0

for result in matched_historical_results:
    if result[4] == 'True':
        historical_breach_count_95 = historical_breach_count_95 + 1

    if result[6] == 'True':
        historical_breach_count_99 = historical_breach_count_99 + 1

historical_breach_rate_95 = (historical_breach_count_95 / len(matched_historical_results) * 100)
historical_breach_rate_99 = (historical_breach_count_99 / len(matched_historical_results) * 100)

filtered_breach_count_95 = 0
filtered_breach_count_99 = 0

for result in filtered_results:
    if result[4] == 'True':
        filtered_breach_count_95 = filtered_breach_count_95 + 1

    if result[6] == 'True':
        filtered_breach_count_99 = filtered_breach_count_99 + 1


filtered_breach_rate_95 = (filtered_breach_count_95 / len(filtered_results) * 100)
filtered_breach_rate_99 = (filtered_breach_count_99 / len(filtered_results) * 100)


print('95% VaR — expected breach rate: 5%')
print('Historical (%):', historical_breach_rate_95)
print('Filtered (%):', filtered_breach_rate_95)

print('99% VaR — expected breach rate: 1%')
print('Historical (%):', historical_breach_rate_99)
print('Filtered (%):', filtered_breach_rate_99)