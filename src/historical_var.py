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


backtest_results = []
for index in range(500, len(dated_returns)):
    historical_window = dated_returns[index - 500:index]
    window_returns = []

    for observation in historical_window:
        window_returns.append(observation[2])
    sorted_returns = sorted(window_returns)
    return_threshold = sorted_returns[24]
    return_threshold_99 = sorted_returns[4]
    next_observation = dated_returns[index]
    actual_return = next_observation[2]
    breach = actual_return < return_threshold
    breach_99 = actual_return < return_threshold_99
    backtest_results.append([next_observation[0], next_observation[1], return_threshold, actual_return, breach, return_threshold_99, breach_99])

breach_count = 0
for result in backtest_results:
    if result[4]:
        breach_count = breach_count + 1

breach_rate = breach_count / len(backtest_results)

yearly_counts = {}

for result in backtest_results:
    end_date = result[1]
    year = end_date[:4]
    if year not in yearly_counts:
        yearly_counts[year] = [0, 0]
    yearly_counts[year][0] = yearly_counts[year][0] + 1

    if result[4]:
        yearly_counts[year][1] = yearly_counts[year][1] + 1

for year in yearly_counts:
    counts = yearly_counts[year]
    yearly_breach_rate = counts[1] / counts[0]
    print(year, 'breach rate (%):', yearly_breach_rate * 100)

breach_exceedances = []

for result in backtest_results:
    if result[4]:
        exceedance = result[2] - result[3]
        breach_exceedances.append(exceedance)
largest_exceedance = max(breach_exceedances)
average_exceedance = sum(breach_exceedances) / len(breach_exceedances)

breach_count_99 = 0
for result in backtest_results:
    if result[6]:
        breach_count_99 = breach_count_99 + 1
breach_rate_99 = breach_count_99 / len(backtest_results)

print('window size:', len(historical_window))
print('first observation in window:', historical_window[0])
print('last observation in window;', historical_window[-1])
print('number of sorted returns:', len(sorted_returns))
print('lowest return (%):', sorted_returns[0] * 100)
print('highest return (%):', sorted_returns[-1] * 100)
print('95% return threshold (%):', return_threshold * 100)

print('forecast period started:', next_observation[0])
print('forecast period ended;', next_observation[1])
print('actual return (%):', actual_return * 100)
print('95% threshold breached:', breach)

print('number of returns:', len(dated_returns))
print('first return:', dated_returns[0])
print('number of backtest results:', len(backtest_results))
print('first backtest result:', backtest_results[0])
print('number of breaches:', breach_count)
print('breach rate (%):', breach_rate * 100)
print('yearly counts:', yearly_counts)
print('largest exceedance (percentage points):', largest_exceedance * 100)
print('average exceedance (percentage points):', average_exceedance * 100)
print('number of 99% breaches:', breach_count_99)
print('99% breach rate (%):', breach_rate_99 * 100)