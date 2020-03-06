#Actions in machine
def print_state():
    print()
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'{money} of money')
    print()

class ResourceError():
    pass

water = 1200
milk = 540
beans = 120
cups =9
money = 550

def select_actions():
    return input('Write what do you want :(buy-fill-take-remaining-exit): ')

def select_flavour():
    answer = input ('1-espresso','2-latte','3-cappuccino','4-back to main menu: ')
    if answer == '4-back to main menu:':
        return 0
    else:
        return int(answer)

def is_enough(need_water=0, need_milk=0, need_beans=0):
    if water < need_water:
        print('Sorry, there is no enough water')
    if milk < need_milk:
        print('Sorry, there is no enough milk')
    if beans < need_beans :
        print('Sorry, there is no enough beans')

def buy():
    global water, milk, beans, cups, money
    try :
        if select_flavour() == 1 :
            is_enough(need_water=250 , need_beans=16)
            water -= 250
            beans -= 16
            cups -= 1
            money -= 4
        elif select_flavour() == 2:
            is_enough(need_water=250,need_milk=75, need_beans=16)
            water -= 350
            milk -= 75
            beans -= 20
            cups -= 1
            money -= 7
        elif select_flavour() == 3 :
            is_enough(need_water=200, need_milk=100, need_beans=12)
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money -= 6
        else:
            raise ValueError('Unknown flavour')
    except ResourceError (Exception):
        pass

def fill():
    global water, milk, beans, cups
    water += int(input('how many ml of water do you want to add: '))
    milk  += int(input('how many ml of milk do you want to add: '))
    beans += int(input('how many ml of beans do you want to add: '))
    cups += int(input('how many ml of cups do you want to add: '))

def take():
    global money
    print(f'It is all your {money}$')

def main():
    while True:
         action = select_actions()
         if action == 'buy':
             buy()
         elif action == 'fill':
             fill()
         elif action == 'take':
             take()
         elif action == 'exit':
             break
         elif action == 'remaining':
             print_state()
         else:
             raise ValueError(f'Unknown command {action}')

    if __name__ == '__main__':
        main()
