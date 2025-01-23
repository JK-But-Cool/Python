import random
def funny():
  flag = False
  guess = random.randint(1, 10)
  while flag == False:
    try:
      rando = int(input("guess my number, it's between 1-10: "))
    except:
      print(rando,"isn't a number, dude.")
    else:
      flag = True
      print("Your guess was", rando, "and the Random number was",guess)
      if(rando == guess):
        print("Good Guess, you are a Winner")
      elif(rando == guess - 1 or rando == guess + 1):
        print("Close but no Cigar")
        print(rando, "is one number away from", guess)
      else:
        print("Better Luck Next Time")
        print(rando, "is NOT equal to", guess)
      
funny()
