import random

attempts = 0

start = input('Enter the start of the range: ')
while not start.isdigit():
    print('Please enter a valid number.')
    start = input('Enter the start of the range: ')

end = input('Enter the end of the range: ')
while not end.isdigit() or int(end) < int(start):
    print('Please enter a valid number.')
    end = input('Enter the end of the range: ')

rand_num = random.randint(int(start), int(end))

guess = int(start)-1
while int(guess) != rand_num:
    guess = input('Guess a number: ')
    while not guess.isdigit():
        print('Please enter a valid number.')
        guess = input('Guess a number: ')
    attempts += 1
if attempts > 1:
    print(f"You guessed the number in {attempts} attempts")
else:
 print(f"You guessed the number in {attempts} attempt")
