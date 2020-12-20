import time
from collections import deque
import math
from collections import defaultdict

class tile():
    def __init__(self, s_input:str):
        zeilen = s_input.split("\n")
        self.id = int(zeilen[0].split()[1].replace(":",""))
        print(self.id)
        daten = zeilen[1:]
        oben = daten[1]
        unten = self.flip_int(daten[-1])
        rechts = links = ""
        for zeile in zeilen[1:]:
            rechts += zeile[-1]
            links = zeile[0] + links
        self.d = deque()

        self.d.append(oben)
        self.d.append(rechts)
        self.d.append(unten)
        self.d.append(links)   

        self.orientierung = 0     
        self.flip_state = 0
    
    def shuffle(self):
        self.rotate()
        if self.orientierung == 0:
            self.flip()
        return (self.orientierung<<2) + (self.flip_state)

    def rotate(self):
        self.orientierung += 1
        self.orientierung %= 4
        self.d.rotate()

    def flip_data(self):
        temp = self.d[1]
        self.d[1] = self.flip_int(self.d[3])
        self.d[3] = self.flip_int(temp)
        self.d[0] = self.flip_int(self.d[0])
        self.d[1] = self.flip_int(self.d[1])

    def flip(self):
        self.flip_state += 1
        self.flip_state %= 4
        if self.flip_state % 2 == 0:
            self.d.rotate()
        self.flip_data()
        if self.flip_state % 2 == 0:
            self.d.rotate(-1)

    def get(self,index):
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
            s += str(self.d[i]) + "\t" + str(self.get(i)) + "\n"
        return s

def get_puzzle(file_name):
    p = []
    with open(file_name) as f:
        p = f.read().split("\n\n")
    return p


class puzzle_itme():
    def __init__(self):
        self.tile = None



def löse(tiles):
    # d = defaultdict(list)
    # dim = math.sqrt(len(tiles))
    # for i in range(dim):
    #     if i > 9:
    #         d[i].append([])
    pass

p = get_puzzle("tag_20_short.txt")
tiles = [tile(itme) for itme in p]

def löse1(tiles):
    n = len(tiles)
    dim = int(math.sqrt(n))




t = tiles[0]
print(t)
print("rot")
for _ in range(4):
    t.rotate()
    print(t)

print("flip")
for _ in range(4):
    t.flip()
    print(t)

print("shuffle")
while True:
    s = t.shuffle()
    print(t)
    if not(s):
        break
print("\nTILES")
for tile in tiles:
    print(tile)








#print("Task 1")
start = time.perf_counter()
#print(löse(r,t), time.perf_counter() - start)

#print("Task 2")
start = time.perf_counter()
#print(löse(r,t), time.perf_counter() - start)