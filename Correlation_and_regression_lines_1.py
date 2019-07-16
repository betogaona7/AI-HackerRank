import math 

#physics = list(map(int, input().split()))
#history = list(map(int, input().split()))

physics = [15,12,8,8,7,7,7,6,5,3]
history = [10,25,17,11,13,17,20,13,9,15]

def mean(x):
    return sum(x)/len(x)

def corr(x, y):
    meanx = mean(x)
    meany = mean(y)
    diffprod = 0;
    xdiff2 = 0
    ydiff2 = 0

    for i in range(len(x)):
        xdif = x[i] - meanx
        ydif = y[i] - meany
        diffprod += xdif*ydif
        xdiff2 += xdif*xdif
        ydiff2 += ydif*ydif
    return diffprod/math.sqrt(xdiff2*ydiff2)

print("{:.3f}".format(corr(physics, history)))
