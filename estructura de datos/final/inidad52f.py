class fus:
    def fu(self,a,a1,a2,part):
        b1=True
        b2=True
        w2=0
        i1=0
        i2=0
        aux1=0
        aux2=0
        part=1
        if  w2<len(a):
            aux1=a1[i1]
            i1=i1+1
            b1=False
        if  w2<len(a):
            aux2=a2[i2]
            i2=i2+1
            b2=False
        while (i1<len(a1) or b1==False) and (i2<len(a2) or b2==False):
            k=0
            l=0
            while (k<part and b1==False) and (l<part and b2==False):
                if aux1<=aux2:
                    a[w2] = aux1
                    b1=True
                    k=k+1
                    #i1=i1+1
                    w2=w2+1
                    if i1<len(a1):
                        aux1=a1[i1]
                        i1 = i1 + 1
                        b1=False
                else:
                    a[w2] = aux2
                    b2 = True
                    l = l + 1
                    #i2 = i2 + 1
                    w2 = w2 + 1
                    if i2 < len(a2):
                        aux2 = a2[i2]
                        i2 = i2 + 1
                        b2 = False
        if b1==False:
            #aux1=a1[i1]
            #i1 = i1 + 1
            a[w2]=aux1
            #i1=i1+1
            w2=w2+1
        if b2==False:
            #aux2 = a2[i2]
            #i2 = i2 + 1
            a[w2]=aux2
            #i2=i2+1
            w2=w2+1
        while i1<len(a1):
            a[w2]=a1[i1]
            w2=w2+1
            i1 = i1 + 1
        while i2<len(a2):
            a[w2]=a2[i2]
            w2 = w2 + 1
            i2 = i2 + 1

