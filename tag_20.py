import time
from collections import deque
import math
from collections import defaultdict
from itertools import permutations

class tile():
    def __init__(self, s_input:str):
        zeilen = s_input.split("\n")
        self.id = int(zeilen[0].split()[1].replace(":",""))
        daten = zeilen[1:]
        oben = daten[0]
        unten = self.flip_int(daten[-1])
        rechts = links = ""
        for zeile in daten:
            rechts += zeile[-1]
            links = zeile[0] + links
        self.d = deque()

        self.d.append(oben)
        self.d.append(rechts)
        self.d.append(unten)
        self.d.append(links)   

        self.orientierung = 0     
        self.flip_state = 0

        self.borders = set()

        while True:
            for v in self.d:
                self.borders.add(v) 
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
        self.d.rotate()

    def flip_data(self):
        temp = self.d[1]
        self.d[1] = self.flip_int(self.d[3])
        self.d[3] = self.flip_int(temp)
        self.d[0] = self.flip_int(self.d[0])
        self.d[2] = self.flip_int(self.d[2])

    def flip(self):
        self.flip_state += 1
        self.flip_state %= 4
        if self.flip_state % 2 == 0:
            self.d.rotate()
        self.flip_data()
        if self.flip_state % 2 == 0:
            self.d.rotate(-1)

    def get_border(self,index):
        value = self.d[index]
        if index > 1:
            value = self.flip_int(value)
        return value
    
    @staticmethod
    def flip_int(s):
        return s[::-1]

    def __str__(self):
        s = "id:" + str(self.id)  + " orientierung:" + str(self.orientierung) + " flip_state:" + str(self.flip_state) + "\n" 
        s += "Daten (intern / get)\n"
        for i in range(4):
            s += str(self.d[i]) + "\t" + str(self.get_border(i)) + "\n"
        return s

def get_puzzle(file_name):
    p = []
    with open(file_name) as f:
        p = f.read().split("\n\n")
    return p

p = get_puzzle("tag_20.txt")

tiles = [tile(item) for item in p]

FOTO_DICT = {foto.id:foto for foto in tiles} # id -> foto

RichtungGegenseite = {0:2,1:3,2:0,3:1}
N = len(tiles)
DIM = int(math.sqrt(N))
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

borders = set()
for tile in tiles:
    borders = borders or tile.borders

NACHBAR_FOTOS = defaultdict(set)
for tile1, tile2 in permutations(tiles, 2):
    if tile1.id == tile2.id: continue
    if len(tile2.borders.intersection(tile1.borders))==0: continue
    s = (tile1.borders.union(tile2.borders))
    NACHBAR_FOTOS[tile1.id].add(tile2.id)
    NACHBAR_FOTOS[tile2.id].add(tile1.id)

ECKEN_TILES = [FOTO_DICT[id] for id in NACHBAR_FOTOS if len(NACHBAR_FOTOS[id]) == 2]
loesung1 = math.prod([tile.id for tile in ECKEN_TILES])
print("lösung1:",loesung1)

pass





MAX_LEN = 0

def check_next_id(loesung, foto1, dim):

    result = True
    # von aktueller Pos wird nur nach links und oben geprüft
    # wenn id=0 (links, oben) geprüft wird -> per default true
    id_next = len(loesung)
    moegliche_richtungen = PRUEF_RICHTUNGEN[id_next]
    zu_pruefende_richtungen = [0,3]
    id_offset = {0:-dim,1:1,2:dim,3:-1}
    for richtung in zu_pruefende_richtungen:
        if richtung in moegliche_richtungen:
            r1 = richtung 
            r2 = RichtungGegenseite[r1]
            id2 = id_next + id_offset[r1]
            foto2 = loesung[id2]
            result &=  foto1.get_border(r1) == foto2.get_border(r2)
            if not result: 
                break
            else:
                result = True
    return result

def next_foto(LOESUNG, FOTO_STACK, PRUEF_RICHTUNGEN, last_id):
    foto = None
    last_loesung_id = LOESUNG[-1].id 
    platz_next_foto = len(LOESUNG)

    richtungen_next_foto = set(PRUEF_RICHTUNGEN[platz_next_foto])
    


    return foto


def löse_rekursiv(loesung):
    global MAX_LEN
    if(len(loesung) > MAX_LEN):
        MAX_LEN = len(loesung)
        print(MAX_LEN)
    # Funktion wird mit leerer Liste aufgerufen -> es muss als erstes ein Foto geholt werden
    if loesung and (len(loesung) >= N):
        return True
    # hole nachstes Foto
    if not FOTO_STACK:
        print("Erorr: kein Foto mehr auf Stack, aktulle Lösungslänge=",len(loesung))
        return False

    foto = FOTO_STACK.popleft()
    id_foto = foto.id 
    loesungs_id = len(loesung) 
    # prufe ob foto passt -> wenn nicht drehe/flippe es solange, bis es passt, wenn nicht: nehme nächstes Foto bis Liste leer. wenn List leer -> return false
    check = False
    while not check:
        check = check_next_id(loesung, foto, DIM)
        if check: 
            ## wir haben eine passendes foto gefunden -> aktualisiere Loesungsmenge
            loesung.append(foto)
            # suche lösunge für alle weiteren Pläetze
            check = löse_rekursiv(loesung)
            if not check:
                # hat nicht geklappt -> entferne Foto -> suche weiteres foto
                loesung.pop()
        if not check:
            if not foto.shuffle():
                # alle shuffles durchprobiert -> kein Erfolg -> nächstes foto vom Stapel
                FOTO_STACK.append(foto)
                foto = next_foto(LOESUNG, FOTO_STACK, PRUEF_RICHTUNGEN, last_id)
                if not(foto):
                    #alle Bilder ausprobiert -> Bild wieder zurücklegen und False returnen
                    if foto.orientierung or foto.flip_state:
                        while foto.shuffle():
                            pass
                    FOTO_STACK.append(foto)
                    return False

    return check
MAX_LEN = 0
LEOSUNG.append(ECKEN_TILES[0])
FOTO_STACK.remove(ECKEN_TILES[0])
löse_rekursiv(LEOSUNG)
pass




if len(LEOSUNG) == N:
    print("prima")
    ecken_ids =[0, DIM-1, -DIM,-1]
    ecken_foto_ids = [LEOSUNG[id].id for id in ecken_ids]
    ergebnis = 1
    for id in ecken_foto_ids:
        ergebnis *= id
    print(ecken_foto_ids)
    print(ergebnis)









# t = tiles[0]
# print(t)
# print("rot")
# for _ in range(4):
#     t.rotate()
#     print(t)

# print("flip")
# for _ in range(4):
#     t.flip()
#     print(t)

# print("shuffle")
# while True:
#     s = t.shuffle()
#     print(t)
#     if not(s):
#         break
# print("\nTILES")
# for tile in tiles:
#     print(tile)

#print("Task 1")
start = time.perf_counter()
#print(löse(r,t), time.perf_counter() - start)

#print("Task 2")
start = time.perf_counter()
#print(löse(r,t), time.perf_counter() - start)