def match(word):
    twos = False
    for idx1,c1 in enumerate(word):
        for idx2,c2 in enumerate(word):
            if idx1 == idx2 -1 and c1 > c2:
                return False
            if idx1 == idx2 -1 and c1 == c2 and (idx1 == 4 or word[idx1+2] != c1) and (idx1 == 0 or word[idx1-1]!=c1) :
                twos = True
    return twos

def match2(word):
    if sorted(word) != list(word):
        return False
    

test = [111111,223450,123789,288888,288899]
print([match(str(i)) for i in test])

print(len([i for i in range(278384,824795) if match(str(i))]))
