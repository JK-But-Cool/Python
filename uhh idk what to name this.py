def main():
  print("Starting Code Challenge")
  print("Starting While Loop")
    # Declare Any main() Variables - (Not Global)
    # Enter Your Code Here:
  flag = False
  while flag == False:
    try:
      grahh = int(input("FEED ME A NUMBER 20 OR GREATER: "))
    except:
      print ("THAT IS NOT A NUMBER, YOU PREPOSTEROUS FIEND!")
    else:
      if grahh >= 20:
        flag = True
        print("THANK YOU FOR THE NUMBER!")
      else:
        print(grahh,"IS NOT GREATER THAN 20, YOU UNINTELLIGENT DONUT!")
    hharg = 1
    while grahh > 1:
      print("YOUR NUMBER IS CURRENTLY",str(grahh)+"!")
      grahh = grahh / 2
      if hharg == 1:
        print("THE LOOP HAS RAN",hharg,"TIME!")
      else:
        print("THE LOOP HAS RAN",hharg,"TIMES!")
      hharg += 1
    else:
      print("YOUR NUMBER IS CURRENTLY",str(grahh)+"!")
      print("THE LOOP HAS RAN",hharg,"TIMES!")
    print("ENDING WHILE LOOP")
    print("ENDING CODE CHALLENGE")

main()
