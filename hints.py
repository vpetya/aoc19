import itertools

#In interactive mode, the last printed expression is assigned to the variable _

"".splitlines()

l = [int(x) for x in "2".split("\n")]

"".strip()
itertools.cycle(l)

# negative indexes
word ='Test'
word[-1]  # last character

#slicing
word[1:2]
print(word[:2] + word[2:] == word)
# last two character
print(word[-2:])

#multiple assignment
a, b = 1,2
a, b = b, a+b

#range
for i in range(0, 10, 3):
    print(i) 
#   0, 3, 6, 9

def f(x):
    """This is a python style function documentation"""
    return x/2

def fun(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    #standard python function definition


#list comprehensions
print([f(x) for x in {1,2,3}])
print([(a, b) for a in {1,2,3} for b in {1,2,3}])

#forelse
for i in range(1,10,2):
    if i%2 == 0:
        break
else:
    print("This is odd")

#unpack lists / tuples
args = [3, 6]
range(*args)

# unpack as named parameters (or formal parameters)
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
f(**d)

#lambda
lambda a, b: a+b