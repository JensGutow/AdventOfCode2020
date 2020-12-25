import time

class cup():
    def __init__(self, label):
        self.label=label
        self.next = None

class cupHandling():
    def __init__(self, s:str, n=0):
        self.move_no = 0
        self.current = None
        self.cups = {}
        self.highest = 0
        last_cup = None
        #labels
        for c in s:
            last_cup = self.addCup(int(c), last_cup)
        for i in range(len(s) + 1, max(n,len(s)) + 1):
            last_cup = self.addCup(i, last_cup)
        # next
        last_cup.next = self.current

    def addCup(self,label:int, vorgaenger:cup):
        self.cups[label] = cup_new = cup(label)
        if not self.current:
            self.current = cup_new
        self.highest = max(self.highest, label)
        if vorgaenger:
            vorgaenger.next = cup_new
        return cup_new

    def destination(self, selection):
        dest = self.current
        while True:
            new_label = dest.label - 1
            if not(new_label):
                new_label = self.highest
            dest = self.cups[new_label]
            if not dest.label  in [item.label for item in selection]:
                return dest

    def move(self):
        self.move_no += 1
        if self.move_no % 500_000 == 0:
            print("Nr:", self.move_no)
        sel = self.get_next_selection(self.current, 3)
        dest = self.destination(sel)
        self.move_sel(self.current,dest, sel[0], sel[-1])
        self.current = self.current.next

    def move_sel(self, von:cup, nach:cup, start:cup, end:cup):
        von.next = end.next
        temp = nach.next 
        nach.next = start
        end.next = temp

    def get_next_selection(self, vorgaenger:cup,n:int):
        selection = []
        for i in range(n):
            selection.append(vorgaenger.next)
            vorgaenger = vorgaenger.next
        return selection

    def lösung2(self):
        cup = self.cups[1].next 
        return cup.label * cup.next.label

    def lösung1(self):
        cup = self.cups[1].next 
        s = ""
        for i in range(len(self.cups)):
            s+=str(cup.label)
            cup = cup.next
        return s

    def __str__(self):
        n = min(20, len(self.cups))
        cup = self.current
        s="("+str(cup.label) + ") "
        while cup.next != self.current:
            cup = cup.next 
            s += str(cup.label) + " "
        return s

def löse(s, task2):
    ch = cupHandling(s, 1_000_000 if task2 else 0)    
    n = 10_000_000 if task2 else 100
    for _ in range(n):
        ch.move()
    return ch.lösung2() if task2 else ch.lösung1()
        
beispiel=("389125467")
task = "853192647"

print("Task 1")
start = time.perf_counter()
print(löse(task, False), time.perf_counter() - start)

print("Task 2")
start = time.perf_counter()
print(löse(task, True), time.perf_counter() - start)