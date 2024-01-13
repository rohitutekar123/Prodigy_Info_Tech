import random

def guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Advanced Guessing Game! Try to guess the secret number between 1 and 100.")

    while not guessed_correctly:
        try:
            # Get user input
            user_input = input("Enter your guess (or 'exit' to quit): ")

            if user_input.lower() == 'exit':
                print(f"Sorry to see you go! The correct number was {secret_number}.")
                break

            user_guess = int(user_input)
            
            # Increment the attempts
            attempts += 1
            
            # Compare the user's guess with the secret number
            if user_guess == secret_number:
                guessed_correctly = True
            elif user_guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if guessed_correctly:
        # Display the results
        print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")

# Run the game
guessing_game()
