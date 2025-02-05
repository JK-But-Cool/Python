flag = False
while flag == False:
  try:
      x = int(input("i got a cool number machine, put in a number between 0 and 255: "))
  except:
      print ("dude... that isn't even a number...")
  else:
      if x > 255 or x < 0:
        print("that number isn't in range...")
      else:
        flag = True
        print("your number is",bin(x),"in binary")
        print("your number is",hex(x),"in hexadecimal")
        print('your number represents',str(chr(x)),'in ASCII')
