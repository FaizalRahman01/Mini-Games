win_list=[1,2,3,4,5,6,7,8,9,10]
for i in range(10):
  import random
  choices = ["stone", "paper", "scissors"]
  user = input("Enter stone, paper, or scissors: ")
  computer = random.choice(choices)
  print("Computer Choice",computer)
  if user == computer:
      print("Your Match is Tie 🤝 ")
      win_list[i]="Tie"
  elif(user=="stone"and computer =="scisors")or\
    (user=="paper" and computer =="stone")or\
    (user=="scissor" and computer =="paper"):
    print("🎉You Win🎉")
    win_list[i]="Win"
    #win_list.append("Win")
  else:
      print("Computer Win")
      win_list[i]="Loss"
     # win_list.append("Loss")
  #print("computer choice =",computer,"\nuser choice = ",user,)
  # win_list[i] 


print(win_list)
print("Win = ",win_list.count("Win"))
print("Tie = ",win_list.count("Tie"))
print("Loss = ",win_list.count("Loss"))
# print("Loss at index no. = ",win_list.index("Loss")+1)
# print("Tie at index no. = ",win_list.index("Tie")+1)
# print("Win at index no. = ",win_list.index("Win")+1)
print("If you want play again the Stone Paper sessiors game, so re run the code")
