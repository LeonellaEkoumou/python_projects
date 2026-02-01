#LATIN AMERCIAN CURRENCY CONVERTER
print('welcome to the currency converter for latin american counrtries')
#currency calculator
#Asking for users left balance
pesos=float(input("what do you have left in pesos?"))
soles=float(input("what do you have left in soles?"))
reais=float(input("what do you have left in reais?"))

#Approximatif rates to usd
PESOS_TO_USD = 0.058   
SOLES_TO_USD = 0.27    
REAIS_TO_USD = 0.20

#Convert current balance

usd1=pesos*PESOS_TO_USD
usd2=soles*SOLES_TO_USD
usd3=reais*REAIS_TO_USD

#Calculate the among

total_in_usd=usd1+usd2+usd3
#Print result
print("the total amount you have in usd is:", total_in_usd)