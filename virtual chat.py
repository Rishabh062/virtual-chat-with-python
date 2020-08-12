#Hello this is a simple program 
import time 

def myName():
  print("                 Chat!")

def welcome():
  print("      Welcome to a virtual chat")
  
def decorador(func):
  print("")
  print("-"*39)
  func()
  print("-"*39)
  print("")
  
decorador(welcome)
time.sleep(2)
decorador(myName)
time.sleep(1)
w="""
  ------------
  |Writing...|
  ------------
  """
print(w)
time.sleep(2)
print("Hello, My name is Rishabh Dwivedi ") 
time.sleep(1)
print(w)
time.sleep(3)
name = input("What's your name? ")
time.sleep(1)
print(w)
time.sleep(5)
print(f"Oh, Hi {name} nice to meet you!")
time.sleep(1)
print(w)
time.sleep(3.5)

f = input("How do you feel today? ")
time.sleep(1)
print(w)
time.sleep(3)
if (f=='fine')|(f=='good')|(f=='nice'):
  print("Oh, that's really good! ")
  
elif (f == "bad")|(f=='sad')|(f=='not nice'):
  print("Oh, that's not good ")
time.sleep(1)
print(w)
time.sleep(3)
age = int(input("How old are you my friend? "))
epoc = ""
if age < 25:
  epoc = "young"
elif age > 25 and age < 60:
  epoc = "adult"
elif age > 60 and age < 100:
  epoc = "old"
else:
  epoc = "very old"
time.sleep(1)
print(w)
time.sleep(5.5)
print(f"Oh {age} years old, you are {epoc} my friend!")
time.sleep(1)
print(w)
time.sleep(3)
print("I'm 19 years old")
time.sleep(1)
print(w)
time.sleep(6)
print("Sorry my friend, I have to go, see you later ")
