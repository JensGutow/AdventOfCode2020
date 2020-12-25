import time
from collections import deque
from itertools import permutations

def calc_dest_value(p,sel, start_value):
    d_value = start_value-1
    n=0
    while (d_value in sel and (n<2)) :
        d_value -= 1
    if not(d_value in p):
        d_value = max(p)
    return d_value
 
def iteration(p:deque, c_pos:int):
    c_pos %= len(p)
    p.rotate(-c_pos)
    sel = []
    for _ in range(3):
        v = p[1]
        sel.append(v)
        p.remove(v)
    d_value = calc_dest_value(p,sel,p[0])
    d_pos = p.index(d_value) + 1
    for i in range(3):
        p.insert(d_pos+i, sel[i])
    p.rotate(c_pos)

def sel_loesung1(p:deque):
    inx_1 = p.index(1)
    p.rotate(-inx_1)
    p.popleft()
    return p

beispiel=("389125467")
task = "853192647"
task2 = True

def create_puzzle(s, length):
    return deque(list(map(int,s)) + [i for i in range(len(s)+1, length+1)])
    

def löse(s, task2):
    l = 1_000_000 if task2 else len(s)
    p = create_puzzle(s, l)
    anz = 1_000 if task else 100
    for i in range(anz):
        iteration(p,i)

    if not task2:
        return sel_loesung1(p)

    

print(löse(beispiel, False))


#  for i in range(100):
#     iteration(p,i)
# print(p)
# sel_loesung1(p)
# print(p)




# for i in range(len(p)):
#     iteration(p,i)








#print("Task 1")
#start = time.perf_counter()
#print(löse(r,t), time.perf_counter() - start)

#print("Task 2")
#start = time.perf_counter()
#print(löse(r,t), time.perf_counter() - start)