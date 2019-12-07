import itertools
from collections import deque

program = [3,8,1001,8,10,8,105,1,0,0,21,38,63,76,89,106,187,268,349,430,99999,3,9,1001,9,5,9,102,3,9,9,1001,9,2,9,4,9,99,3,9,101,4,9,9,102,3,9,9,101,4,9,9,1002,9,3,9,101,2,9,9,4,9,99,3,9,101,5,9,9,1002,9,4,9,4,9,99,3,9,101,2,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,5,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99]



def runComputer(arr,inputStack,output, initCounter = 0):
    counter = initCounter
    while True:
        inst = arr[counter]
        code = int(str(arr[counter])[-2:])
        if code == 99:
            return -1
        elif code == 1:
            #add
            step = 4
            p1 = arr[counter+1] if len(str(inst)) > 2 and int(str(inst)[-3]) else arr[arr[counter+1]]
            p2 = arr[counter+2] if len(str(inst)) > 3 and int(str(inst)[-4]) else arr[arr[counter+2]]
            arr[arr[counter+3]] = p1+p2
        elif code == 2:
            #multiply
            step = 4
            p1 = arr[counter+1] if len(str(inst)) > 2 and int(str(inst)[-3]) else arr[arr[counter+1]]
            p2 = arr[counter+2] if len(str(inst)) > 3 and int(str(inst)[-4]) else arr[arr[counter+2]]
            arr[arr[counter+3]] = p1*p2
        elif code == 3:
            #read
            step = 2
            if len(inputStack) == 0:
                #halt
                return counter
            arr[arr[counter+1]] = inputStack.pop()
        elif code == 4:
            #write
            step = 2
            p1 = arr[counter+1] if len(str(inst)) > 2 and int(str(inst)[-3]) else arr[arr[counter+1]]
            output.append(p1)
        elif code == 5:
            # jump if true
            p1 = arr[counter+1] if len(str(inst)) > 2 and int(str(inst)[-3]) else arr[arr[counter+1]]
            p2 = arr[counter+2] if len(str(inst)) > 3 and int(str(inst)[-4]) else arr[arr[counter+2]]
            if p1 != 0:
                step = 0
                counter = p2
            else:
                step = 3
        elif code == 6:
            # jump if false
            p1 = arr[counter+1] if len(str(inst)) > 2 and int(str(inst)[-3]) else arr[arr[counter+1]]
            p2 = arr[counter+2] if len(str(inst)) > 3 and int(str(inst)[-4]) else arr[arr[counter+2]]
            if p1 == 0:
                step = 0
                counter = p2
            else:
                step = 3
        elif code == 7:
            # less than
            step = 4
            p1 = arr[counter+1] if len(str(inst)) > 2 and int(str(inst)[-3]) else arr[arr[counter+1]]
            p2 = arr[counter+2] if len(str(inst)) > 3 and int(str(inst)[-4]) else arr[arr[counter+2]]
            arr[arr[counter+3]] = 1 if p1 < p2 else 0
        elif code == 8:
            # equals
            step = 4
            p1 = arr[counter+1] if len(str(inst)) > 2 and int(str(inst)[-3]) else arr[arr[counter+1]]
            p2 = arr[counter+2] if len(str(inst)) > 3 and int(str(inst)[-4]) else arr[arr[counter+2]]
            arr[arr[counter+3]] = 1 if p1 == p2 else 0
        counter+=step


#config = [0,1,2,3,4] #21860
config = [5,6,7,8,9]
def runConfig(conf):

    amplifiers = [{'memory':program[:],'inputStack':deque([i]),'output':[], 'counter':0} for i in conf]
    amplifiers[0]['inputStack'].appendleft(0)

    nextAmp = 0
    while amplifiers[4]['counter']!=-1:
        #while the last unit runs
        amp = amplifiers[nextAmp%5]
        counter = runComputer(amp['memory'],amp['inputStack'],amp['output'],amp['counter'])
        #copy the outputs
        for o in amp['output']:
            amplifiers[(nextAmp+1)%5]['inputStack'].appendleft(o)
        amp['output'].clear()
        #status
        amp['counter'] = counter
        nextAmp+=1
    return amplifiers[0]['inputStack'].pop()

maxOut = 0
for conf in list(itertools.permutations(config)):
    out = runConfig(conf)
    if out > maxOut:
        maxOut = out
print(maxOut)