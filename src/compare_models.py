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

historical_yearly_counts = {}

for result in matched_historical_results:
    year = result[1][:4]

    if year not in historical_yearly_counts:
        historical_yearly_counts[year] = [0, 0, 0]

    historical_yearly_counts[year][0] += 1

    if result[4] == 'True':
        historical_yearly_counts[year][1] += 1
    if result[6] == 'True':
        historical_yearly_counts[year][2] += 1

filtered_yearly_counts = {}

for result in filtered_results:
    year = result[1][:4]

    if year not in filtered_yearly_counts:
        filtered_yearly_counts[year] = [0, 0, 0]

    filtered_yearly_counts[year][0] += 1

    if result[4] == 'True':
        filtered_yearly_counts[year][1] += 1

    if result[6] == 'True':
        filtered_yearly_counts[year][2] += 1

for year in historical_yearly_counts:
    historical_counts = historical_yearly_counts[year]
    filtered_counts = filtered_yearly_counts[year]

    historical_rate_95 = historical_counts[1] / historical_counts[0] * 100
    filtered_rate_95 = filtered_counts[1] / filtered_counts[0] * 100
    historical_rate_99 = historical_counts[2] / historical_counts[0] * 100
    filtered_rate_99 = filtered_counts[2] / filtered_counts[0] * 100


    print(year, 'historical 95% breach rate (%):', historical_rate_95)
    print(year, 'filtered 95% breach rate (%):', filtered_rate_95)
    print(year, 'historical 99% breach rate (%):', historical_rate_99)
    print(year, 'filtered 99% breach rate (%):', filtered_rate_99)

historical_exceedances_95 = []

for result in matched_historical_results:
    if result[4] == 'True':
        threshold = float(result[2])
        actual_return = float(result[3])
        exceedance = threshold - actual_return
        historical_exceedances_95.append(exceedance)

historical_average_exceedance_95 = (sum(historical_exceedances_95) / len(historical_exceedances_95))
historical_largest_exceedance_95 = max(historical_exceedances_95)

filtered_exceedances_95 = []

for result in filtered_results:
    if result[4] == 'True':
        threshold = float(result[2])
        actual_return = float(result[3])
        exceedance = threshold - actual_return
        filtered_exceedances_95.append(exceedance)

filtered_average_exceedance_95 = (sum(filtered_exceedances_95) / len(filtered_exceedances_95))
filtered_largest_exceedance_95 = max(filtered_exceedances_95)

historical_exceedances_99 = []

for result in matched_historical_results:
    if result[6] == 'True':
        threshold = float(result[5])
        actual_return = float(result[3])
        exceedance = threshold - actual_return
        historical_exceedances_99.append(exceedance)

historical_average_exceedance_99 = (sum(historical_exceedances_99) / len(historical_exceedances_99))
historical_largest_exceedance_99 = max(historical_exceedances_99)

filtered_exceedances_99 = []

for result in filtered_results:
    if result[6] == 'True':
        threshold = float(result[5])
        actual_return = float(result[3])
        exceedance = threshold - actual_return
        filtered_exceedances_99.append(exceedance)

filtered_average_exceedance_99 = (sum(filtered_exceedances_99) / len(filtered_exceedances_99))
filtered_largest_exceedance_99 = max(filtered_exceedances_99)

print('historical 95% average exceedance (percentage points):', historical_average_exceedance_95 * 100)
print('historical 95% largest exceedance (percentage points):', historical_largest_exceedance_95 * 100)
print('filtered 95% average exceedance (percentage points):', filtered_average_exceedance_95 * 100)
print('filtered 95% largest exceedance (percentage points):', filtered_largest_exceedance_95 * 100)
print('historical 99% average exceedance (percentage points):', historical_average_exceedance_99 * 100)
print('historical 99% largest exceedance (percentage points):', historical_largest_exceedance_99 * 100)
print('filtered 99% average exceedance (percentage points):', filtered_average_exceedance_99 * 100)
print('filtered 99% largest exceedance (percentage points):', filtered_largest_exceedance_99 * 100)
