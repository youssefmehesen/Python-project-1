# That's a documentaion for my plan for that's project 
# Start the game 
# Ask the player to make a move (Rock(R),Paper(P),Scissors(S))
# Pc would select a move randomly 
# Pc == Player -> Tie
# (Player == P and Pc == R) OR (Player == R and Pc == S) OR (Player == S and Pc == P)
## Palyer won / You won
# Any other case 
## Pc won / You lost     
# Ask if the player wants to play again . then we play again

# That's Start for coding 
import random

# Ask the player to make a move (Rock(R),Paper(P),Scissors(S))
def get_user_choice():
  user = input("What's your choice? 'R' for Rock,'P' for Paper, and 'S' for Scissors\n")
# Enhancement From Chatgpt
  while user not in ['R', 'P', 'S']:
        print("Invalid choice. Please enter 'R' for Rock, 'P' for Paper, or 'S' for Scissors.")
        user = input("What's your choice? 'R' for Rock, 'P' for Paper, and 'S' for Scissors\n").upper()
  return user  
while True:
# Ask the player to make a move (Rock(R), Paper(P), Scissors(S))
       user = get_user_choice()

# Pc would select a move randomly 
       pc = random.choice(['R', 'P', 'S'])

#Some sort of  Interactivity here 
       print("User Played:" + user)
       print("PC Played:" + pc)

# Pc == Player -> tie 
       if user == pc:
              print("It's a tie")
       elif (user == 'P' and pc == 'R') or (user == 'R' and pc == 'S') or (user == 'S' and pc == 'P'):
              print("you won!")
       else:
              print("you lost")    
 # Ask if the player wants to play again
       play_again = input("Do you want to play again? (yes/no)\n").lower()
       if play_again != 'yes':
        break

print("Thanks for playing!")       