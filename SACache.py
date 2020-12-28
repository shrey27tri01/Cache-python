import math
import traceback
import sys

def convertHexToBinary(hexCode):
    '''
    Utility to convert a given hex code into binary
    '''
    bSize = len(hexCode) * 4 
    binaryCode = ("{0:08b}".format(int(hexCode, 16))).zfill(bSize)
    return binaryCode

inputFiles = ["gcc.trace", "gzip.trace", "mcf.trace", "swim.trace", "twolf.trace"] 

for inputFile in inputFiles:
    '''
    loop through all the input files
    '''
    SACache = []     
    rows, columns = (16384, 4)     
    SACache = [[None] * 4 for _ in range(16384)]
    
    time = [[0] * 4 for _ in range(16384)]

    timer = 0
    hit = 0
    miss = 0

    try:
        fileObject = open(inputFile, 'r')
        count = 0
        while True:
            count += 1
            line = fileObject.readline()
            if not line:
                break
            
            address = line[4:12]
            address = convertHexToBinary(address)

            #get address and tag from the trace file
            index = (int)(address[16:30], 2)
            tag = address[0:16]

            #perform the required operations
            timer += 1
            #print(index)
            if SACache[index][0] != None or SACache[index][1] != None or SACache[index][2] != None or SACache[index][3] != None:
                flag = 0
                for x in range(4):
                    if SACache[index][x] != None and SACache[index][x] == tag:
                        hit += 1
                        time[index][x] = timer
                        break
                    flag += 1   
                if flag == 4:
                    maxValue = sys.maxsize * 2 + 1 
                    maxIndex = sys.maxsize * 2 + 1

                    for y in range(4):
                        if time[index][y] < maxValue:
                            maxValue = time[index][y]
                            maxIndex = y
                    
                    SACache[index][maxIndex] =  ""
                    SACache[index][maxIndex] += tag

                    time[index][maxIndex] = timer
                    miss += 1
            elif SACache[index][0] == None or SACache[index][1] == None or SACache[index][2] == None or SACache[index][3] == None:
                index1 = sys.maxsize * 2 + 1

                for z in range(4):
                    if SACache[index][z] == None:
                        index1 = z
                        break
                SACache[index][index1] = ""
                SACache[index][index1] += tag
                time[index][index1] = timer
                miss += 1

        print(f"File is: {inputFile}")
        # print(f"Number of hits: {hit}")
        # print(f"Number of misses: {miss}")
        print(f"Hit rate: {(float)(hit / (hit + miss))}")
        print(f"Miss rate: {(float)(miss / (hit + miss))} \n")

        fileObject.close()
    except FileNotFoundError as e:
        print("An error occurred.")
        traceback.print_exception(*sys.exc_info()) 
