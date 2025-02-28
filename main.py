# for demo see https://appbrewery.github.io/python-day14-demo/
# outline:
# function to populate compare a to compare b
# input to accept user choice
# function to compare choice against correct answer. Tracks how many right answers. If right calls function below. If wrong, displays final score and game ends
# function to update compare fields

import game_data
import random

score = 0

def get_choices():
    choice_index = random.randint(1, 49)
    choice = game_data.data[choice_index]
    choice_to_list = []
    choice_to_list.append(choice["name"])
    choice_to_list.append(choice["follower_count"])
    choice_to_list.append(choice["description"])
    choice_to_list.append(choice["country"])
    return choice_to_list

def populate_compare(name, desc, country):
    print("Higher vs. Lower")
    print(f'Compare A: {name}, a {desc}, from {country}.')

def populate_against(name, desc, country):
    print("VERSUS")
    print(f'Against B: {name}, a {desc}, from {country}.')

def evaluate(choice_1, choice_2, guess, score):
    if choice_1[1] >= choice_2[1]:
        winning_answer = "A"
        winning_list = choice_1
    else:
        winning_answer = "B"
        winning_list = choice_2

    if guess == winning_answer:
        choice_1 = winning_list
        choice_2 = get_choices()
        score += 1
        gameplay(score)
    else:
        print("you lost!")
        print(f'Final score: {score}')

def gameplay(score):

    choice_2 = get_choices()

    populate_compare(choice_1[0], choice_1[2], choice_1[3])
    populate_against(choice_2[0], choice_2[2], choice_2[3])
    
    guess = input("Who has more followers? Type 'A' or 'B':  ")
    evaluate(choice_1, choice_2, guess, score)

choice_1 = get_choices()
gameplay(score)



    