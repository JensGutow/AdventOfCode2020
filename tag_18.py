import time
import re

#see Shunting-yard algorithm: https://en.wikipedia.org/wiki/Shunting-yard_algorithm
'''
Detailed example

Input: 3 + 4 × 2 ÷ ( 1 − 5 ) ^ 2 ^ 3

    Operator 	Precedence 	Associativity
    ^ 	4 	Right
    × 	3 	Left
    ÷ 	3 	Left
    + 	2 	Left
    − 	2 	Left 

The symbol ^ represents the power operator.

    Token 	Action 	Output
    (in RPN) 	Operator
    stack 	Notes
    3 	Add token to output 	3 		
    + 	Push token to stack 	3 	+ 	
    4 	Add token to output 	3 4 	+ 	
    × 	Push token to stack 	3 4 	× + 	× has higher precedence than +
    2 	Add token to output 	3 4 2 	× + 	
    ÷ 	Pop stack to output 	3 4 2 × 	+ 	÷ and × have same precedence
    Push token to stack 	3 4 2 × 	÷ + 	÷ has higher precedence than +
    ( 	Push token to stack 	3 4 2 × 	( ÷ + 	
    1 	Add token to output 	3 4 2 × 1 	( ÷ + 	
    − 	Push token to stack 	3 4 2 × 1 	− ( ÷ + 	
    5 	Add token to output 	3 4 2 × 1 5 	− ( ÷ + 	
    ) 	Pop stack to output 	3 4 2 × 1 5 − 	( ÷ + 	Repeated until "(" found
    Pop stack 	3 4 2 × 1 5 − 	÷ + 	Discard matching parenthesis
    ^ 	Push token to stack 	3 4 2 × 1 5 − 	^ ÷ + 	^ has higher precedence than ÷
    2 	Add token to output 	3 4 2 × 1 5 − 2 	^ ÷ + 	
    ^ 	Push token to stack 	3 4 2 × 1 5 − 2 	^ ^ ÷ + 	^ is evaluated right-to-left
    3 	Add token to output 	3 4 2 × 1 5 − 2 3 	^ ^ ÷ + 	
    end 	Pop entire stack to output 	3 4 2 × 1 5 − 2 3 ^ ^ ÷ + 		
'''

prios_1 = {"(":0,")":0,"+":1,"*":1}
prios_2 = {"(":0,")":0,"+":2,"*":1}

def read_puzzle_input(file_Name):
    p = []
    pattern = re.compile('\(|\)|\*|/|\+|\d+')
    pattern_d = re.compile("\d+")
    with open(file_Name) as f:
        for zeile in f:
            task = []
            z = zeile.strip()
            tokens = pattern.findall(z)
            for token in tokens:
                if pattern_d.match(token):
                    task.append(("D",int(token)))
                else:
                    task.append(("OP", token))
            p.append(task)
    return p

def calc(a, b, op):
    if op == "+" : 
        #("ADD", a, b)
        return a+b
    else: 
        #print("MULT", a, b)
        return a*b

def löse(p, prios):
    summe = 0
    value = 0
    for tokens in p:
        OPS = []
        NRS = []
        #print(tokens)
        for token in tokens:
            #print("T",token, " OPS:", OPS," NRS", NRS)
            if token[0] == "D":
                NRS.append(token[1])
            else:
                op_new = token[1]
                if op_new in "*+":
                    while OPS  and prios[OPS[-1]] >= prios[op_new]:
                        #print("calc")
                        NRS.append(calc(NRS.pop(), NRS.pop(), OPS.pop()))
                    OPS.append(op_new)
                elif  op_new == "(":
                    OPS.append(op_new)
                    #print("push (")
                elif op_new == ")":
                    while OPS and OPS[-1] != "(":
                        #print("calc -> )")
                        NRS.append(calc(NRS.pop(), NRS.pop(), OPS.pop()))
                    OPS.pop()
                else:
                    print("ERRR", op_new)
        while(OPS):
            #print("calc end")
            NRS.append(calc(NRS.pop(), NRS.pop(), OPS.pop()))
        summe += NRS[0]
    return summe
                

p = read_puzzle_input("tag_18.txt", )
print(löse(p, prios_1))
print(löse(p, prios_2))