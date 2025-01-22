forward = input("what do you wanna spell backward? ")
backward = []
def main():
  for letter in forward:
    backward.append(letter)
  backward.reverse()
  backwardstring = ''.join(backward)
  print(backwardstring)
main()
  
