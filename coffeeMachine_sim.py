def coffeeMachine():
    print()
    #modules
    import sys
    #intro
    print(' WELCOME TO COFFEE-EXPRESS '.center(88, '\u25CF'))
    # ● = \u25CF

    #data source
    #dictionary to hold items data
    menu = {
    "expresso": {
    'water': 50,
    'coffee': 18,
    'milk': 0,
    'cost': 1.50
    },

    "latte": {
    'water': 200,
    'coffee': 24,
    'milk': 150,
    'cost': 2.50
    },

    "cappuccino": {
    'water': 250,
    'coffee': 24,
    'milk': 100,
    'cost': 3.00
    }
    }

    #report of resoucre left
    resource = {
    'water': 300,
    'coffee': 200,
    'milk': 200 
    }

    #payment data
    PENNY = 0.01
    NICKEL = 0.05
    DIME = 0.1
    QUATER = 0.25

    #functions

    def getItems(dict):
        """
    get either the key or value for iterable
        """
        lst_key = []
        lst_values = []
        for key in dict.keys():
            lst_key.append(key)
        for value in dict.values():
            lst_values.append(value)
        return lst_key, lst_values
    
    
    #simulation of loading
    def simulateLoad():
        print()
        creating = 0
        while creating < 15:
            print('loading... preparing coffee ☕️ | 🔄')
            creating+= 1
        print()
        print('coffee ready ☕️. Enjoy')
       #order
    def order():
        print()
        coffee = input('What kind of coffee:\nExpresso\nLatte\nCappuccino\n>>>       : ').lower()
        if coffee in menu:
            print()
            print(coffee.upper())
            for key, value in menu[coffee].items():#create a key value pair
                print(f'{key}: {value}')# prints the key value of the dictionary
            print()
            if menu[coffee]['water'] < resource['water']: #checks if any resource avaliable
                if menu[coffee]['coffee'] < resource['coffee']:#runs if first code runs
                    if menu[coffee]['milk'] < resource['milk']:#runs if second code runs
                        result = getItems(resource) #assigns results of getItems(dict)
                        #arithemetic agrus
                        new_resource_water = resource['water'] - menu[coffee]['water']
                        new_resource_coffee = resource['coffee'] - menu[coffee]['coffee']
                        new_resource_milk = resource['milk'] - menu[coffee]['milk']
                        #updates the resource dictionary
                        resource.update({"water": new_resource_water, 
                        "coffee": new_resource_coffee,
                        "milk": new_resource_milk
                        }) #updates the resources dictionary to current values
                        payment(coffee)
                    else:
                        print(' I, might need a refill of milk')
                else:
                    print(' I, might need a refill of coffee')
            else:
                print(' I, might need a refill of water')
        else:
            print()
            sys.exit('coffee not in menu: ☕️❗️')
        return coffee #return the coffee choosen
         
    #payment
    def payment(coffee):
        """
    takes user payments and checks whether sufficient or not    
        """
        print()
        print('PAYMENT METHOD: COINS ONLY')
        pennies = int(input('Pennies: '))
        nickels = int(input('Nickels: '))
        dimes = int(input('Dimes: '))
        quaters = int(input('Quaters: '))
        #arithemetic 
        amount_pennies = PENNY*pennies
        amount_nickels = NICKEL*nickels
        amount_dimes = DIME*dimes
        amount_quaters = QUATER*quaters
        print()
        #sum of all coins
        sum_paid = amount_pennies+amount_nickels+amount_dimes+amount_quaters
        print(f"AMOUNT PAID: ${round(sum_paid, 2)}")
        if sum_paid == menu[coffee]['cost']:
            simulateLoad()
            re_order = input("Do you want to re-order? :")# to make user re order another coffee
            match re_order:
                case 'yes':
                    order()
                case 'no':
                    sys.exit("THANK YOU FOR USING COFFEE EXPRESS")
        elif sum_paid > menu[coffee]['cost']:
            simulateLoad()
            print()
            print(f"Your change: ${round(sum_paid-menu[coffee]['cost'], 2)}")# prints out change
            print()
            re_order = input("Do you want to re-order? :")
            match re_order:
                case 'yes':
                    order()
                case 'no':
                    sys.exit("THANK YOU FOR USING COFFEE EXPRESS")
            sys.exit()
        elif sum_paid < menu[coffee]['cost']:
            amount_error = input('Money not sufficient. Do you want to return: ').lower()
            match amount_error:
                case "yes":
                    coffeeMachine()
                case "no":
                    sys.exit()             
    
    #start of machine   
    start = input("What's for today?\n1.coffee\n2.???\n3.report\n>>>     : ").lower()#enter `sys -m modify &resource` to modify resources
    match start:
        case 'coffee': #case where start == 'coffee'
            print()
            order()
        case '???':
            print('COMING SOON')
        case 'report':# report of default resources in machine
            print()
            for key, vaule in resource.items():
                print(f'{key}: {vaule}')
        case 'off':
            sys.exit()
        case 'sys -m modify &resource':# a command-line feature to add more resources to default
            print('welcome_to_system_resources')
            water = int(input('enter_volume_water'))
            coffee = int(input('enter_grams_coffee'))
            milk = int(input('enter_volume_milk'))
            resource.update({
            "water": water,
            "coffee": coffee,
            "milk": milk
            })
            go_back = input('go_back?').lower()
            if go_back == 'yes':
                order()
            else:
                sys.exit('closed_')
        case _:
            typeerror = input("Wrong input. Do you want to restart?: ").lower()
            match typeerror:
                case 'yes':
                    coffeeMachine()
                case 'no':
                    sys.exit()
#calling the function
coffeeMachine()#starts the whole machine