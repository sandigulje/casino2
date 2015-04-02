from random import randint
secret= randint (1, 10)
print("Welcome to Casino!")
guess = 0
while guess != secret:
    g = raw_input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("Congratulations!")
        print("You win!")
    else:
        if guess < secret:
            print("To low")
        else:
            print("To high")
print("Game over!")