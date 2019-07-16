p = [15,  12,  8,   8,   7,   7,   7,   6,5,   3]
h = [10,  25,  17,  11,  13,  17,  20,  13,  9,  15]

def mean(x):
    return sum(x)/len(x)

meanx = mean(p)
meany = mean(h)

den = 0
var = 0
for i in range(len(p)):
    den += (p[i]-meanx)*(h[i]-meany)
    var += (p[i]-meanx)**2

print("{:.3f}".format(den/var))
