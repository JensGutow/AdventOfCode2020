import time
import re

def get_puzzle(file_name):
    d = {}
    with open(file_name) as f:
        rules, tests = f.read().replace("\"","").split("\n\n")
    tests = tests.split()
    for rule in rules.split("\n"):
        id, items = rule.split(":")
        d[id] = items.split()
    return d, tests

def make_regex(rules, cmd, regex):
    nrs = rules[cmd]
    result = "("
    for sub_cmd in nrs:
        if sub_cmd  == "|":     result += ")|("
        elif sub_cmd in "ab":  result += sub_cmd
        else:  result += "(" + make_regex(rules, sub_cmd, regex) + ")"
    result += ")"
    result = result.replace("(a)","a").replace("(b)","b")
    return result

def löse(rules, text):
    p = re.compile(make_regex(r,"0",""))
    n = 0
    for z in text:
        m = re.match(p,z)
        if  m and len(z) == len(m.group()):
            n+=1
    return n

r,t = get_puzzle("tag_19.txt")

print("Task 1")
start = time.perf_counter()
print(löse(r,t), time.perf_counter() - start)

print("Task 2")
n_max = 15
s_42 = "42 "
s_31 = "31 "
ds_08 = s_42
ds_11 = s_42 + s_31
for i in range(2,10):
    ds_08 += "| " + s_42*i
    ds_11 += "| " + s_42*i + s_31*i
r["8"] = ds_08.strip().split()
r["11"] = ds_11.strip().split()

start = time.perf_counter()
print(löse(r,t), time.perf_counter() - start)