import random
print("let's play rock-paper-scissors")
print("its a best of three")
def game():
    user_wins = 0
    computer_wins = 0
    for index in range(3):
        user_input = input("type 'r' for rock, 'p' for paper and 's' for scissors: ")
        computer_input = random.choice(['r','p','s'])
        if(user_input == 'r' or user_input == 'p' or user_input == 's'):
            print(f'the computer chose {computer_input}')
            if(user_input == computer_input):
                print("no one gets a point")
            elif(user_input == 'r' and computer_input == 'p'):
                print("computer gets a point")
                computer_wins += 1
            elif(user_input == 'r' and computer_input == 's'):
                print("user gets a point")
                user_wins += 1
            elif(user_input == 'p' and computer_input == 's'):
                print("computer gets a point")  
                computer_wins += 1
            elif(user_input == 'p' and computer_input == 'r'):
                print("user gets a point")  
                user_wins += 1
            elif(user_input == 's' and computer_input == 'r'):
                print("computer gets a point")  
                computer_wins += 1
            elif(user_input == 's' and computer_input == 'p'):
                print("user gets a point")     
                user_wins += 1   
        else:
            print("invalid input")        
    if(computer_wins > user_wins):
        print("you lose :(")
    elif(user_wins > computer_wins):
        print("you win :)")
    else:
        print("it's a draw -_-")
game()








    

