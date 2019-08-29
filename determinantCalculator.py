import numpy as np

def twoXtwo(array):
    return array[0][0]*array[1][1]-array[1][0]*array[0][1]

test=[[7,8],[12,5]]
test1=[[-3,6],[4,-9]]

print(twoXtwo(test)) #prints -61
print(twoXtwo(test1)) #prints 3


def threeXthree(array):
    #The original array is split into two parts
    part1=np.array([array[1][0],array[1][2]])
    part2=np.array([array[2][0],array[2][2]])

    #Whole is the array minus the column taken out
    whole=np.concatenate((part1, part2))

    #Reshaping the new array into a two by two
    whole.shape=(2,2)
    #print whole

    return array[0][0]*twoXtwo(array[1:,1:])-array[0][1]*twoXtwo(whole)+array[0][2]*twoXtwo(array[1:,:-1])

test2=np.array([[1,2,3],[4,5,6],[7,8,9]])
test3=np.array([[4,-9,8],[8,7,-11],[1,9,-3]])
print(threeXthree(test2)) #prints 0
print(threeXthree(test3)) #prints 715


def sliceoutcolumn(array,column):
    front=np.array(array[1:,0:column])
    back=np.array(array[1:,column+1:])
    newarray=np.append(front,back,axis=1)
    return newarray

#Lots of commented out code was for my debugging
def nXn(array, n):
    determinant=0
    if(n==2):
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

test3=np.array([[1,9,12,-10],[8,-5,2,-7],[12,9,-3,12],[-19,7,-21,3]])
test4=np.array([[-10,-22,8,0,-4],[4,13,-1,8,-9],[-19,5,14,12,-7],[10,-11,-13,-15,1],[3,6,12,19,-2]])
print(nXn(test3, 4)) #prints -66978
print(nXn(test4, 5)) #prints -15354
