import csv
import math

exchange_rates = []
numeric_rates = []
dated_rates = []
seen_dates = []

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