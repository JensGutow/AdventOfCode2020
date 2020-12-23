import time
from collections import deque
import math

def get_puzzle(file_name):
    p = []
    with open(file_name) as f:
        decks = f.read().split("\n\n")
    for deck in  decks:
        d = deck.split("\n")
        p.append(deque(map(int, d[1:])))
    return p

def bewrte_deck(d):
    s = 0
    for i, k in enumerate(reversed(d)):
        s += (i+1)*k
    return s

def löse_rek(p, task2):
    h = set() #historie
    #print("game:",p)
    s1, s2 = p
    while True:
        if task2:
            tu = (tuple(s1.copy()),tuple(s2.copy()))
            if tu in h:
                #print("Loop detektiert -> S1 ist gewinner")
                #print(s1,s2)
                return True, s1 # spieler 1 gewinnt
            h.add(tu)
        k1 = s1.popleft()
        k2 = s2.popleft()
        k1_is_gewinner = True
        if task2 and (k1 <= len(s1) and k2 <=len(s2)):
            #print("Subgame ->")
            # erstelle neues spiel: ziehe soviele Karten, wie die aktuelle Karte anzeigt
            s1_new = deque([s1[x] for x in range(k1)])
            s2_new = deque([s2[x] for x in range(k2)])
            k1_is_gewinner, _ = löse_rek([s1_new, s2_new], task2)
            #print("<- Subgame: winner is:", "1" if k1_is_gewinner else "2" )
        else:
            k1_is_gewinner = k1 > k2
            #print("nromal cmp", "1" if k1_is_gewinner else "2" )
        if k1_is_gewinner:
            s1.append(k1)
            s1.append(k2)
        else:
            s2.append(k2)
            s2.append(k1)
        #print(s1, s2)
        if not(s2 and s1):
            s = s1 if s1 else s2
            return k1_is_gewinner, s

def löse(file_name, task2):
    p = get_puzzle(file_name)
    _, deck = löse_rek(p, task2)
    return bewrte_deck(deck)

file_name = "tag_22.txt"
print(file_name)
print("Task 1")
start = time.perf_counter()
print(löse(file_name, False), time.perf_counter() - start)

print("Task 2")
start = time.perf_counter()
print(löse(file_name, True), time.perf_counter() - start)