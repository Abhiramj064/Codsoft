import random

def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ")
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Choose rock, paper, or scissors: ")
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return 'You win!'
    else:
        return 'Computer wins!'

def print_result(user_choice, computer_choice, result):
    print(f'You chose {user_choice.capitalize()}.')
    print(f'Computer chose {computer_choice.capitalize()}.')
    print(result)

def play_game():
    user_score = 0
    computer_score = 0
    print("WELCOME TO THE GAME OF ROCK PAPER AND SCISSORS!!!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, result)

        if 'You win' in result:
            user_score += 1
        elif 'Computer wins' in result:
            computer_score += 1

        print(f'Score - You: {user_score}, Computer: {computer_score}')

        play_again = input('Do you want to play again?(1/0): ')
        if play_again != '1':
            print('Thanks for playing!')
            break

if __name__ == "__main__":
    play_game()
