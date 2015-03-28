import math


while(True):
    print "n"
    n = raw_input()
    print "churn"
    c = int(raw_input())
    print "t"
    t = int(raw_input())
    print "std"
    std = int(raw_input())

    if(t>=c):
        kmin = math.ceil( int(n)*0.5*  (   1-            math.sqrt(     1  -   math.exp(     -    (((t-c)/std)**2)    )          )                 ))
    else:
        kmin = math.ceil(int(n)*0.5*(1-math.sqrt(1-math.exp(-(((c-t)/(std*math.sqrt(2)))**2)))))
    print "kmin = " + str(kmin)
