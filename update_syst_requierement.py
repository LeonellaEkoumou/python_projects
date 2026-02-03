# Check if you can upadate your phone system
print("For start the update, your device should be at least at 80 percent of battery and the wifi have to be coonect")
battery=float(input('enter your battery percentage: '))
wifi=float(input('if your wifi is connect tape 1, if is not tape 0: '))
if battery > 80 and wifi==1:
  print('you can download the update :)')
elif battery > 80 or wifi==0:
  print('Please connect the wifi')
elif battery < 80 or wifi==1:
  print("Please charge your phone to 80 percent")
else :
  print('Sorry you can update the device for now')