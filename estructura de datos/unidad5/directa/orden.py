di = 0
ba = True
while ba == True:
    co = part + 1
    while di < len(a1):
        for t1 in range(di, co - 1):
            if a1[t1] > a1[t1 + 1]:
                aq = a1[t1]
                a1[t1] = a1[t1 + 1]
                a1[t1 + 1] = aq
        # co=co*2
        di = di + co
    else:
        ba = False
print "arreglado", a1

di = 0
ba = True
while ba == True:
    co = part + 1
    while di < len(a2):
        for t1 in range(di, co - 1):
            if a2[t1] > a2[t1 + 1]:
                aq = a2[t1]
                a2[t1] = a2[t1 + 1]
                a2[t1 + 1] = aq
        # co=co*2
        di = di + co
    else:
        ba = False
print "arreglado", a2
print part



########################

f = 0
f1 = 0
j = 0
di = 0
ba = True
while ba == True:
    co = part
    while di < len(a1) - 1:
        for t1 in range(di, co - 1):
            f = int(a1[j])
            f1 = int(a1[j + 1])
            if a1[t1] < a1[t1 + 1]:
                aq = a1[t1]
                a1[t1] = a1[t1 + 1]
                a1[t1 + 1] = aq
            j = j + part
        co = co * 2
        di = di + co
    else:
        ba = False
print "arreglado", a1

f = 0
f1 = 0
j = 0
di = 0
ba = True
while ba == True:
    co = part
    while di < len(a2) - 1 and j < len(a2) and co < len(a2):
        for t1 in range(di, co):
            f = int(a2[j])
            f1 = int(a2[j + 1])
            if f > f1:
                aq = a2[t1]
                a2[t1] = a2[t1 + 1]
                a2[t1 + 1] = aq
            j = j + part
        co = co * 2
        di = di + co
    else:
        ba = False
print "arreglado", a2
print part

