
# Functions - Passing Arguments
print('''Functions - Passing Arguments
Learn more about Functions here:
https://www.w3schools.com/python/python_functions.asp
''')      
print('''
Challenge #1
Run this code
Run, then Edit the code in the template example:
      
Can you follow and explain
- How arguments are passed from the main code to the function?
- Can you explain how a value is 'returned'
      ''')
print('''
----------------------------------------------------
''')

def my_math(x,y) :
  z=x+y
  return z

def main():
  my_num_1 = 5
  my_num_2 = 2
  sum = my_math(my_num_1, my_num_2)
  print("The sum of", my_num_1, "+", my_num_2, "=",sum)

main()
# print('Done with Challenge 1')
print('''
----------------------------------------------------
''')

print('''
Challenge #2
Create a function that multiplies 2 numbers and returns the result
Enter Code Here:
----------------------------------------------------      ''')
# Enter Code Here:
def argh1(woah1, haow1):
  return woah1 * haow1
print(argh1(1, 2))
print('''
----------------------------------------------------
''')

print('''
Challenge #3
Create a function that adds 2 numbers and if the result is odd, adds 1, then returns the result
Enter Code Here:
----------------------------------------------------      ''')
# Enter Code Here:
def argh2(woah2, haow2):
  woah2haow2 = woah2 + haow2
  if woah2haow2 % 2 == 1:
    return woah2haow2 + 1
  else:
    return woah2haow2
print(argh2(4, 4))
print('''
----------------------------------------------------
''')
print('''
Challenge #4
Create a single function that takes the 2 argument numbers x,y 
and a 3rd argument, that selects between Addition, Subtraction, 
Multiplication, and Division, with the default being Addition. 
Then returns the result
Enter Code Here:
----------------------------------------------------      ''')
# Enter Code Here:
def argh3(woah3, haow3, uh):
  uh = uh.lower()
  match uh:
    case "subtraction":
      return woah3 - haow3
    case "multiplication":
      return woah3 * haow3
    case "division":
      return woah3 / haow3
    case _:
      return woah3 + haow3
print(argh3(5, 10, "division"))
print('''
----------------------------------------------------
''')
