
                        #creating a shop simulator 
#items
import sys
print('                                      ',80,'٪' , 'DISCOUNT')
pen_cil_pri ='Pencil...............$3'
print(pen_cil_pri)
print('info: ','''sorry 😓 we only have pencils available\nBut our team will update soon''')
#assignment
pen_cil2 = 3
pen_cil ="pencil"
#selection1
select_1= input(' \nSELECT ITEM FROM MENU\n')
if select_1.casefold()== pen_cil:
    print('YOU HAVE SELECTED: \nITEM.......... ' + select_1)
else:
    sys.exit('\nITEM NOT AVALIABLE')

#quantity
num_quantity=int(input("\nENTER QUANTITY OF ITEM:  "))
print('QUANTITY OF ITEMS TO BUY ARE :  ',num_quantity)
new_pri = pen_cil2 * num_quantity
print('AMOUNT:  ', new_pri)

#pen_cil
pen_cil=float(input('\nPLEASE ENTER AMOUNT TO PAY\n'))
#discount/generally assignments writes
per_act = 100
dis_p1 = 60 / per_act * new_pri
dis_ctmoney = new_pri - dis_p1
new_disp1 = round(dis_p1 , 3)
balan = pen_cil - dis_p1
new_bala = round(balan, 3)
#quantity write 
quan_am = new_pri - new_disp1 
if pen_cil == new_pri:
    print('DISCOUNT')
    print('$', new_disp1)
    print('BALANCE_ $',pen_cil - new_disp1,'\nSOLD') 
elif pen_cil > new_pri:
    print("DISCOUNT")
    print('$', new_disp1) 
    print('BALANCE_ $', balan , "\n\nTHANK YOU FOR SHOPPING AT CODIFY'S")
elif pen_cil < new_pri:
    sys.exit('Insufficient funds')
    