def other():
  flag = False
  while flag == False:
    try:
      x = int(input("value 1: "))
      y = int(input("value 2: "))
    except:
      print("that's not a number jimbo.")
    else:
      flag = True
      print(x==y,x!=y,x>y,x>=y,x<y,x<=y,x is y, x is not y)
other()
