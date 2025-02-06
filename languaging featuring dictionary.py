languages = {
  "es":"Hola",
  "fr":"Bonjour",
  "it":"Ciao",
  "jp":"Konichiwa",
  "cn":"Nǐ hǎo"
  }
def greet():
  name = input("What's your name? ")
  lang = input("What language do you speak? ")
  try:
    print(languages[lang],end='')
  except: 
    print("Hello,",name + "!")
  else:
    print(",",name + "!")
greet()
