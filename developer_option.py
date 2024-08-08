correct_input = {
}


for r in range(7):
    correct_input['value'+str(r)] = True

true_values = []

i = 0
while i <= 6:
      print()
      user_input= input('Enter open\n')    
      if user_input != 'open':
          correct_input['value'+str(i)]= False
          print(f'typo error')
      elif user_input == 'open':
          correct_input['value'+str(i)]= True
      i+=1
         
for x,y in correct_input.items():
    if y == True:
        true_values.append(y)
print()       
if len(true_values) == 7:
    print(f'You are a developer')
elif len(true_values) != 7:
    print(f'There were some typos: please try again')