import random

question =input('Enter your question: ')

random_number=random.randint(1, 9)

if random_number==1:
   print('Yes - definitely')
elif random_number==2:
   print('It is decidedly so')
elif random_number==3:
   print("Without a doubt")
elif random_number==4:
   print('Reply hazy, try again.')
elif random_number==5:
   print('Better not tell you now')
else :
   print("no")