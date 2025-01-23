def epic():
  flag = False
  while flag == False:
    try:
      woah = int(input("put in a number: "))
      woah2 = int(input("put in another number: "))
    except:
      print("that's not a number jimbo.")
    else:
      flag = True
      if(woah>woah2):
        print(woah,"is greater than",woah2)
      elif(woah<woah2):
        print(woah,"is less than",woah2)
      else:
        print(woah,"is equal to",woah2)
epic()
