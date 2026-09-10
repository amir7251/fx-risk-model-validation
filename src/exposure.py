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

print('previous USD value:', previous_usd_value)
print('current USD value:', current_usd_value)
print('USD P&L:', usd_pnl)

