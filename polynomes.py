import math
import random

def plus(a,b):
    res =[0 for i in range( max( len(a),len(b)))]
    for i in range( max( len(a),len(b)) ):
        if i >= len(a):
            res[i] = b[i]
        elif i >= len(b):
            res[i] = a[i]
        else:
            res[i] = a[i]+b[i]
    return res

def mult(a,b):
    res = [0 for i in range( len(a)+len(b)-1)]
    for i in range( len(a) ):
        for j in range( len(b) ):
            res[i+j] += a[i]*b[j]
    return res

def opp(a):
    res = []
    for i in a:
        res.append( -i )
    return res

def coeff(P, i):
    if i>=0 and i<len(P):
        return P[i]
    return 0

def evaluate(a, t):
    res = 0
    for i in range( len(a) ):
        res = res + a[i] * (t**i)
    return res


def c(k, n):
    if n<k:
        return 0
    if n == k or k == 0:
        return 1
    if k == 1:
        return n
    return c(k-1, n-1)+c(k, n-1)

def tobernstein(lst):
    ret = [0 for x in range(len(lst))]
    d = len(lst) -1
    for k in range(len(lst)):
        temp = []
        for i in range(len(lst)):
            temp.append(lst[k]* (c(k, i)/c(k, d)))
        ret = [ret[x]+temp[x] for x in range(len(ret))]
    return ret

def mintab(v):
    return min(v)

def maxtab(v):
    return max(v)


def casteljau(v):
   
    res = [[],[]]
        
    def internal(v):
        res[0].append(v[0])
        res[1].append(v[-1])
        if len(v) == 1:
            return
        vn =[]
        for i in range(len(v)-1):
            vn.append(( v[i]+ v[i+1]) /2)
    
        internal(vn)
        
    internal(v)
    #invertir lista 1 antes de enviarla
    return [res[0], res[1][::-1]]
   
def solve(epsilon, tab, t1, t2, sol):
    #print(tab)
    if 0 < min(tab) or 0>max(tab):
        return sol
    if t2-t1 < epsilon:
        return ((t1+t2)/2, None)
    tab1, tab2 = casteljau(tab)
    b1 = solve(epsilon, tab1, t1, (t1+t2)/2, sol)
    b2 = solve(epsilon, tab2, (t1+t2)/2, t2, sol)
    return cons(b1, b2)


def cons(c1, c2):
    if c1 == None:
        return c2
    if c2 == None:
        return c1
    (hd, qu) = c1
    return cons(qu, (hd, c2))

def mymap(func, lst):
    if lst == None:
        return None
    (hd, qu) = lst
    return (func(hd), mymap(func, qu))

def racines(p):
    p1 = p[::-1]
    p1 = tobernstein(p1)
    roots = solve(1e-8,p1, 0, 1, None)
    return  mymap((lambda x: 1./x), roots)


def hd( q ):
    if q is not None:
        m = []
        while True:
            m.append(q[0])
            q = q[1]
            if q is None:
                break
            if q[1] is None:
                m.append(q[0])
                break
        return mintab(m)
    return None

def interpole( x1, y1, x2, y2, x) :
    # x=x1 -> y=y1
    # x=x2 -> y=y2
    x1, y1, x2, y2, x= float(x1), float(y1), float( x2), float(y2), float(x)
    return (x-x2)/(x1-x2)*y1 + (x-x1)/(x2-x1)*y2

def normalize3(x):
    (a,b,c) = (x[0], x[1], x[2])
    (a,b,c)=(float(a),float(b),float(c))
    n=math.sqrt(a*a+b*b+c*c)
    if 0.==n:
        return (0.,0.,0.)
    else:
        return (a/n, b/n, c/n)
