import random

""" simulate monty hall problem """

# constans
PRIZES = [True, False, False]
results = {'Switch': [], 'Stay': []}

class Door():
    def __init__(self, isChosen, isPrize, isOpen):
        self.isChosen = False
        self.isPrize = isPrize
        self.isOpen = isOpen

    def open(isOpen=True):
        self.isOpen = isOpen

    def choose(isChosen=True):
        self.isChosen = isChosen
        
class Trial():
    def __init__(self, strategy):

        # initialize_doors
        self.doors = []
        for i in range(len(PRIZES)):
            self.doors.append(Door(False, PRIZES[i], False))
        random.shuffle(self.doors)

        self.choice = None
        self.strategy = strategy
        
    def make_initial_choice(self):

        # contestant chooses a door
        self.choice = random.randrange(3)
        doors[self.choice].choose()
        print("choice: ", self.choice)
        
    def monty_opens_a_goat_door(self):

        #monty chooses a random door that is not the prize
        montyDoorChoice = random.randrange(len(doors))
        while True:
            if not self.doors[montyDoorChoice].isPrize and \
               montyDoorChoice != self.choice
                break
            else:
                montyDoorChoice = random.randrange(len(doors))
        self.doors[montyDoorChoice].open()
            
        
    def decide_stay_or_switch(self):
        if self.strategy != 'Stay':
            self.choice = self.doors[self.choice
            
    
    def record_result(self):
        return
    
# main simulation
# takes an integer for number of trials and runs trials for each strategy
def simulate(n):
    for i in range(n):
        for strategy in results.keys():
            run_trial(strategy)

# runs a single game of monty hall
def run_trial(strategy):
    trial = Trial(strategy)
    trial.make_initial_choice()
    monty_removes_a_goat()
    decide_stay_or_switch()
    record_result()

# randomly select the initial prizes
def initialize_doors():
    doors = PRIZES[:]
    random.shuffle(doors)
    print(doors)
    

def make_initial_selection():
    return
def monty_removes_a_goat():
    return
def decide_stay_or_switch():
    return
def record_result():
    return

simulate(1)

    
        
    
    
