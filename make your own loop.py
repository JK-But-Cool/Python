def diy():
   print("i'm feelin lazy... you make the list for me.")
   flag = False
   while flag == False:
    try:
        star = int(input("what number do you wanna start on? "))
        en = int(input("what number do you wanna end on? "))
        incremen = int(input("what number do you wanna increment on? "))
    except:
        print ("cmon dude, numbers only...")
    else:
        flag = True
        if star > en and incremen > 0:
            print("you uh, can't increment through that pal...")
            flag = False
        else:
            for num in range(star,en,incremen):
                print(num)
diy()
