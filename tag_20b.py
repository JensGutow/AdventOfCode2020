'''
https://adventofcode.com/2020/day/20
--- Day 20: Jurassic Jigsaw ---

The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...

By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....

For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171

To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

Your puzzle answer was 17032646100079.
--- Part Two ---

Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing them.

In the example above, the tiles become:

.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###

Remove the gaps to form the actual image:

.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###

Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   

When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image, after flipping and rotating it to the appropriate orientation, there are two sea monsters (marked with O):

.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#

Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a sea monster. In the above example, the habitat's water roughness is 273.

How many # are not part of a sea monster?

Your puzzle answer was 2006.

Both parts of this puzzle are complete! They provide two gold stars: **

At this point, you should return to your Advent calendar and try another puzzle.

==========================================================================================

Das hier ist die zweite Version.
In der ersten wurde ein rekursiver Tiefensuchalgorithmus verwendet.
Für den Beispieldatensatz war das noch in Ordnung. Für den Datensatz der Aufgabebe konnte aber keine Lösung ermittelt ewrden - 
der Algorithmus braucht zu lange.
Eine Analyse ergab, dass höchstens 10 Fotos richtig sortiert wurden - der Suchbaum ist zu gross und zu mächtig.
-> erstma Abbruch.

Zweiter Ansatz.
Grundlage sind die Mengen aller möglichen Foto-Kanten (orginal/gekippt) pro Bild.
Es wird nun nicht mehr blind ein (Foto)-Exemplar genommen. Vielmehr werden die Daten im Vorfeld vorbereitet.

Zwei Fotos werden als Nachbarn definiert, wenn es in den Mengen der Foto-Kanten der beiden Fotos Übereinstimmungen gibt 
(der Durchschnitt der Kanten-Mengen der beiden Fotos ist nicht leer).

In der finalen Version habe ich nicht nur die Kanten vewaltet - sondern die Gesamtheit der Bildaten.
Dies war für den Übergang zur Monstersuche (Task2) notwendig.
Hierfür wird numpy benutzt (Methoden für "schnelle" Matrix-Ops -> u.a. Rotation/Flipping.).

Von dieser Definition (der Nachbarkeits-Beziehung zwischen Fotos) ausgehend, werden zwei Verzeichnisse erstellt.
- Nachbarn: 
	- Schlüssel: Foto id
	- Wert: Liste aller Foto IDs, die bezüglich dem Schlüssel Nachbarn sind
- N_NACHBAR_FOTO_ID_DIR: 
	-Schlüssel:i (2,3,4)
	- Wert: Liste alle Fotos ids, bei denen die Menge der Nachbarn den Umfang "i" besitzt.
		-> N_NACHBAR_FOTO_ID_DIR[2] wäre dann die Liste aller Ecken (eine Ecke hat 2 Nachbarn)
	
Nun wird eine Lösungsliste aufgebaut.
Erste Iteration: NUR die Nachbarschaftsbeziehungen werden ausgwertet. Die Orientierung wird hier noch nicht betrachtet.
Start: lösung[0] := eine beliebige Ecke. ("links-oben")
Zeilenweise wird nun die Lösung aufgebaut.
Für den nächste freien Platz wird aus der Menge der noch zur Verfügung stehenden Fotos eins ausgewählt, unter Berücksichtigung:
- in der Lösung "links" und "oben" stehende Fotos sind Nachbarn für das neu einzufügende Foto
- dieses Foto hat genau so viele Nachbarn wie es seinen aktuellen Platz in der Lösungsmatrix entspricht.
	(in den Ecken -> 2, auf der Kante (und nicht der Ecke) -> 3, sonst -> 4)

In der zweiten Iteration wird die Orientierung der Fotos (Rotation/Flipping) betrachtet.
Ausgang: linke obere Ecke, und deren beiden Nachbarn.
Diese werde solange gedreht und geflippt, bis die Orientierung dieser drei Fotos korrekt ist (die Kantenbeziehungen dieser drei Fotos stimmen überein).

Nun wird vom zweiten Foto beginnend die Orientierung korrigiert.
Es wird ein Nachbar ausgewählt (linker oder oberer). Das aktuelle Foto wird so lange gedreht/geflippt, bis diese EINE Kantenbeziehungen übereinstimmt.

Zum Schluss wirde überpüft, ob alle Kantenbeziehungen aller Fotos zu allen Nachbarn ok sind.

Für die eigentlche Monstersuche muss zunächst ein "big_picture" aufgebaut werden (Ignorierung der Kanten der Orignal-Fotos).
In diesem "big_picture" wird nun das "monster" gesucht.
Auch hierfür werden Methoden aus dem Numpy-Modul verwendet.
Wenn die Suche nicht efolgreich war, wird rotiert/geflippt und die Suche wiederholt.
Wenn das Monster gefunden wurde, wird die "Gefährlichkeit des Gewässers" berechnet und zurück gegeben.
'''

