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

def binaryToDecimal(binary):    
    '''
    Utility to convert a given binary code into decimal
    '''   
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10   
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

inputFiles = ["gcc.trace", "gzip.trace", "mcf.trace", "swim.trace", "twolf.trace"] 

for inputFile in inputFiles:
    '''
    loop through all the input files
    '''
    DMCache = [None for x in range(65536)]
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

            # get address and tag from the trace file
            # conv = lambda i : i or 0
            # addressIndex = conv(address[14:30]) 
            index = (int)(address[14:30], 2)
            tag = address[0:14]
            # 20000010 -> 00100000000000 0000000000000100 00
            #perform the required operation
            if DMCache[index] == None:
                DMCache[index] = ""
                DMCache[index] += tag
                miss += 1
            elif DMCache[index] == tag:
                hit += 1
            else:
                DMCache[index] = ""
                DMCache[index] += tag
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




    