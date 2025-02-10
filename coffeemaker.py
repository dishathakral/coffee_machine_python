from art1 import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money':0
}
resources_unit={
    "water":'ml',
    "milk":'ml',
    "coffee":'g',
    'money':'$'
}
def int_value(values):
    while True:
        try:
            x=int(input(f'how many {values}?:'))
            return x
        except ValueError:
            print(f"error! {values} is not integer")
def enough_resources(type_coffee):
    ingredients=MENU[type_coffee]['ingredients']
    for items,values in ingredients.items():
        if resources[items]<values:
            print(f"Sorry there is not enough {items}.")
            return False
    return True
def process_coins(type_coffee):
    print("Please insert coins.")
    coin_list={
        'quarters':0.25,
        'dime':0.10,
        'nickels':0.05,
        'pennies':0.01
    }
    total_sum=sum(value*int_value(item) for item,value in coin_list.items())
    if total_sum<MENU[type_coffee]['cost']:
        return False
    else:
        in_change=round(total_sum-MENU[type_coffee]['cost'],2)
        print(f"Here is ${in_change} in change.")
        return True
def update_report(type_coffee):
    for item,value in MENU[type_coffee]['ingredients'].items():
        resources[item]-=value
    resources['money']+=MENU[type_coffee]['cost']

print(logo)
print(f"Espresso     ${MENU['espresso']['cost']}")
print(f"latte        ${MENU['latte']['cost']}")
print(f"cappuccino   ${MENU['cappuccino']['cost']}")
off =False
while not off:
    coffee_type=input("What would you like? (espresso/latte/cappuccino): ").lower()
    coffee_names=list(MENU.keys())
    if coffee_type=='report':
        for key,value in resources.items():
            if key=='money':
                print(f'{key}: {resources_unit[key]}{value}')
            else:
                print(f'{key}: {value}{resources_unit[key]}')
    elif coffee_type not in coffee_names:
        print("Error!Enter valid coffee_name.")
        continue
    elif enough_resources(coffee_type):
        print(f"You can make drink.")
        if process_coins(coffee_type):
            update_report(coffee_type)
            print(f"Here is your {coffee_type} ☕️. Enjoy!")
        else:
            print('Sorry that\'s not enough money. Money refunded.')
    else:
        print(f"Cannot make drink.")
        break

