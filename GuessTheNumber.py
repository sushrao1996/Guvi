from random import randint
c=0
p=0
while c<3 and p<=9:
    guess=randint(0,20)
    n=int(input("Guess the number: "))
    if n==guess:
      print("Wow! You guessed it right")
      p+=1
    else:
      print("Sorry! Better luck next time")
      print("The number was",guess)
      print(2-c,"lives more...")
      c=c+1
if c==3:
  print("GAME OVER")
if p==10:
  print("YOU WON!!!")

