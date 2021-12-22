from consolemenu import *
from consolemenu.items import *
import random
import names

### MENU ###

def main_menu():
    main_menu = ConsoleMenu('MAIN MENU', 'Select an option')
    option_start_game = FunctionItem('START GAME', start_game)
    option_quit = FunctionItem('QUIT GAME', exit)

    main_menu.append_item(option_start_game)
    main_menu.append_item(option_quit)

    main_menu.show(show_exit_option = False)

### GAME ###

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

male = 'male'
female = 'female'

fname = ''
lname = ''
country = ''
city = ''

def start_game():
    global fname, lname, country, city
    print('### INSERT YOUR DETAILS ###')
    fname = input('> First name: ')
    lname = input('> Last name: ')
    country = input('> Country: ')
    city = input('> City: ')

    complete_name = fname + ' ' + lname
    random_month = months[random.randrange(0, 11)]
    if random_month == 'February':
        random_day = random.randrange(1, 28)
    else:
        random_day = random.randrange(1, 30)
    print(f'\n> Hi {complete_name}, you were born on {random_month} {random_day} in {city}, {country}')

    mom = names.get_full_name(gender = 'female')
    dad = names.get_first_name(gender = 'male') + ' ' + lname
    print(f'\n> Your mom is {mom} (age {random.randrange(18, 35)})')
    print(f'\n> Your dad is {dad} (age {random.randrange(18, 35)})')
    input('\nPRESS RETURN TO ADVANCE')

    print('\n### STATS ###')
    print(f'\n> Happiness: {random.randrange(0, 100)}%')
    print(f'\n> Health: {random.randrange(0, 100)}%')
    print(f'\n> Smartness: {random.randrange(0, 100)}%')
    print(f'\n> Beauty: {random.randrange(0, 100)}%')
    input('\nPRESS RETURN TO ADVANCE')

    print('\n### EVENT ###')
    print(f'\n> You are now attending {names.get_full_name(gender = male)} Primary School')
    input('\nPRESS RETURN TO ADVANCE')

    print('\n### EVENT ###')
    print(f'\n> You are now attending {names.get_full_name(gender = male)} Middle School')
    input('\nPRESS RETURN TO ADVANCE')

    print('\n### EVENT ###')
    print(f'\n> You are now attending {names.get_full_name(gender = male)} High School')
    input('\nPRESS RETURN TO ADVANCE')

### START ###

main_menu()