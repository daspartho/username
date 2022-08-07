import json
import random

def random_noun():
    with open('noun.json', 'r') as f:
        noun_list = json.load(f)
    return random.choice(noun_list)

def random_adj():
    with open('adj.json', 'r') as f:
        adj_list = json.load(f)
    return random.choice(adj_list)

if __name__== '__main__':
    print(random_adj()+random_noun())