import argparse
import math


def calc_payment():
    global interest
    interest = interest / 1200
    payment = math.ceil(
        principal * interest * math.pow(1 + interest, periods) / (math.pow(1 + interest, periods) - 1))
    message = f'Your monthly payment = {payment}!'
    print(message)
    over_payment = payment * periods - principal
    print(f'Overpayment = {over_payment}')


def calc_months():
    global interest
    interest = interest / 1200
    periods = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
    years = periods // 12
    no_months = periods % 12
    months_txt = f"{no_months} month{no_months and 's'}" if no_months > 0 else ""
    months_txt = " and " + months_txt if no_months > 0 and years > 0 else months_txt
    years_txt = f"{years} year{years and 's'}" if years > 0 else ""
    full_text = 'It will take ' + years_txt + months_txt + ' to repay this loan!'
    print()
    print(full_text)
    over_payment = round(payment * periods - principal)
    print(f'Overpayment = {over_payment}')


def calc_principal():
    global interest
    interest = interest / 1200
    principal = int(
        payment / (interest * math.pow(1 + interest, periods) / (math.pow(1 + interest, periods) - 1)))
    print(f'Your loan principal = {principal}!')
    over_payment = round(payment * periods - principal)
    print(f'Overpayment = {over_payment}')


def calc_diff_payments():
    global interest
    interest = interest / 1200
    monthly_payment = []
    print(periods)
    for i in range(1, periods + 1):
        payment = math.ceil((principal / periods) + interest * (principal - (principal * (i - 1) / periods)))
        monthly_payment.append(payment)
        print(f'Month {i - 1}: payment is {payment}')
    over_payment = sum(monthly_payment) - principal
    print(f'Overpayment = {over_payment}')


parser = argparse.ArgumentParser()
parse_group = parser.add_argument_group()
parse_group.add_argument('--type')  # , choices=['annuity', 'diff'])
parse_group.add_argument('--payment', type=float)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
args = parser.parse_args()

calc_type = args.type
payment = args.payment
interest = args.interest
principal = args.principal
periods = args.periods

if calc_type not in ['annuity', 'diff']:
    print('Incorrect parameters')
    exit()

if calc_type == 'diff' and payment:
    print('Incorrect parameters')
    exit()

if not interest:
    print('Incorrect parameters')
    exit()

if payment and payment < 0:
    print('Incorrect parameters')
    exit()

if principal and principal < 0:
    print('Incorrect parameters')
    exit()

if periods and periods < 0:
    print('Incorrect parameters')
    exit()

if interest and interest < 0:
    print('Incorrect parameters')
    exit()

if sum(value is None for value in vars(args).values()) != 1:
    print('Incorrect parameters')
    exit()

if calc_type == 'diff':
    calc_diff_payments()
elif payment is None:
    calc_payment()
elif principal is None:
    calc_principal()
elif periods is None:
    calc_months()
