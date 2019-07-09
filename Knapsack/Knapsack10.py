def readFile(name):
    f = open(name,'r')
    line0 = f.readline()
    line0 = line0.strip()
    line0 = line0.split(" ")
    i = int(line0[0])
    W = int(line0[1])
    w = []
    v = []
    for line in f:
        line = line.strip()
        line = line.split(' ')
        v.append(int(line[0]))
        w.append(int(line[1]))
    return (i,W,w,v)

def knapsack10(i,W,q):
    if i < 0 :
        return 0
    if q < 10 and w[i] <= W:
        q += 1
        return max(v[i] + knapsack10(i,W-w[i],q),knapsack10(i-1,W,0))
    else:
        return knapsack10(i-1,W,0)

inst = input('Instancia de teste:')
t = readFile(inst)
i = t[0] - 1
W = t[1]
w = t[2]
v = t[3]

print(knapsack10(i,W,0))
