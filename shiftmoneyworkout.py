#######################################
#hour rate
hour_rate = input("rate of pay?:  ")
rate = float(hour_rate)
#######################################
total_hours = input("how many hours?:  ")
hours = int(total_hours)
########################################
#shifts
total_shift = input("how many shifts?:  ")
shift = int (total_shift)
########################################
# tax
tax_rate = 20
########################################
hours_times_pay = hours * rate
#######################################
dreaded_tax = hours_times_pay / tax_rate
########################################

wage_after_tax = dreaded_tax * shift

print(wage_after_tax)