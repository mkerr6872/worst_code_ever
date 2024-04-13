import math


if __name__ == "__main__":
    a = 4
    ca = list()
    coa = 0
    for i in range(2,a+1,1):
        if ((a/i) - math.floor(a/i) == 0):
            ca.append(i)
    ccb = ca.copy()
    for i in ccb:
        coa = coa + 1
    if (coa == 1):
        cca = "prime"
    else:
        cca = 'not prime'
    b = 52
    ba = list()
    boa = 0
    for i in range(2,b+1,1):
        if ((b/i) - math.floor(b/i) == 0):
            ba.append(i)
    bbb = ba.copy()
    for i in bbb:
        boa = boa + 1
    if (boa == 1):
        bba = "prime"
    else:
        bba = 'not prime'
    a1=a
    b1=b
    #capj = 0
    #ap = list()
    #apr = list()
    #for i in range(1,a+1,1):
    #    for j in range(1,i+1,1):
    #        if ((i/j)-math.floor(i/j)==0):
    #            ap.append(j)
    #    for k in ap:
    #        capj +=1
    #    if (capj <=2):
    #        apr.append(j)
    #    capj=0
    #    ap.clear()
    #aprl = set(apr)
    #aprlf = list()
    if cca == "prime":
        factorsa = list()
        factorsa.append(a)
    else:
        factorsa = []
        d = 2
        while a > 1:
            while a % d == 0:
                factorsa.append(d)
                a /= d
            d = d + 1
    if bba == "prime":
        factorsb = list()
        factorsb.append(b)
    else: 
        factorsb = []
        d = 2
        while b > 1:
            while b % d == 0:
                factorsb.append(d)
                b /= d
            d = d + 1   
    la = len(factorsa)
    lb = len(factorsb)


    answer = 1
    for i in factorsa:
        answer = answer*i
    for j in factorsb:
        answer = answer*j

    print("The answer is the amount of a's printed below")

    for i in range(answer):
        print("a")
    

