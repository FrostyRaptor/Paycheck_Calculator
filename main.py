from functions import *

total_pay_before = 0
total_pay_after = 0
week = 1

# Get the user's hourly rate
while True:
    try:
        user_pay = float(input('What is your hourly rate?: '))
        break
    except ValueError:
        print('Invalid')
        

# Figure out the user's hours
while True:
    user_hours = float(input(f'How many hours did you work in week {week}? (-1 to quit): '))
    if user_hours != -1:
        if user_hours >= 0:
            if overtime_qual(user_hours) > 0:
                # User made overtime
                overtime_hours = overtime_qual(user_hours)
                total_pay_before += total_week_pay(user_hours,user_pay,overtime_hours)
                week += 1
            else:
                total_pay_before += total_week_pay(user_hours,user_pay)
                week += 1
        else:
            print('Invalid')
    else:
        break

oasdi_tax = round(oasdi(total_pay_before), 2)
medicare_tax = round(medicare(total_pay_before), 2)
il_state_tax = round(state_tax(total_pay_before), 2)
user_total_tax = round(total_tax(total_pay_before), 2)
total_pay_after = round((total_pay_before - total_tax(total_pay_before)), 2)

print(f'Your total pay is ${round(total_pay_before, 2)} before taxes.')
print(f'Taxable income: {total_pay_before}. OASDI: {oasdi_tax}.')
print(f'Taxable income: {total_pay_before}. Medicare: {medicare_tax}.')
print(f'Taxable income: {total_pay_before}. State Tax: {il_state_tax}.')
print(f'Total amount paid in taxes: {user_total_tax}.')
print(f'Total amount after taxes: {total_pay_after}')