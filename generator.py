import os
import sys
import re
import random

global cwd
cwd = os.getcwd()

def write_all_templates():
    for i in range(1, 100):
        wholedeck = ["As", "Ah", "Ad", "Ac", \
             "Ks", "Kh", "Kd", "Kc", \
             "Qs", "Qh", "Qd", "Qc", \
             "Js", "Jh", "Jd", "Jc", \
             "Ts", "Th", "Td", "Tc", \
             "9s", "9h", "9d", "9c", \
             "8s", "8h", "8d", "8c", \
             "7s", "7h", "7d", "7c", \
             "6s", "6h", "6d", "6c", \
             "5s", "5h", "5d", "5c", \
             "4s", "4h", "4d", "4c", \
             "3s", "3h", "3d", "3c", \
             "2s", "2h", "2d", "2c"]

        random.shuffle(wholedeck)

        op_card1 = wholedeck.pop()
        op_card2 = wholedeck.pop()

        ip_card1 = wholedeck.pop()
        ip_card2 = wholedeck.pop()

        f_card1 = wholedeck.pop()
        f_card2 = wholedeck.pop()
        f_card3 = wholedeck.pop()

        t_card = wholedeck.pop()
        r_card = wholedeck.pop()

        dead_cards = [op_card1, op_card2, ip_card1, ip_card2, f_card1, f_card2, f_card3, t_card, r_card]

        f = open(cwd + "//slots//log" + str(i) + ".log", "w")
        f.write("PS Hand #" + str(i) + "\n")
        f.write("Seat 1: op ($10000 in chips)\n")
        f.write("Seat 2: ip ($10000 in chips)\n")
        f.write("ip: posts small blind $50\n")
        f.write("op: posts big blind $100\n")
        f.write("*** HOLE CARDS ***\n")
        f.write("Dealt to op [" + op_card1 + " " + op_card2 + "]\n")
        f.write("Dealt to ip [" + ip_card1 + " " + ip_card2 + "]\n")
        f.write(' '.join(dead_cards) + "\n")
        f.close()

def write_one_template(template_number):
    wholedeck = ["As", "Ah", "Ad", "Ac", \
            "Ks", "Kh", "Kd", "Kc", \
            "Qs", "Qh", "Qd", "Qc", \
            "Js", "Jh", "Jd", "Jc", \
            "Ts", "Th", "Td", "Tc", \
            "9s", "9h", "9d", "9c", \
            "8s", "8h", "8d", "8c", \
            "7s", "7h", "7d", "7c", \
            "6s", "6h", "6d", "6c", \
            "5s", "5h", "5d", "5c", \
            "4s", "4h", "4d", "4c", \
            "3s", "3h", "3d", "3c", \
            "2s", "2h", "2d", "2c"]

    random.shuffle(wholedeck)

    op_card1 = wholedeck.pop()
    op_card2 = wholedeck.pop()

    ip_card1 = wholedeck.pop()
    ip_card2 = wholedeck.pop()

    f_card1 = wholedeck.pop()
    f_card2 = wholedeck.pop()
    f_card3 = wholedeck.pop()

    t_card = wholedeck.pop()
    r_card = wholedeck.pop()

    dead_cards = [op_card1, op_card2, ip_card1, ip_card2, f_card1, f_card2, f_card3, t_card, r_card]

    f = open(cwd + "//slots//log" + str(template_number) + ".log", "w")
    f.write("PS Hand #" + str(template_number) + "\n")
    f.write("Seat 1: op ($10000 in chips)\n")
    f.write("Seat 2: ip ($10000 in chips)\n")
    f.write("ip: posts small blind $50\n")
    f.write("op: posts big blind $100\n")
    f.write("*** HOLE CARDS ***\n")
    f.write("Dealt to op [" + op_card1 + " " + op_card2 + "]\n")
    f.write("Dealt to ip [" + ip_card1 + " " + ip_card2 + "]\n")
    f.write(' '.join(dead_cards) + "\n")
    f.close()

#write_all_templates()
#write_one_template(13)

start = "Hand"
flop =  "FLOP"
turn =  "TURN"
river = "RIVER"
end =   "SUMMARY"
dealt = "Dealt"
collected = "collected"
seat = "Seat"

checks = "checks"
posts =  "posts"
calls =  "calls"
bets =   "bets"
raises = "raises"
folds =  "folds"
small_blind = "small"
big_blind = "big"

