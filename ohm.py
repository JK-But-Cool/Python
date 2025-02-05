print(ord('Ω'))
def diy():
   print("i'm feelin lazy... you make the list for me.")
   flag = False
   while flag == False:
    try:
        v = float(input("how much voltage do you have? "))
        i = float(input("how many amps do you want? "))
    except:
        print ("please only input numbers")
    else:
        flag = True
        o = v/i
        print("you will need a",str(o)+chr(937),"resistor")
diy()