import time
from collections import deque
import math
from collections import defaultdict
from itertools import permutations
import numpy as np

class tile():
    def __init__(self, s_input:str):
        zeilen = s_input.split("\n")
        dim = len(zeilen) - 1
        self.id = int(zeilen[0].split()[1].replace(":",""))
        self.matrix = np.array(list("".join(zeilen[1:]))).reshape(dim,dim)
        self.orientierung = 0     
        self.flip_state = 0
        self.borders = set()
        while True:
            for richtung in range(4):
                self.borders.add(self.get_border(richtung)) 
            self.flip()
            if not self.flip_state:
                break
    
    def shuffle(self):
        self.rotate()
        if self.orientierung == 0:
            self.flip()
        return (self.orientierung) or (self.flip_state)

    def rotate(self):
        self.orientierung += 1
        self.orientierung %= 4
        self.matrix = np.rot90(self.matrix,-1)

    def flip(self):
        self.flip_state += 1
        self.flip_state %= 4
        axis = 1 if self.flip_state % 2 == 0 else 0
        self.matrix = np.flip(self.matrix, axis=axis)

    def get_border(self,index):
        zeile = "".join(np.rot90(self.matrix, index)[0])
        if index > 1:
            zeile = self.flip_int(zeile)
        return zeile
   
    @staticmethod
    def flip_int(s):
        return s[::-1]

    def __str__(self):
        s = "id:" + str(self.id)  + " orientierung:" + str(self.orientierung) + " flip_state:" + str(self.flip_state) + "\n" 
        s += "Kanten \n"
        for i in range(4):
            s += str(self.get_border(i)) + "\n"
        return s

def get_puzzle(file_name):
    p = []
    with open(file_name) as f:
        p = f.read().split("\n\n")
    return p

file_name = "tag_20.txt"
print("Eingabe File:", file_name)
p = get_puzzle(file_name)

#startzeit für Lösung 1
start = time.perf_counter()

tiles = [tile(item) for item in p]

FOTO_DICT = {foto.id:foto for foto in tiles} # id -> foto

# 0(oben), 1(rechts), 2(unten) 3(links)
RichtungGegenseite = {0:2,1:3,2:0,3:1}
N = len(tiles)
DIM = int(math.sqrt(N))
'''
    Felder und mögliche Richtungen
        0, 2,..., 1*DIM - 1
        DIM,...,  2*DIM - 1
        :
        N-DIM,.., N-1

        konkret N=144 -> DIM=12
        0   ..  11
        12  ..  23
        :
        132 ..  143

        => Feld DIM-1 ist linke, obere Ecke -> mögliche Richtungen: links(3),unten(2)

    PRUEF_RICHTUNGEN: mögliche Richtungen für Feld i als Liste 
'''
#PRUEF_RICHTUNGEN[i] = [mögliche Richtungen des Feldes i]
PRUEF_RICHTUNGEN = defaultdict(list)
for i in range(N):
    if i >= DIM: PRUEF_RICHTUNGEN[i].append(0)          # oben = 0
    if i < (DIM-1)*DIM: PRUEF_RICHTUNGEN[i].append(2)   # unten = 2
    if i%DIM != 0: PRUEF_RICHTUNGEN[i].append(3)        # links = 3
    if i%DIM != (DIM-1):  PRUEF_RICHTUNGEN[i].append(1) #rechts = 1

FOTO_STACK = deque()
for foto in tiles:
    FOTO_STACK.append(foto)
LEOSUNG = []

# Gesamtheit aller Kanten aller Fotos bei allen Rotationen/Flipps
borders = set()
for tile in tiles:
    borders = borders or tile.borders

# jedes Foto (bestimmmt durch seine  ID) -> MENGE von passenden Nachbar-Fotos
#   Fotos sind passend, wenn es (mindestens) eine passende Kante bei beiden Fotos gibt (bei allen möglichen Kombis von Drehungen undFlips)
NACHBAR_FOTOS = defaultdict(set)
for tile1, tile2 in permutations(tiles, 2):
    if tile1.id == tile2.id: continue
    if len(tile2.borders.intersection(tile1.borders))==0: continue
    s = (tile1.borders.union(tile2.borders))
    NACHBAR_FOTOS[tile1.id].add(tile2.id)
    NACHBAR_FOTOS[tile2.id].add(tile1.id)

#Liste von Ecken-Fotos
ECKEN_TILES = [FOTO_DICT[id] for id in NACHBAR_FOTOS if len(NACHBAR_FOTOS[id]) == 2]

