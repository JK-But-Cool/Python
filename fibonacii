fido = [0, 1]
fido.append(1)
for i in range(len(fido)-1,12):
    fido.append(fido[i] + fido[i-1])
fidoex = [fido[-2],fido[-1]]
for i in range(len(fidoex)-1,12):
    fidoex.append(fidoex[i] + fidoex[i-1])
del (fidoex[0:2])
fido = fido + fidoex
print(fido)
