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

# read in the puzzle input by using regex
# puzzle structure: 
#   - each puzzle input row is a math. taks for example: ( 1 * 4 )
#   - each list entry: list of tupel of (Token, value) 
#       all Math. Operatores: Token->"OP"
#       Digits -> "D"
#       example: (1*4) -> [("OP", "("), ("O", 1), ("OP", "*"), ("O", "4"), ("OP", ")")]
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

# return a OP b (OP is in "*" or "+")
def calc(a, b, op):
    if op == "+": return a+b
    else        : return a*b

# solution for task 1 and 2 
# a prios dikctionary defined the operator priority : higher value <-> lower prority
def löse(p, prios):
    summe = 0
    value = 0
    for tokens in p:
        OPS = []    # stack for oparators: + * ( ) 
        NRS = []    # stack for numbers
        for token in tokens:
            # most simples rule: if a digit detect -> add to the number stack
            if token[0] == "D":
                NRS.append(token[1])
            else:
                op_new = token[1]
                if op_new in "*+":
                    # if a math. operator "received" 
                    # -> all previous operators (with "their" numbers paren) are processed.
                    # -> but only if the "worker op" has a higher priority value as the last received operatore
                    # (remember: higher priority value <-> lower math. priority)
                    # !!! indirect requirement: the priority of the brackets shall higher as the priority other OPs 
                    #   else error: calc will get the bracket.operator as input!
                    while OPS and prios[OPS[-1]] >= prios[op_new]:
                        NRS.append(calc(NRS.pop(), NRS.pop(), OPS.pop()))
                    OPS.append(op_new)
                elif  op_new == "(":
                    OPS.append(op_new)
                elif op_new == ")":
                    # resolving a received closed bracket -> dealing the stacks until a open is bracket detected
                    while OPS and OPS[-1] != "(":
                        NRS.append(calc(NRS.pop(), NRS.pop(), OPS.pop()))
                    OPS.pop()
                else:
                    print("ERRR", op_new)
        while(OPS):

            NRS.append(calc(NRS.pop(), NRS.pop(), OPS.pop()))
        summe += NRS[0]
    return summe

p = read_puzzle_input("tag_18.txt", )
print(löse(p, prios_1))
print(löse(p, prios_2))