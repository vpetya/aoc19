arr = [3,225,1,225,6,6,1100,1,238,225,104,0,1001,92,74,224,1001,224,-85,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1101,14,63,225,102,19,83,224,101,-760,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,21,23,224,1001,224,-44,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1102,40,16,225,1102,6,15,225,1101,84,11,225,1102,22,25,225,2,35,96,224,1001,224,-350,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,56,43,225,101,11,192,224,1001,224,-37,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1002,122,61,224,1001,224,-2623,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1,195,87,224,1001,224,-12,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,75,26,225,1101,6,20,225,1102,26,60,224,101,-1560,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,226,224,102,2,223,223,1006,224,329,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,344,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,359,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,1108,677,226,224,102,2,223,223,1005,224,389,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,404,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,434,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,449,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,464,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,524,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,539,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,554,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,569,101,1,223,223,107,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,599,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,7,226,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,659,1001,223,1,223,1008,226,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

arr2 = [1002,4,3,4,33]
arr3 = [1101,100,-1,4,0]
arr4 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
input = 5
output = [0]

def runArr(arr):
    counter = 0
    while True:
        inst = arr[counter]
        code = int(str(arr[counter])[-2:])
        if code == 99:
            break
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
            arr[arr[counter+1]] = input
        elif code == 4:
            #write
            step = 2
            p1 = arr[counter+1] if len(str(inst)) > 2 and int(str(inst)[-3]) else arr[arr[counter+1]]
            output[0] = p1
            if output[0] != 0:
                print(counter)
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

#print(runArr(arr2))
#print(runArr(arr3))
runArr(arr)
print(output[0])


 