# import needed modules
import random
# Welcome To The Game
print("Welcome To The Guessing Game✨✨")
choose_level = input("Choose How The Game Is Going to be (hard(h) - medium(m) - easy(e) >> ").lower()
print("Let's Get Started:)")
number = 0
high_num = 0

if choose_level == "h":
    high_num = 100
    number = random.randint(0, high_num)
elif choose_level == "m":
    high_num = 50
    number = random.randint(0, high_num)
else:
    high_num = 10
    number = random.randint(0, high_num)

run = True
while run:
    user_input = input(f"Choose Number Between 0 and {high_num} >> ")
