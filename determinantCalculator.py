import numpy as np

def twoXtwo(array):
    return array[0][0]*array[1][1]-array[1][0]*array[0][1]


def sliceoutcolumn(array,column):
    front=np.array(array[1:,0:column])
    back=np.array(array[1:,column+1:])
    newarray=np.append(front,back,axis=1)
    return newarray


def nXn(array, n):
    determinant=0
    if(n==1):
        return array[0][0] 
    elif(n==2):
        return twoXtwo(array)
    else:
        count=0
        top=np.array(array[0,:n])
        bot=[]
        for i in range(0,n):
            count+=1
            bot.append(sliceoutcolumn(array,i))
            pos_or_neg=(-1)**i
            #Multiplies the top element with the determinent of the modified bottom array
            determinant+=top[i]*nXn(bot[i],n-1)*pos_or_neg
            #Only returns the sum at the end of the for loop
            if(count==n):
                return determinant


def getMatrixSize():
     colNum = 0
     isNum=False
     while(not isNum):
         colNum = input("How many rows/columns are in your matrix? ")
         isNum=colNum.isdigit() and colNum != "0"
     return int(colNum) 


def getMatrixValues(colNum):
    matrix = []
    for colIndex in range(colNum):
        isInvalid = True
        while(isInvalid):
            matrixColumn = input("Insert the {} numbers in row {}, seperated by commas: ".format(colNum, colIndex+1)).split(',');
            if(len(matrixColumn) != colNum):
                continue;
            isInvalid = False
            for i in range(len(matrixColumn)):
                matrixColumn[i] = int(matrixColumn[i].strip()); 
            matrix.append(matrixColumn)
    return matrix


def printResult(numpyMatrix, determinant):
    print("\n\nInputted Matrix")
    print("-"*15)
    print(numpyMatrix)
    print("\nDeterminant = {}".format(determinant))


def startProgram():
    while(True):
        colNum = getMatrixSize()
        numpyMatrix = np.array(getMatrixValues(colNum))
        determinant = nXn(numpyMatrix, colNum)  
        printResult(numpyMatrix, determinant)
        runAgain = input("Have another matrix(y/n)? ").lower()
        if(runAgain == "y"):
            continue;
        break;

startProgram();
