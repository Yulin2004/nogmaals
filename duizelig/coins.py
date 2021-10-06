# name of student: Yu-Lin Roozemond
# number of student:99067028
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # hier moet je typen hoeveel euro (cent) het is.
paid = int(float(input('Paid amount: ')) * 100) #hier moet je aangeven hoeveel je geeft.
change = paid - toPay #dit geeft aan hoeveel wisselgeld je krijgt.

if change > 0: #Dit is het begin getal van de change.
  coinValue = 500 #dit is de coinvalue.
  
  while change > 0 and coinValue > 0: #dit geeft aan wat je terug krijgt
    nrCoins = change // coinValue #dit ie het uiteindelijke bedrag dat je krijgt

    if nrCoins > 0: #max bedrag wat je krijgt
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #hoeveel euro cent of hele euro's je krijgt
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #je cashback
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    
    if coinValue == 500:
        coinValue = 500
    elif coinValue == 300:
        coinValue = 300
    elif coinValue == 200:
        coinValue = 200
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #geen cashback
  print('Change not returned: ', str(change) + ' cents')
else:   
  print('done')