pounds_held = 500000
previous_exchange_rate = 1.25
current_exchange_rate = 1.23

def calculate_usd_value(gbp_amount, exchange_rate):
    return gbp_amount * exchange_rate
previous_usd_value = calculate_usd_value(pounds_held, previous_exchange_rate)
current_usd_value = calculate_usd_value(pounds_held, current_exchange_rate)

def calculate_usd_pnl(previous_value, current_value):
    return current_value - previous_value
usd_pnl = calculate_usd_pnl(previous_usd_value, current_usd_value)
loss_test_actual = calculate_usd_pnl(200000, 195000)
loss_test_expected = -5000
loss_test_passed = loss_test_actual == loss_test_expected

def is_var_breach (pnl, var_threshold):
    return pnl < -var_threshold
loss_above_threshold = is_var_breach(-12000, 10000)


print('previous USD value:', previous_usd_value)
print('current USD value:', current_usd_value)
print('USD P&L:', usd_pnl)
print('loss test actual:', loss_test_actual)
print('loss test expected:', loss_test_expected)
if loss_test_passed:
    print('loss test passed')
else:
    print('loss test failed')
print('loss exceeds VaR threshold', loss_above_threshold)
