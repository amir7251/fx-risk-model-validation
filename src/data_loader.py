import csv

exchange_rates = []
numeric_rates = []

with open ('data/raw/gbpusd_daily.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)

    missing_rate_count = 0
    non_missing_rate_count = 0

    for row in reader:
        exchange_rate = row[1]
        exchange_rates.append(exchange_rate)

        if exchange_rate == '':
            missing_rate_count = missing_rate_count + 1
        else:
            non_missing_rate_count = non_missing_rate_count + 1
            numeric_rate = float(exchange_rate)
            numeric_rates.append(numeric_rate)

number_of_rows = len(exchange_rates)
count_check = number_of_rows == missing_rate_count + non_missing_rate_count
number_numeric_rates = len(numeric_rates)


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
