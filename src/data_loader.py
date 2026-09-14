import csv
import math

exchange_rates = []
numeric_rates = []
dated_rates = []
seen_dates = []
dated_returns = []

with open ('data/raw/gbpusd_daily.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)

    missing_rate_count = 0
    non_missing_rate_count = 0
    invalid_rate_count = 0
    

    for row in reader:
        exchange_rate = row[1]
        exchange_rates.append(exchange_rate)

        if exchange_rate == '':
            missing_rate_count = missing_rate_count + 1
        else:
            non_missing_rate_count = non_missing_rate_count + 1
            numeric_rate = float(exchange_rate)
            numeric_rates.append(numeric_rate)
            if numeric_rate <= 0 or not math.isfinite(numeric_rate):
                invalid_rate_count = invalid_rate_count + 1
                print(row[0], exchange_rate)
            else:
                dated_rate = [row[0], numeric_rate]
                dated_rates.append(dated_rate)
duplicate_date_count = 0
for observation in dated_rates:
    date = observation[0]
    if date in seen_dates:
        duplicate_date_count = duplicate_date_count + 1
        print('duplicate date:', date)
    else:
        seen_dates.append(date)



number_of_rows = len(exchange_rates)
count_check = number_of_rows == missing_rate_count + non_missing_rate_count
number_numeric_rates = len(numeric_rates)
dated_observaation_count = len(dated_rates)

for index in range(1, len(dated_rates)):
    previous_observation = dated_rates[index - 1]
    current_observation = dated_rates[index]

    previous_date = previous_observation[0]
    previous_rate = previous_observation[1]

    current_date = current_observation[0]
    current_rate = current_observation[1]

    if current_date > previous_date:
        daily_return = current_rate / previous_rate - 1
        dated_returns.append([previous_date, current_date, daily_return])
    else:
        raise ValueError('dates are not in ascending order')

worst_observation = dated_returns[0]

for observation in dated_returns:
    if observation[2] < worst_observation[2]:
        worst_observation = observation

print('largest fall started:', worst_observation[0])
print('largest fall ended:', worst_observation[1])
print('largest fall (%):', worst_observation[2] * 100)

print('number of returns:', len(dated_returns))
print('first return:', dated_returns[0])

print('number of rows:', number_of_rows)
print('missing rate count:', missing_rate_count)
print('non-missing rate count:', non_missing_rate_count)
print('row count check:', count_check)
    
print('number of numeric rates:', number_numeric_rates)
print('first numeric rate:', numeric_rates[0])
if non_missing_rate_count == number_numeric_rates:
    print('the number of numeric rates matches the non missing rate count')
else:
    print('the number of numeric rates do not match the non missing rate count')
print('invalid rate count:', invalid_rate_count)
print('first observation:', dated_rates[0])
print('number of dated observations:', dated_observaation_count)
print('duplicate date count:', duplicate_date_count)