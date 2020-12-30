import time
import math

def read_puzzle(datei):
  with open(datei) as f:
    return [zeile.strip() for zeile in f]

def löse(puzzle, dx, dy):
  x = y = 0
  maxX, maxY = len(puzzle[0]), len(puzzle)
  n = 0
  while True:
    x, y = x + dx, y + dy
    if y >= maxY:
      return n
    if puzzle[y][x % maxX] == '#':
      n += 1

puzzle = read_puzzle('tag_03.txt')

print("Task 1")
start = time.perf_counter()
print(löse(puzzle, 3, 1), time.perf_counter() - start)

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

print("Task 2")
start = time.perf_counter()
lösung = 1
for dx, dy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
  lösung *= löse(puzzle, dx, dy)
print(lösung, time.perf_counter() - start)