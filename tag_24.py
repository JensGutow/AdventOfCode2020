'''
https://adventofcode.com/2020/day/24#part2

TASK 1
The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. 
Not in the mood to wait, you offer to help figure out the pattern.

The tiles are all white on one side and black on the other. 
They start with the white side facing up. 
The lobby is large enough to fit whatever pattern might need to appear there.

A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). 
Each line in the list identifies a single tile that needs to be flipped by giving a series of steps 
starting from a reference tile in the very center of the room. (Every line starts from the same reference tile.)

Because the tiles are hexagonal, every tile has six neighbors: 
    east, southeast, southwest, west, northwest, and northeast. 

These directions are given in your list, respectively, 
    as e, se, sw, w, nw, and ne. 
A tile is identified by a series of these directions with no delimiters; for example, 
esenee identifies the tile you land on if you start at the reference tile and then move one tile east, 
one tile southeast, one tile northeast, and one tile east.

Each time a tile is identified, it flips from white to black or from black to white. 
Tiles might be flipped more than once. 
For example, a line like esew flips a tile immediately adjacent to the reference tile, 
and a line like nwwswee flips the reference tile itself.

--------------------------------------------------------------
Lösung:
- Koordinatensystem:
    - Die x-Achse ist identisch mit dem kartesischen System
    - Die y-Achse wird um 30 Grad nach links gedreht.
- Der Startpunkt ist (0,0)
- Mittelpunkte der Hexagons sind die Koordinaten.
- die sechs möglichen Richtungen werden als Deltas in das Koordinatensystem übersetzt (delta_x=+/-1, delta_y=+-1)
- Benutzt wird das Modul numpy (für Vector Operationen)
- Jede Zeile des Puzzles-Input wird in eine Liste von Vectoren übersetzt und anschliessend addiert.
- Das Ergebnis wird als Schlüsselwert für ein Verzeichnis benutzt -> um den Seitenzustand der Fliessen (shwarz/weiß) zu verwalten/speichern.
- zum Schluss wird die Anzahl der schwarzen Steine gezählt.

=========================================================
Task 2
=========================================================
The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

    Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.

Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

How many tiles will be black after 100 days?

--------------------------------------------------------------
Lösung:

- Nutze Counter aus Collections
- Arbeite "nur" auf schwarze Positionen -> eventuell weiße Steine werden VOR der Iteration gelöscht
- Nachbarbeziehung: wird via DELTAS.values() definiert
- Für alle schwarzen Steine wird der Counter-Value für seine Nachbarn hochgezhählt
    -> das ist zwar i.o. -> aber es werden damit "schwarze" Inseln "vergessen"
    -> also: der Counter muss für alle schwarzen Positionen mit 0 initialisiert werden
'''
import time
import numpy as np
from collections import Counter

RICHTUNGEN="e se sw w nw ne".split(" ")
DELTAS = {"e": np.array([1,0]),"se": np.array([0,-1]),"sw": np.array([-1,-1]),"w": np.array([-1,0]),"nw": np.array([0,1]),"ne": np.array([1,1])}

def parse_zeile(zeile):
    deltas = []
    zeile = list(zeile.strip())
    while len(zeile)>0:
        c = zeile.pop(0)
        if c not in RICHTUNGEN:
            c += zeile.pop(0)
        deltas.append(DELTAS[c])
    return deltas

def get_puzzle(file_name):
    d = []
    with open(file_name) as f:
        for zeile in f:
            d.append(parse_zeile(zeile))
    return d

def loesung_1(p):
    d = {}
    for item in p:
        hex = sum(item)
        koord = (hex[0], hex[1])
        v = d.get(koord, "white")
        d[koord] = "black" if v == "white" else "white"
    return d

def get_nr_black_tiles(d):
    return list(d.values()).count("black")

file_name = "tag_24.txt"
p = get_puzzle(file_name)
print(file_name)
print("Task 1")
d=loesung_1(p)
nr_black_tiles = get_nr_black_tiles(d)
print("Number of black tiles:", nr_black_tiles)

#task 2:

def del_white_tiles(d):
    del_keys = [k for k,v in d.items() if v!="black"]
    for k in del_keys:
        del d[k]

def iteration(p):
    # counter for all black items
    cnt = Counter()
    del_white_tiles(p)
    
    # init cnt for all black items
    for pos in p:
        cnt[pos] = 0

    # zähle "schwarze Nachbarn"
    for pos in p:
        for delta in DELTAS.values():
            pos_x = pos[0] + delta[0]
            pos_y = pos[1] + delta[1]
            cnt[(pos_x, pos_y)] += 1
    erg = p.copy()
    
    for cnt_pos, cnt_v in cnt.items():
        if cnt_pos not in erg: #white
            if cnt_v == 2:
                erg[cnt_pos] = "black"
        else: #black
            if (cnt_v == 0) or (cnt_v > 2):
                # flipp to white -> erase the black for erg
                del erg[cnt_pos]
    return erg
      
print("#TASK 2")
for i in range(100):
    d=iteration(d)
print("Number of black tiles after 100 iterations:",get_nr_black_tiles(d))