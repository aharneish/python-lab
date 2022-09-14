import math
def dist_Xy(x,y):
    """takes in two points which can be of n dimensions and computes the distance between the two points 
    date: 1/08/2022
    Author: Abburu Aharneish
    Args:
        x (_type_):  tuple
        y (_type_):  tuple
    output: the deistance between them
    """
    out=0
    length=len(x)
    for i in range(length):
        out+=math.sqrt((x[i]-y[i])**2)
    return out
x=[]
y=[]
n=int(input("enter the dimension of the first vector: "))
n2=int(input("enter the dimension of the second vector: "))
if n==n2:
    print("now for the x vector: ")
    for i in range(n):
        x.append(int(input("enter the points ")))
    print("now for the y vector: ")
    for i in range(n2):
        y.append(int(input("enter the points ")))
    print(x)
    print(y)
    print(dist_Xy(x,y))
else:
    print("both the vectors muct have the same dimensions")