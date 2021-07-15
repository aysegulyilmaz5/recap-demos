n = int(input("Please enter number:"))


for row in range (1,n):
  for column in range(1,row+1):
    print("*",end = ' ')
  print("")