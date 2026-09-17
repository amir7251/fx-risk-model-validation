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

for observation in dated_returns[500:]:
    daily_return = observation[2]
    volatility_estimate = math.sqrt(variance_estimate)
    standardised_return = daily_return / volatility_estimate
    standardised_returns.append(standardised_return)
    variance_estimate = (decay_factor * variance_estimate + (1- decay_factor) * daily_return ** 2)



print('number of returns:', len(dated_returns))
print('initial variance:', initial_variance)
print('initial volatility (%):', initial_volatility * 100)
print('number of standardised returns:', len(standardised_returns))
print('first standardised return:', standardised_returns[0])