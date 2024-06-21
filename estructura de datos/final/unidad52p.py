import numpy as n
class parte:
    def par(self,a,part):
        ind=0
        #part=1
        a1=[]
        a2=[]
        w1=0
        #print ""
        #print a
        #print a1
        #print a2
        #rint ""

        while w1<len(a):
            k=0
            while k<part and w1<len(a):
                a1.append(a[w1])
                k=k+1
                w1=w1+1
            l=0
            while l<part and w1<len(a):
                a2.append(a[w1])
                l=l+1
                w1 = w1 + 1

        return a1,a2