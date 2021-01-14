# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_opponent_play,
          opponent_history=[],
          my_history = [],
          strategy = [0],
          play_order=[{
               "RR": 0,
               "RP": 0,
               "RS": 0,
               "PR": 0,
               "PP": 0,
               "PS": 0,
               "SR": 0,
               "SP": 0,
               "SS": 0,
           }]):

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}


    if not prev_opponent_play:
        prev_opponent_play = 'R'
        my_history.append('R')
    opponent_history.append(prev_opponent_play)

    last_two = "".join(my_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    n = 2
    last_my_history = my_history[-n:]
    last_opponent_history = opponent_history[-n:]
    am_i_winning = 0
    if len(opponent_history) >= n:
        for i in range(n):
            if last_my_history[i]=='R' and last_opponent_history[i]=='S' or\
                last_my_history[i]=='S' and last_opponent_history[i]=='P' or\
                last_my_history[i]=='P' and last_opponent_history[i]=='R':
                am_i_winning +=1
            elif last_my_history[i] != opponent_history[i]:
                am_i_winning -=1
    if am_i_winning < 0:
        strategy[0]+=1
        strategy[0]=(strategy[0]%4)
    prediction = ideal_response[my_history[-1]]
    if strategy[0]==1 and len(opponent_history) >=2:
        choices = ["R", "R", "P", "P", "S"]
        last_two = opponent_history[-2:]
        for i in range(len(choices)):
            if choices[i]==last_two[0] and choices[(i+1)%len(choices)]==last_two[1]:
                prediction = choices[(i+2)%len(choices)]
    if strategy[0]==2:
        last_ten = my_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)

        if most_frequent == '':
            most_frequent = "S"
        prediction = ideal_response[most_frequent]

    if strategy[0]==3:
        potential_plays = [
            my_history[-1] + "R",
            my_history[-1] + "P",
            my_history[-1] + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }

        prediction = ideal_response[max(sub_order, key=sub_order.get)[-1:]]


    result = ideal_response[prediction]
    my_history.append(result)
    return result
