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
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user = int(input("Make a choice :  0 for Rock , 1 For Paper , 2 For Scissors \n"))
if user == 0:
    user = "Rock"
    print ("User's choice : Rock")
    print(rock)
elif user == 1:
    user = "Paper"
    print ("User's choice : Paper")
    print(paper)
elif user == 2:
    user = "Scissors"
    print ("User's choice : Scissors")
    print(scissors)
else :
    print ("Invalid Choice")
Computer = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(Computer)
if computer_choice == "Rock":
    print ("Computer chose : Rock")
    print(rock)
elif computer_choice == "Paper":
    print ("Computer chose  : Paper")
    print(paper)
elif computer_choice == "Scissors":
    print ("Computer chose  : Scissors")
    print(scissors)
if user == computer_choice:
    print ("Draw")
if user == "Rock" and computer_choice == "Paper":
    print ("Computer Wins")
elif user == "Rock" and computer_choice == "Scissors":
    print ("User Wins")
elif user == "Paper" and computer_choice == "Rock":
    print ("User Wins")
elif user == "Paper" and computer_choice == "Scissors" :
    print ("Computer Wins")
elif user == "Scissors" and computer_choice == "Rock":
    print ("Computer Wins")
elif user == "Scissors" and computer_choice == "Paper":
    print ("User Wins")


