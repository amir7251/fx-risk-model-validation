import csv
import math

dated_returns = []

with open('data/processed/gbpusd_returns.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        previous_date = row[0]
        current_date = row[1]
        daily_return = float(row[2])

        dated_returns.append([previous_date, current_date, daily_return])

initial_returns = []

for observation in dated_returns[:500]:
    initial_returns.append(observation[2])
squared_returns = []

for daily_return in initial_returns:
    squared_returns.append(daily_return ** 2)
initial_variance = sum(squared_returns) / len(squared_returns)
initial_volatility = math.sqrt(initial_variance)

decay_factor = 0.94
variance_estimate = initial_variance
standardised_returns = []
volatility_estimates = []
filtered_backtest_results = []

for observation in dated_returns[500:]:
    daily_return = observation[2]
    volatility_estimate = math.sqrt(variance_estimate)
    volatility_estimates.append(volatility_estimate)
    standardised_return = daily_return / volatility_estimate
    standardised_returns.append(standardised_return)
    variance_estimate = (decay_factor * variance_estimate + (1- decay_factor) * daily_return ** 2)

for index in range(500, len(standardised_returns)):
    historical_window = standardised_returns[index - 500:index]
    sorted_returns = sorted(historical_window)
    standardised_threshold_95 = sorted_returns[24]
    standardised_threshold_99 = sorted_returns[4]
    forecast_volatility = volatility_estimates[index]
    return_threshold_95 = standardised_threshold_95 * forecast_volatility
    return_threshold_99 = standardised_threshold_99 * forecast_volatility
    next_observation = dated_returns[index + 500]
    actual_return = next_observation[2]
    breach_95 = actual_return < return_threshold_95
    breach_99 = actual_return < return_threshold_99
    filtered_backtest_results.append([next_observation[0], next_observation[1], return_threshold_95, actual_return, breach_95, return_threshold_99, breach_99])

filtered_breach_count_95 = 0
filtered_breach_count_99 = 0

for result in filtered_backtest_results:
    if result[4]:
        filtered_breach_count_95 = filtered_breach_count_95 + 1
    if result[6]:
        filtered_breach_count_99 = filtered_breach_count_99 + 1
filtered_breach_rate_95 = filtered_breach_count_95 / len(filtered_backtest_results)
filtered_breach_rate_99 = filtered_breach_count_99 / len(filtered_backtest_results)

print('number of returns:', len(dated_returns))
print('initial variance:', initial_variance)
print('initial volatility (%):', initial_volatility * 100)
print('number of standardised returns:', len(standardised_returns))
print('first standardised return:', standardised_returns[0])
print('number of filtered backtest results:', len(filtered_backtest_results))
print('first filtered result:', filtered_backtest_results[0])
print('last filtered result:', filtered_backtest_results[-1])
print('filtered 95% breach count:', filtered_breach_count_95)
print('filtered 95% breach rate (%):', filtered_breach_rate_95 * 100)
print('filtered 99% breach count:', filtered_breach_count_99)
print('filtered 99% brach rate (%):', filtered_breach_rate_99 * 100)

with open('data/processed/filtered_var_backtest.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        'previous_date', 'current_date', 'threshold_95',
        'actual_return', 'breach_95', 'threshold_99', 'breach_99'
    ])
    writer.writerows(filtered_backtest_results)