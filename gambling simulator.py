import random
rarities = ('UR','SSR','SR','R','N')
rewards = ('Banana','Orange','Blueberry','Apple','Pineapple','Watermelon')
def draw(draws):
    pulls = []
    pull = []
    def dopull(rarity):
        pull.append(random.choice(rewards))
        pull = ' '.join(pull)
        pulls.append(pull)

    for i in range(draws):
        pull = []
        rarity = random.random()
        if rarity > 0.99:
            pull.append(rarities[0])
        elif rarity > 0.9:
            pull.append(rarities[1])
        elif rarity > 0.75:
            pull.append(rarities[2])
        elif rarity > 0.45:
            pull.append(rarities[3])
        else:
            pull.append(rarities[4])
        pull.append(random.choice(rewards))
        pull = ' '.join(pull)
        pulls.append(pull)
    print ("you got:")
    for idkwhatnamehtis in pulls:
        print(idkwhatnamehtis)
def numreal():
   flag = False
   while flag == False:
    try:
        x = int(input("how many draws doth thou request? "))
    except:
        print ("please only put a number, good sir.")
    else:
        flag = True
        return x
while True:
    numdraw = numreal()
    draw(numdraw)
            
