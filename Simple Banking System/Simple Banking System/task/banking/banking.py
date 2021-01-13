# Write your code here
import random
import sqlite3
import sys


# conn = sqlite3.connect('card.s3db')
# cur = conn.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
# cur.execute('INSERT INTO card(id, number, pin, balance) values(?)')
# cur.execute('"SELECT * FROM card WHERE num=?"')
# conn.commit()
# cur.fetchall()


def connect_db(name):
    conn = sqlite3.connect(name)
    query = 'CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)'
    execute_query(conn, query)
    # query = 'SELECT * FROM card WHERE number'
    # results = execute_query(conn, query)
    # for row in results:
    #     print(row)
    return conn


def execute_query(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    return cur.fetchone()


def convert_len(num, length):
    return '0' * (length - len(str(num))) + str(num)


def get_checksum(card_num):
    num = [int(i) for i in card_num]
    for i in range(0, len(num), 2):
        num[i] *= 2
        num[i] = num[i] if num[i] <= 9 else num[i] - 9
    checksum = (10 - (sum(num) % 10)) % 10
    return str(checksum)


class Banking:

    def __init__(self):
        self.state = -1
        self.card_num = ''
        self.conn = connect_db('card.s3db')

    def controller(self):
        while True:
            if self.state == -1:
                self.home()
            elif self.state == 0:
                print('Bye!')
                sys.exit()
            elif self.state == 1:
                self.create()
            elif self.state == 2:
                self.login()
            elif self.state == 3:
                self.account_status()
            else:
                self.state = -1
            print()

    def home(self):
        self.state = int(input('''1. Create an account
2. Log into account
0. Exit\n'''))

    def login(self):
        card_num = input('Enter your card number:\n')
        pin = input('Enter your PIN:\n')
        query = f"SELECT pin FROM card WHERE number={card_num}"
        result = execute_query(self.conn, query)

        if result and int(result[0]) == int(pin):
            print('You have successfully logged in!')
            self.card_num = card_num
            self.state = 3
        else:
            print('Wrong card number or PIN!')
            self.state = -1

    def create(self):
        while True:
            acc_num = random.randrange(0, 999999999)
            card_num = '400000' + convert_len(acc_num, 9)
            card_num += get_checksum(card_num)
            query = f"SELECT number FROM card WHERE number={card_num}"
            result = execute_query(self.conn, query)
            if result is None:
                break
        pin = random.randint(0, 9999)
        pin = convert_len(pin, 4)
        query = f'INSERT INTO card(id, number, pin, balance) values(1, {card_num}, {pin}, 0)'
        execute_query(self.conn, query)
        print(f'''Your card has been created
Your card number:
{card_num}
Your card PIN:
{pin}''')
        self.state = -1

    def account_status(self):
        choice = int(input('''1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit\n'''))
        balance_query = f"SELECT balance FROM card WHERE number={self.card_num}"
        if choice == 1:
            result = execute_query(self.conn, balance_query)
            print(f'Balance: {result[0]}')
            self.state = 3
        elif choice == 2:
            income = int(input('Enter income:\n'))
            result = execute_query(self.conn, balance_query)
            income += result[0]
            update_balance = f'update card SET balance={income} WHERE number={self.card_num}'
            execute_query(self.conn, update_balance)
            self.state = 3
        elif choice == 3:
            card = input('Enter card number:\n')
            check_sum = get_checksum(card[:-1])
            if card[-1] != check_sum:
                print('Probably you made a mistake in the card number. Please try again!')
            else:
                from_balance = execute_query(self.conn, balance_query)
                balance_query = f"SELECT balance FROM card WHERE number={card}"
                to_balance = execute_query(self.conn, balance_query)
                if to_balance is None:
                    print('Such a card does not exist.')
                else:
                    amount = int(input('Enter how much money you want to transfer:\n'))
                    if amount > from_balance[0]:
                        print('Not enough money!')
                    else:
                        print('Success!')
                        update_balance = f'update card SET balance={from_balance[0] - amount} WHERE number={self.card_num}'
                        execute_query(self.conn, update_balance)
                        update_balance = f'update card SET balance={to_balance[0] + amount} WHERE number={card}'
                        execute_query(self.conn, update_balance)

            self.state = 3
        elif choice == 4:
            print('The account has been closed!')
            delete_query = f'DELETE FROM card WHERE number={self.card_num}'
            execute_query(self.conn, delete_query)
            self.state = -1
        elif choice == 5:
            print('You have successfully logged out!')
            self.card_num = ''
            self.state = -1
        elif choice == 0:
            self.state = 0
        else:
            pass


banking = Banking()
banking.controller()
