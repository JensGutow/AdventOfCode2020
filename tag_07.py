import time
import re
from collections import defaultdict

class rule_item():
    def __init__(self, item):
        item = item.strip().split(" ")
        self.n = int(item[0])
        self.color = item[1] + " " + item[2]


def parse_line(line):
    #pale chartreuse bags contain 3 faded orange bags.
    line = line.replace(".", "")
    k,v = line.strip().split(" bags contain ")
    v = v.split(", ")
    values = []
    for v_item in v:
        if "no other" not in v_item:
            values.append(rule_item(v_item))
    return (k,values)
 
def get_puzzle(file_name):
    p = [] 
    with open(file_name) as f:
        for line in f:
            parse_result = parse_line(line)
            if parse_result:
                p.append(parse_result)
    return p

def build_child_parent_dir(puzzle):
    d=defaultdict(set)
    for (k,rule_items) in puzzle:
        for ri in rule_items:
            d[ri.color].add(k)
    return d

def build_parent_child_dir(puzzle):
    d={}
    for (k,rule_items) in puzzle:
        if rule_items:
            d[k] = rule_items
    return d

def get_cumm_bags_number(color, d):
    if color not in d:
        return 0
    else:
        n = 0
        rules = d[color]
        for rule in rules:
            n += (rule.n * (1 + get_cumm_bags_number(rule.color,d)))
        return n

puzzle = get_puzzle("tag_07.txt")
bag_is_contained_in = build_child_parent_dir(puzzle)
bag_contains = build_parent_child_dir(puzzle)
print(bag_contains)

bags_contains_shiny_gold = set(["shiny gold"])
n = -1
while True:
    n_new = len(bags_contains_shiny_gold)
    if n_new == n:
        break
    n = n_new
    temp_set = bags_contains_shiny_gold
    for color in temp_set:
        bags_contains_shiny_gold = bags_contains_shiny_gold.union(bag_is_contained_in[color])

print("Lösung1:", n-1)
print("Lösung2:", get_cumm_bags_number("shiny gold",bag_contains))



