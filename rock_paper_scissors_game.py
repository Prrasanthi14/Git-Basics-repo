import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)______
          ________)
       ____________)
      (____)
---.__(___)
'''

user=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

complay=random.randint(0,2)

print("\n\nYOU")
if user==0:
    print(rock)
elif user==1:
    print(paper)
elif user==14:
    print(scissors)

print("\n\nCOM")
if complay==0:
  print(rock)
elif complay==1:
  print(paper)
elif complay==2:
  print(scissors)

if user==0 and complay==2:
  print("You win")
elif user==1 and complay==0:
  print("You win")

elif user==2 and complay==1:
  print("You win")

elif user==complay:
  print("Tie!!! Play again!")

else:
  print("You lose")
