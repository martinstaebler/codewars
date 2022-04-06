# https://www.codewars.com/kata/57e141ad8a8b8d4d150004f6
from random import randint
def r_p_s_cheat(choice):  
    return {"paper": "rock", "scissors": "paper", "rock": "scissors"}[choice] if (randint(0, 100) > 89) else {"rock": "paper","paper": "scissors","scissors": "rock"}[choice]


def r_p_s_cheat(choice):
    options = { "rock": "paper", "paper": "scissors", "scissors": "rock" }
    return options[choice] if random.randint(1, 10) <= 9 else options[options[choice]]

def r_p_s_cheat(ch):
    return ("rock", "paper", "scissors")[("rps".index(ch[0]) + 1 + (rand() > 0.9)) % 3]