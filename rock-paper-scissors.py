#play command line Rock-paper-scissors
#by Manuel Folgar
import random 


choices = ("rock","paper","scissors")
user_choice = input( enter ("rock, paper or scissors"))
ai_response = random.choice(choices)
game = input("we will play rock paper scissors ill start, Rock")
game2 = input ("n scissors and shoot ") 

if user_choice == ai_response:
  print(f"we tied, Lets choose again") \
elif: \
(user_choice == "scissors"and ai_response == "scissors" ) or \
(user_choice == "rock" and ai_response =="rock") or \
(user_choice == "paper" and ai_response = ="paper" ) \
print("we drew") \
elif: \
(user_choice == "rock"  and ai_response == "scissors") or \
(user_choice == "paper" and ai_response == "rock") or \
(user_choice == "scissors" and ai_response == "paper") or \
print("you win") \
else: \
(user_choice == "paper" and ai_response = "scissors") or \
(user_choice == "rock" and ai_response = "paper") or \
(user_choice == "Scissors" and ai_response = "rock") \
print("You lose")



