import copy
import random
import time
from collections import Counter
# Consider using the modules imported above.

class Hat:

    def __init__(self,*args,**kwargs):
        self.contents = [x for x in kwargs.keys() for _ in range(kwargs[x])]

    def draw(self,number):
        if number >= len(self.contents):
            return self.contents
        drawed =random.sample(self.contents,number)
        [self.contents.remove(x) for x in drawed]
        return drawed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    good = 0
    for i in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        gotten = new_hat.draw(num_balls_drawn)
        good_gotten = Counter(gotten)
        is_good = True
        for x in expected_balls.keys():
            if x not in good_gotten or expected_balls[x]>good_gotten[x]:
                is_good = False
                break
        if is_good :
            good+=1
    return good/num_experiments
