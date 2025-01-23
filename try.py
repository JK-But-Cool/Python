def main():
   flag = False
   while flag == False:
    try:
        x = int(input("give me your number, john: "))
    except:
        print ("john, that's not a number")
    else:
        print("wow john,",x,"is such an original number...")
        flag = True
main()
