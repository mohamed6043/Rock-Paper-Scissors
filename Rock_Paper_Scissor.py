import random as rand
d = {"Rock": 1 , "Scissor": 2, "Paper": 3}
user = ''
while(user != 'E'):
  user = input("Please choose Rock, Paper, or Scissor or E to end game: ")
  try:
    ps = d[user.capitalize()]
    comp = rand.randint(1,3)
    print(comp)
    if ps == 1 and comp == 2:
      print("User wins with Rock, Computer loses with Scissor")
    elif ps == 2 and comp == 3:
      print("User wins with Scissor, Computer loses with Paper")
    elif ps == 3 and comp == 1:
      print("User wins with Paper, Computer loses with Rock")
    elif ps == 2 and comp == 1:
      print("Computer wins with Rock, User loses with Scissor")
    elif ps == 3 and comp == 2:
      print("Computer wins with Scissor, User loses with Paper")
    elif ps == 1 and comp == 3:
      print("Computer wins with Paper, User loses with Rock")
    else:
      print("Draw")

  except:
    print("Please enter a valid option")
