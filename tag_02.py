import time

def read_puzzle(datei):
  puzzle = []
  with open(datei) as f:
    for zeile in f:
      anzahlen, buchst, psw = zeile.split()
      mi, ma = [int(x) for x in anzahlen.split('-')]
      buchst = buchst[0]
      puzzle.append((mi,ma,buchst,psw))
  return puzzle    

def löse(puzzle):
  n = 0
  for min_, max_, buchst, psw in puzzle:
    if min_ <= psw.count(buchst) <= max_: n += 1
  return n   

def löse2(puzzle):
  n = 0
  for min_, max_, buchst, psw in puzzle:
    if (psw[min_-1]+psw[max_-1]).count(buchst) == 1: n += 1
  return n


puzzle = read_puzzle('tag_02.txt')

start = time.perf_counter()
print(löse(puzzle), time.perf_counter()-start)

start = time.perf_counter()
print(löse2(puzzle), time.perf_counter()-start)    