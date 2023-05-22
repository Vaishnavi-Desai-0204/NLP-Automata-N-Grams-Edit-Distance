
import random

def create_automata(option):
    if option == 1:
        transitions = {
            0: {'b': 1},
            1: {'a': 2},
            2: {'a': 3},
            3: {'a': 3}
        }
        final_states = {3}
    elif option == 2:
        transitions = {
            0: {'a': 1 , 'b' : 2},
            1: {'b': 3 },
            2: {'a': 4},
            3: {'b' : 5},
            4: {'a': 6},
            5: {'a': 7 },
            6: {'b' : 8},
            7: {'a': 1 },
            8: {'b': 2}
        }
        final_states = {7,8}
    elif option == 3:
        transitions = {
            0: {'one': 2 , 'two' : 2, 'three' : 2, 'four' : 2, 'five' : 2, 'six' : 1, 'seven' : 2, 'eight' : 2, 'nine' : 2,'ten' : 2, 'eleven' : 2,'twelve' : 2,'thirteen' : 2,'fourteen' : 2,'fifteen' : 2,'sixteen' : 2,'seventeen' : 2,'eighteen' : 2,'nineteen' : 2, 'twenty': 1,'thirty': 1,'fourty': 1,'fiftey': 1,'sixty': 1,'seventy': 1,'eighty': 1,'ninety': 1},
            1:{'one': 1 , 'two' : 1, 'three' : 1, 'four' : 1, 'five' : 1, 'six' : 1, 'seven' : 1, 'eight' : 1, 'nine' : 1},
            2:{'':2}
        }
        final_states = {0,1,2}
    else:
        print("Invalid option.")
        return None

    automata = {'transitions': transitions, 'final_states': final_states}
    return automata

import random

def generate_language(automata):
    current_state = 0  # initialize the current state to the initial state
    word = ""  # initialize an empty word/utterance
    random_bool = False
    while True:
        # randomly choose a symbol from the set of possible symbols for the current state
        symbols = list(automata["transitions"][current_state].keys())
        if not symbols:
            break
        symbol = random.choice(symbols)
        
        # add the chosen symbol to the word/utterance
        word += symbol
        
        # update the current state based on the chosen symbol
        current_state = automata["transitions"][current_state][symbol]
        
        # check if the current state is an accepting state and ransom choice is true
        random_bool = random.choice((True, False))
        if current_state in automata["final_states"] and random_bool == True:
            break
    
    return word


def recognize_language(automata, utterance):
        current_state = 0  # initialize the current state to the initial state
        accept = 0
        words = utterance.split()
        t = 0
        
        for w in words:
            
            if w not in automata["transitions"][current_state]:
                 for symbol in utterance:        
                    if symbol not in automata["transitions"][current_state]:
                        return 0  # reject if there is no transition for the current symbol
                    current_state = automata["transitions"][current_state][symbol]  # update the current state based on the transition
                        
                 if current_state in automata["final_states"]:
                    return 1
                
            current_state = automata["transitions"][current_state][w] 
            
        if current_state in automata["final_states"]:
            return 1

        return accept














