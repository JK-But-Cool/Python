import random
flag = False
while flag == False:
    try:
        your = int(input("gimme a number 0-9: "))
    except:
        print ("THAT'S NOT A NUMBER!!!!!")
    else:
        if 9 >= your >= 0:
            flag = True
        else:
            print("that number isn't between 0-9. you can try again though!")
fido = [random.randint(0, 9), your]
for i in range(len(fido)-1,12):
    fido.append(fido[i] + fido[i-1])
print(fido)