RED   = '\033[1;31m'
BLUE  = '\033[1;34m'
CYAN  = '\033[1;36m'
GREEN = '\033[0;32m'
RESET = '\033[0;0m'
BOLD    = '\033[;1m'
REVERSE = '\033[;7m'
GREY = '\033[1;30m'
YELLOW='\033[0;33m'
RESET= '\033[0m'

suit_club = '\u2663'
suit_diamond = '\u2666'
suit_heart = '\u2665'
suit_spade = '\u2660'

colors_on = 1
if colors_on:
    suit_club = GREEN + '\u2663' + RESET
    suit_diamond = BLUE + '\u2666' + RESET
    suit_heart = RED + '\u2665' + RESET
    suit_spade = GREY + '\u2660' + RESET

actions = []
actions.append(start)
actions.append(flop)
actions.append(turn)
actions.append(river)
actions.append(posts)
actions.append(calls)
actions.append(bets)
actions.append(raises)
actions.append(folds)
actions.append(checks)
actions.append(dealt)
actions.append(collected)

flop_table = ""
turn_table = ""
river_table = ""
hand_title = ""
hand_action = ""
hero_button = ""
villain_button = ""

def print_table(hand_title, hand_action):
    if skip_print:
        pass
    clearscreen()
    if incognito:
        print(villain_hand[1:-2] + villain_button + " " + str(vilbet) + " : " + str(herobet)  + " " +hero_button + hero_hand[1:-2])
        print("sum:" + str(pot) + " " +flop_table.rstrip()[1:-1] + turn_table.rstrip()[1:-1] + river_table[1:-2] + " " + hand_title)
    else:
        print(hand_title)
        print(villain_nickname + " "+ villain_button + " " + villain_hand)
        print("-----------------------------")
        print("     " + str(vilbet))
        print("")
        print("     " + flop_table.rstrip() + turn_table.rstrip() + river_table)
        print(" pot: " + str(pot))
        print("")
        print("     " + str(herobet))
        print("-----------------------------")
        print(hero + " " + hero_button + " " + hero_hand)
        print("")
        print(hand_action)
    dumb = input("]")

def clearscreen():
    if os.system('cls' if os.name == 'nt' else 'clear'):
        if not terminal_size:
            print("\n" * get_terminal_size().lines, end='')
        else:
            print("\n" * terminal_size, end='')

if os.name == 'posix':
    pass

def clearscreen():
    if os.system('cls' if os.name == 'nt' else 'clear'):
        if not terminal_size:
            print("\n" * get_terminal_size().lines, end='')
        else:
            print("\n" * terminal_size, end='')

pl = 0
history = []
index = 0

incognito = 0
if len(sys.argv) > 1:
    if sys.argv[1] == 'i':
        #incognito mode
        incognito = 1

hero = "ip"
hero_nickname = "ip"
villain = "op"
villain_nickname = "op"

chosen_file_number = random.randint(1, 100)
chosen_slot = cwd + "//slots//log" + str(chosen_file_number) + ".log"
f = open(chosen_slot,"r")

hand_lines = []
last_line = ""
counter_lines = 0   
for line in f:
    #print(line)
    history.append(line)
    last_line = line
    tokens = last_line.split()
f.close()

action_points = []
for current_line in history:
    tokens = current_line.split()
    for act in actions:
        if act in tokens and seat not in tokens:
            action_points.append(current_line)

#print(last_line)
#print(tokens[2])
flop_print = "*** FLOP **** [" + tokens[4] + " " + tokens[5] + " " + tokens[6] + "]"
#print(flop_print)
turn_print = "*** TURN **** [" + tokens[7] + "]"
#print(flop_print)
river_print = "*** RIVER **** [" + tokens[8] + "]"
summary = "*** SUMMARY ***"

print("hand #" + str(chosen_file_number))
print("villain (op): [" + tokens[0] + " " + tokens[1] + "]")
print("hero (ip): [" + tokens[2] + " " + tokens[3] + "]")
print(flop_print)
print(turn_print)
print(river_print)
print(summary)
print("last action point:")
print(action_points[-1])

#construct_table based on last action point - which cards to show. Then save to file

pot = 0
herobet = 0
vilbet = 0
pot_offset = 0
hand_title = ""
hero_hand = ""
villain_hand = ""
hand_title = ""
hand_action = ""
flop_table = ""
turn_table = ""
river_table = ""
hero_button = "D"
villain_button = ""
skip_print = 0
#clearscreen()
'''
if posts in current and villain in current and small_blind in current:
    villain_button = "D"
if posts in current and hero in current and small_blind in current:
    hero_button = "D"
'''



