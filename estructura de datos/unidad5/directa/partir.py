import numpy as n
class parte:
    def par(self,a,part):
        ind=0
        #part=1
        a1=[]
        a2=[]
        w1=0
        print ""
        print a
        print a1
        print a2
        print ""


        #a1 = open("res1.txt", "w")
        #vis = str(" ")
        #a1.write(vis)
        #a1.close()
        #print "Cerrado o no : ", a1.closed

        #a2 = open("ar2.txt", "w")
        #vis = str(" ")
        #a2.write(vis)
        #a2.close()
        #print "Cerrado o no : ", a2.closed

        while w1<len(a):
            k=0
            while k<part and w1<len(a):
                a1.append(a[w1])
                #a1 = open("res1.txt", "a")
                #vis = str(a[w1])
                #a1.write(vis)
                #a1.close()
                #print "Cerrado o no : ", a1.closed
                k=k+1
                w1=w1+1
            l=0
            while l<part and w1<len(a):
                a2.append(a[w1])
                #a2 = open("ar2.txt", "a")
                #vis = str(a[w1])
                #a2.write(vis)
                #a2.close()
                #print "Cerrado o no : ", a1.closed
                l=l+1
                w1 = w1 + 1
        #print part
        print a
        print a1
        print a2
        #a1.close()
        #a2.close()
        #print "Cerrado o no : ", a1.closed
        #print "Cerrado o no : ", a2.closed
        #b1 = open("res1.txt", "r+")
        #a1 = b1.readlines()
        #b1.close()
        #print "Cerrado o no : ", b1.closed

        #b2 = open("ar1.txt", "r+")
        #a2 = b2.readlines()
        #b2.close()
        #print "Cerrado o no : ", b2.closed

        return a1,a2