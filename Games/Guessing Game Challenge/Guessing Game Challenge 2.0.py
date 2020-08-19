from random import randint

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

rand_num = randint(0, 100)
print(rand_num)

how_close_list = [0]

# cleaned up solution
while True:
    guess = int(input("Enter a Guess: "))

    if guess > 100 or guess < 0:
        print('OUT OF BOUNDS!')
        continue

    how_close = abs(guess - rand_num)
    how_close_list.append(how_close)

    if how_close == 0:
        print(f"You've guessed correctly, in {len(how_close_list)} guesses")
        break

    if how_close_list[-2]:
        prev_close = how_close_list[-2]
        curr_close = how_close_list[-1]

        if curr_close < prev_close:
            print("Warmer")
        elif curr_close > prev_close:
            print("Colder")
        elif curr_close == prev_close:
            print("Same Guess")  # not exactly needed
        else:  # we've guessed, don't need to print anything
            pass
    else:
        if how_close <= 10 and how_close > 0:
            print("Warm")
        else:
            print("Cold")