print("Task 1")
l1 = math.prod([foto.id for foto in ECKEN_TILES])
print(l1, time.perf_counter()-start)

#start für Lösung 2
print("Task 2")
start = time.perf_counter()

#-> allgemein: Dictonary: i -> set(fotos): i: Anzahl von Nachbarn -> value: Menge von Fotos, die i Nachbarn haben
N_NACHBAR_FOTO_ID_DIR = {} 
for i in range(2,5):
    foto_ids_with_n_nightbores =  {FOTO_DICT[id].id for id in NACHBAR_FOTOS if len(NACHBAR_FOTOS[id]) == i}
    N_NACHBAR_FOTO_ID_DIR[i] = foto_ids_with_n_nightbores

loesung = []
tile_0 = ECKEN_TILES[0]
#loesung : insert eine ECKE als start der lösung
loesung.append(tile_0)
# suche einen Stein für Platz 2, der
#   - richtige Anzahl von Richtungen hat
#   - gemeinsame Kante mit tile_0 hat

foto_ids_all = {tile.id  for tile in tiles if tile != loesung[0] } # initial: alle foto ids

# Erstelle losung mit Fotos auf den Plaetzen - unter Beachtung der Kantenbeziehung zwischen Nachbarn und 
# der  Anzahl der möglichen Nachbarn auf der Position
# Rotierung und Flipp - wird hier NICHT betrachtet.
for i in range(1,N):
    # mögliche Richtungen für platz i
    möglicheRichtungen = PRUEF_RICHTUNGEN[i]
    # hole linken und/oder oberen Nachbarn 
    nachbar_ids = []
    if 0 in möglicheRichtungen:
        nachbar_ids.append(i-DIM) # nach oben
    if 3 in möglicheRichtungen: # nach links
        nachbar_ids.append(i-1)
    n_richtungen = len(möglicheRichtungen)
    # Einschränken auf Nachbarn
    foto_ids = foto_ids_all
    for id in nachbar_ids:
        foto_ids = foto_ids.intersection(NACHBAR_FOTOS[loesung[id].id]) 
    # Einschränken auf Nachbar Anzahl
    foto_ids = foto_ids.intersection(N_NACHBAR_FOTO_ID_DIR[n_richtungen])
    #wähle ein beliebiges Foto raus 
    foto_id = foto_ids.pop()
    # vermindere die Menge der zur Verfügung stehenden ids um die ausgewählte id
    foto_ids_all.remove(foto_id)
    # Aktualisiere Lösungsmenge -> nächste Schleife oder Ende
    loesung.append(FOTO_DICT[foto_id])

# Drehe und Flippe jedes Teil so, dass alle Kantenbeziehungen i.o. sind
# sonderbehandlung des 1. Elements
# finde gemeinsame Kante zwischen der linken obren ecke, dem 2. item und dem item "unter" dem Eckteil
item_0 = loesung[0]
item_1 = loesung[1]
item_2 = loesung[DIM]
for shuffle_index in range(16*16*16):
    if (item_0.get_border(1) == item_1.get_border(3)) and (item_0.get_border(2) == item_2.get_border(0)):
        break
    item_0.shuffle()
    if  (shuffle_index % 16) == 0: item_1.shuffle()
    if  (shuffle_index % (16*16)) == 0: item_2.shuffle()

# erstes Element (unter anderem) ist richtig orientiert - nun der Reihe nach alle anderen
for i in range(1,N):
    # mögliche Richtungen für platz i
    möglicheRichtungen = PRUEF_RICHTUNGEN[i]
    # hole linken und/oder oberen Nachbarn 
    nachbar_ids = []
    if 0 in möglicheRichtungen:
        nachbar_ids.append((i-DIM, 0)) # nach oben
    if 3 in möglicheRichtungen: # nach links
        nachbar_ids.append((i-1,3))
    n_richtungen = len(möglicheRichtungen)
    # es sollte reichen, eine Kante auszurichten
    nachbar_id, richtung = nachbar_ids[0]
    # aktuelles Element so lange drehen/flippen, bis Nachbarbeziehung bzgl. Orientierung passt
    n_shuffle = 0
    foto1 = loesung[nachbar_id]
    foto2 = loesung[i]
    for n_shuffle in range(16):
        if foto2.get_border(richtung) == foto1.get_border(RichtungGegenseite[richtung]):
            break 
        foto2.shuffle()
    pass

