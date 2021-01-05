class CoffeeMachine:
    coffee_details = {'espresso': {'water': 250, 'milk': 0, 'beans': 16, 'price': 4},
                      'latte': {'water': 350, 'milk': 75, 'beans': 20, 'price': 7},
                      'cappuccino': {'water': 200, 'milk': 100, 'beans': 12, 'price': 6}}
    choice = ['espresso', 'latte', 'cappuccino']

    def __init__(self):
        self.milk_balance = 540
        self.water_balance = 400
        self.beans_balance = 120
        self.cups_balance = 9
        self.cash_balance = 550
        self.state = 'Main'

    def __str__(self):
        return f"""The coffee machine has:
    {self.water_balance} of water
    {self.milk_balance} of milk
    {self.beans_balance} of coffee beans
    {self.cups_balance} of disposable cups
    {self.cash_balance} of money"""

    def add_resource(self, water_to_add=0, milk_to_add=0, beans_to_add=0, cups_to_add=0, cash_to_add=0, option=None):

        if option == 'buy':
            water_count = int(self.water_balance / water_to_add) if water_to_add > 0 else 1000
            milk_count = int(self.milk_balance / milk_to_add) if milk_to_add > 0 else 1000
            beans_count = int(self.beans_balance / beans_to_add) if beans_to_add > 0 else 1000
            max_coffee = min(water_count, milk_count, beans_count, self.cups_balance)
            if max_coffee > 0:
                print('I have enough resources, making you a coffee!')
                self.water_balance -= water_to_add
                self.milk_balance -= milk_to_add
                self.beans_balance -= beans_to_add
                self.cups_balance -= cups_to_add
                self.cash_balance += cash_to_add
            else:
                missing_inc = 'water' if water_count <= 0 else 'milk' if milk_count <= 0 else 'beans' \
                    if beans_count <= 0 else 'cup'
                print(f'Sorry, not enough {missing_inc}!')
                return
        else:
            self.water_balance += water_to_add
            self.milk_balance += milk_to_add
            self.beans_balance += beans_to_add
            self.cups_balance += cups_to_add
            self.cash_balance += cash_to_add

    def main(self):
        while True:
            action = input('Write action (buy, fill, take, remaining, exit):\n')
            print()
            if action == 'buy':
                to_buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
                if to_buy == 'back':
                    continue
                elif int(to_buy) in [1, 2, 3]:
                    coffee = CoffeeMachine.coffee_details.get(CoffeeMachine.choice[int(to_buy) - 1])
                    self.add_resource(coffee.get('water'), coffee.get('milk'), coffee.get('beans'), 1,
                                      coffee.get('price'), 'buy')
            elif action == 'fill':
                water_to_add = int(input('Write how many ml of water the coffee machine has:\n'))
                milk_to_add = int(input('Write how many ml of milk the coffee machine has:\n'))
                beans_to_add = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
                cups_to_add = int(input('Write how many cups of coffee you will need:\n'))
                self.add_resource(water_to_add=water_to_add, milk_to_add=milk_to_add, beans_to_add=beans_to_add,
                                  cups_to_add=cups_to_add)
            elif action == 'take':
                print(f'I gave you ${self.cash_balance}')
                self.add_resource(cash_to_add=-self.cash_balance)
            elif action == 'remaining':
                print(self)
            elif action == 'exit':
                break
            else:
                continue
            print()


cm = CoffeeMachine()
cm.main()
