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
    return x/2


#list comprehensions
print([f(x) for x in {1,2,3}])
print([(a, b) for a in {1,2,3} for b in {1,2,3}])