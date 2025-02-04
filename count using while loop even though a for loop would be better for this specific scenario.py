def main():

  print("Starting While Loop - Print Count Variable")
  flag = False
  while flag == False:
    try:
      nedemoji = int(input("number please: "))
    except:
      print ("TYPE A NUMBER!!!!!!!!!")
    else:
      flag = True
  nerdemoji = 0
    # Enter Your Code Here:
  while nerdemoji <= 9:
    print(nerdemoji)
    if(nerdemoji == nedemoji):
      print("hey wait a minute,",nedemoji,"is also your number!")
    nerdemoji += 1
  print("Ending While Loop")

main()
