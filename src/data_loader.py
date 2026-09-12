import csv

exchange_rates = []

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
            non_missing_rate_count_rate_count = non_missing_rate_count = non_missing_rate_count + 1

number_of_rows = len(exchange_rates)
count_check = number_of_rows == missing_rate_count + non_missing_rate_count_rate_count
print('number of rows:', number_of_rows)
print('missing rate count:', missing_rate_count)
print('valid rate count:', non_missing_rate_count_rate_count)
print('valid count check:', count_check)
