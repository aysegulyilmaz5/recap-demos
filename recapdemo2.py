number = int(input("Please enter a number:"))
isPrime = True

for x in range(2,number):
  if number % x == 0:
    isPrime = False
    break

if isPrime == True:
  print("PRİME")
else:
  print("NOT PRİME")