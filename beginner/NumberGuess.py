import random
def guessing():
  num = random.randint(1,10)
  attempts = 0
  while True:
    
    guess = int(input("Guess(1-10) : "))
    attempts += 1
    
    if guess > num:
      print("Nope think lower")
    elif guess < num:
      print("Nope think higher")
    else:
      print(f"Correct!!!!!!!!! You took {attempts} attempts")
      break
    
guessing()
while True:
  a = input("Wanna play again (y/n) : ")
  if a == "y":
    guessing()
  else:
    break
