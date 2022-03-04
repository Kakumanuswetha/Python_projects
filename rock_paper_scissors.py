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
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Welcome to rock,paper,scissors game!")
c=int(input("What do you wanna choose?\nEnter 0 for rock 1 for paper 2 for scissors:"))
co=random.randint(0,2)
if(c==0):
  print("\n",rock)
elif(c==1):
  print("\n",paper)
elif(c==2):
  print("\n",scissors)
print("\nComputer choose:")
if(co==0):
  print("\n",rock)
elif(co==1):
  print("\n",paper)
elif(co==2):
  print("\n",scissors)

if(c>co):
  print("You won!")
elif(c<co):
  print("OOps You loose")
else:
  print("Its a draw")
