# for demo see https://appbrewery.github.io/python-day14-demo/
# Compare A: Ellen DeGeneres, a Comedian, from United States
# outline:
# function to populate compare a to compare b
# input to accept user choice
# function to compare choice against correct answer. Tracks how many right answers. If right calls function below. If wrong, displays final score and game ends
# function to update compare fields
import game_data
import random

print(len(game_data.data))
print("########")


def get_choices():
    choice_index = random.randint(1, 50)
    choice = game_data.data[choice_index]
    choice_to_list = []
    choice_to_list.append(choice["name"])
    choice_to_list.append(choice["follower_count"])
    choice_to_list.append(choice["description"])
    choice_to_list.append(choice["country"])
    print(choice_to_list)
    return choice_to_list

def populate_choices():
    print("Higher vs. Lower")
    print(f'Compare A: {choice_to_list[0]}')
    #print("Versues")
    #print(f'Against B: {second}')
    
choice_1 = get_choices()

#populate_choices(apples, bananas)

#input(f'Who has more followers? Type A or B')

get_choices()
print("######")
print(choice_1)