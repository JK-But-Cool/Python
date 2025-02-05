def main():
   flag = False
   while flag == False:
    try:
        food = int(input("i am hungry, feed me a number: "))
    except:
        print ("that's a string")
    else:
        if len(str(food)) > 10:
          print("that number is too big >:(")
        elif len(str(food)) < 5:
          print("that number is too small >:(")
        else:
          print("that number is very good, thank you")
          flag = True
main()
