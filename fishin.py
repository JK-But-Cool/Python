def fish():
  print("type 1, or 2 for each option")
  rod, line, distance = input("do you want the premium or basic rod? "), input("do you want the strong or weak line? "), input("do you want to cast the line far, or close? ")
  if(rod == line == distance == "1"):
    print("you caught the LR super duper fish!!!")
  elif(rod == "1" and distance == "1"):
    print("you tried to catch the super duper fish, but your line was too weak.")
  elif(line == "1" and distance == "1"):
    print("you tried to catch the super duper fish, but your rod snapped in half.")
  elif(line == "1" and rod == "1"):
    print("you tried to catch the super duper fish, but your line didn't go far enough.")
  else:
    print("your rod was far too weak to catch the super duper fish.")
fish()