# Prüfe alle Kanten-Beziehungen aller Elemente der Lösung
# sollte nun alles passen -> prüfe von allen Feldern alle Nachbarn die Kanten-Beziehungen (auch wenn jede Beziehung zweimal getesetet wird)
for i in range(N):
    offs = {0:-DIM, 1:1, 2:DIM,3:-1}
    möglicheRichtungen = PRUEF_RICHTUNGEN[i]
    item_0 = loesung[i]
    for r in möglicheRichtungen:
        id2 = i + offs[r]
        item_1 = loesung[id2]
        if item_0.get_border(r) != item_1.get_border(RichtungGegenseite[r]):
            print("FEHLER bei ids:",i, id2," Richtung:",r)

#########################################
# Bisher wurden nur die Ränder betrachtet und manipuliert
# Nun ist es Ziel, ausgehend von der Lösung ein grosses Array von Zeichen zu erhalten, in dem das Seemonster gesucht wird.
# Für die Manipulation und Generierung der Matrix wird das Modul numpy verwendet 
# - Funktionen zum Rotieren/Flippen
# - Funktionen zum Erzeugen / Ändern der internen Dimension / horizontales/vertikales Anhängen
# - shöne Übersicht: https://www.w3resource.com/numpy/manipulation/squeeze.php
# Das Seemonster wird als kleines numpy Array realisiert und dann im grossen Array gesucht.
#   diese Suche wird realisiert, indem ein kleines Sub-Array aus dem grossen geholt wird 

# Aufbau eines "grossen"-Lösungsarrays
def get_zeile(foto_array, start_id, zeile_in_matrix):
    zeile = np.array([])
    dim = int(math.sqrt(len(foto_array)))
    for foto_id in range(start_id, start_id + dim):
        zeile = np.hstack((zeile, foto_array[foto_id].matrix[zeile_in_matrix][1:-1])) 
    return zeile


def get_big_picture(foto_array):
    dim = int(math.sqrt(len(foto_array)))
    matrix_dim = len(foto_array[0].matrix)
    big_picture = np.array([])
    for dim_zeile in range(dim):
        start_foto_id = dim_zeile * dim
        for sub_zeile in range(1,matrix_dim-1):
            if not dim_zeile and not sub_zeile:
                big_picture_zeile = get_zeile(foto_array, start_foto_id, sub_zeile)
            elif not sub_zeile:
                continue
            else:
                big_picture_zeile = get_zeile(foto_array, start_foto_id, sub_zeile)
            big_picture =  np.concatenate((big_picture,big_picture_zeile)) if len(big_picture) else big_picture_zeile
    dim_big_pciture = int(math.sqrt(len(big_picture)))
    big_picture.reshape(dim_big_pciture, dim_big_pciture)
    return big_picture


class monstser_suche():
    def __init__(self, big_picture, monster, monster_dim):
        self.matrix = big_picture
        self.n1 = sum(np.char.count(self.matrix,"#"))
        self.n2 = monster.count("#")
        self.shuffle_status = 0
        self.dim = int(math.sqrt(len(self.matrix)))
        self.matrix = self.matrix.reshape(self.dim, self.dim)
        self.monster = np.array(list(monster.replace("\n",""))) == "#"
        self.monster.shape = monster_dim
        self.monster_dim = monster_dim

    def shuffle(self):
        self.shuffle_status += 1
        self.matrix = np.rot90(self.matrix)
        if self.shuffle_status % 4 == 0:
            self.matrix = np.flip(self.matrix, 0)
        if self.shuffle_status % 8 == 0:
            self.matrix = np.flip(self.matrix, 1)
            self.shuffle_status = 0

    def get_subarray(self, zeile,spalte):
        sa = np.array(["."]*self.monster_dim[0]*self.monster_dim[1])
        sa.shape = self.monster_dim
        for z in range(self.monster_dim[0]):
            for s in range(self.monster_dim[1]):
                sa[z,s] = self.matrix[z+zeile, s+spalte]
        return sa

    def find_monster(self):
        findings = []
        tiefe = None
        for zeile in range(0, self.dim - self.monster_dim[0]):
            for spalte in range(0, self.dim - self.monster_dim[1]):
                sub_arr = self.get_subarray(zeile,spalte) 
                sub_arr = sub_arr == "#"
                check = np.bitwise_and(sub_arr, self.monster)
                if (check == self.monster).all():
                    findings.append((zeile,spalte))
        tiefe = None if not findings else self.n1 - self.n2*len(findings)
        return tiefe

    def print_matrix(self):   
        for zeile in self.matrix:
            s = ""
            for c in zeile:
                s+=c
            print(s)


big_picture = get_big_picture(loesung)
monster = "                  # #    ##    ##    ### #  #  #  #  #  #   "

ms = monstser_suche(big_picture,monster, (3,20))

n = 0
while True:
    n += 1
    findings = ms.find_monster()
    if not findings:
        ms.shuffle()
        if n > 50:
            break
    else:
        break

print(findings, time.perf_counter()-start)