             #creating a shop simulator
#import functions
import sys
#intro
intro = ' CODIFY\'S SHOP '.center(30,'○')
print(intro)
print('''info: we are working on,
providing more items 😃''')
print('')
#items for sale
pencil_sh ='Pencil...............$3'
coca_sh ='Coca-cola...............$5'
waterbottle_sh ='Water-bottle.................$10'
print(pencil_sh)
print(coca_sh)
print(waterbottle_sh)
#item list
item_list = ['Pencil','Coca cola','Water bottle']
#item price
pencil = 3
coca_cola = 5
water_bottle = 10
#item selection
print('')
item = input('SELECT ITEM TO BUY\n').capitalize()
if item in item_list:
    print("\nYOU HAVE SELECTED: \nITEM......... " +  item)
else:
    sys.exit('\nITEM NOT AVALIABLE')   
#quantity of product
quantity_input = int(input('\nENTER QUANTITY OF PRODUCT TO BUY: '))
quan_price_pencil = pencil * quantity_input
quan_price_cocacola = coca_cola * quantity_input
quan_price_waterbottle = water_bottle * quantity_input 
if item == 'pencil'.capitalize():
    print("AMOUNT TO PAY $",quan_price_pencil,'''\ninfo: price for pencil(s)''')
elif item == 'Coca cola'.capitalize():
    print("AMOUNT TO PAY $",quan_price_cocacola,'''\ninfo: price for coca cola(s)''')
elif item == 'Water bottle'.capitalize():
    print("AMOUNT TO PAY $",quan_price_waterbottle,'''\ninfo: price for water bottle(s)''')
else:
    sys.exit('error')
print('')   
#for pencil purchase
def pencilPurchase():
   print("PENCIL PURCHASE")
   pencil_price = float(input('\nENTER AMOUNT TO PAY:$ '))
   if pencil_price == quan_price_pencil:
       print('SOLD')
   elif pencil_price > pencil:
       print('BALANCE_ $',pencil_price-quan_price_pencil,"\n\nTHANKS FOR SHOPPING AT CODIFY'S")
   elif pencil_price < quan_price_pencil:
       print('Insufficient Funds')

if item == 'Pencil':
    pencilPurchase()
else:
    print('')
#for coca cola purchase
def cocacolaPurchase():
   print('COCA COLA PURCHASE')
   cocacola_price = float(input('\nENTER AMOUNT TO PAY:$ '))
   if cocacola_price == quan_price_cocacola:
       print('SOLD')
   elif cocacola_price > quan_price_cocacola:
       print('BALANCE_ $',cocacola_price-quan_price_cocacola,"\n\nTHANKS FOR SHOPPING AT CODIFY'S")
   elif cocacola_price < quan_price_cocacola:
       print('Insufficient Funds')

if item == 'Coca cola':
    cocacolaPurchase()
else:
    print('')
#for water bottle
def waterbottlePurchase():
   print('WATER BOTTLE PURCHASE')
   waterbottle_price = float(input('\nENTER AMOUNT TO PAY:$ '))
   if waterbottle_price == quan_price_waterbottle:
       print('SOLD')
   elif waterbottle_price > quan_price_waterbottle:
       print('BALANCE_ $',waterbottle_price-quan_price_waterbottle,"\n\nTHANKS FOR SHOPPING AT CODIFY'S")
   elif waterbottle_price < quan_price_waterbottle:
       print('Insufficient Funds')

if item == 'Water bottle':
    waterbottlePurchase()
else:
    print('')    
