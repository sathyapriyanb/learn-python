# Write your code here
import os
import random


class Game:
    def __init__(self):
        file_path = os.getcwd() + '\\rating.txt'
        # self.win = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
        self.win = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water',
                    'dragon', 'devil', 'lightning', 'gun']
        f = open(file_path, 'r')
        name = input('Enter your name:')
        print(f"Hello, {name}")
        options_chosen = input()
        options_chosen = ['rock', 'paper', 'scissors'] if not options_chosen else options_chosen.split(",")
        print("Okay, let's start")
        ratings_list = f.readlines()
        f.close()
        ratings_map = {}
        for line in ratings_list:
            data = line.replace('\n', '').split(" ")
            ratings_map[data[0]] = data[1]
        rating = int(ratings_map.get(name, 0))

        while True:
            user_ip = input()
            if user_ip == '!exit':
                print('Bye')
                break
            elif user_ip == '!rating':
                print(f'Your rating: {rating}')
                continue
            elif user_ip not in options_chosen:
                print('Invalid input')
                continue
            sys_op = random.choice(options_chosen)
            ind = self.win.index(user_ip)
            wining_combo = self.win[ind:] + self.win[: ind -1]
            diff = wining_combo.index(sys_op)
            if diff == 0:
                print(f'There is a draw ({sys_op})')
                rating += 50
            elif diff > 7:
                print(f'Sorry, but the computer chose {sys_op}')
            else:
                print(f'Well done. The computer chose {sys_op} and failed')
                rating += 100
        ratings_map[name] = rating

        f = open(file_path, 'w')
        for x in ratings_map:
            print(x, ratings_map[x], file=f)
        f.close()


g = Game()
