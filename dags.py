from polynomes import * 


class M(object):
    def __init__(self):
        "   " 
    def __add__( self, b):
        return Plus( self, b)
    def __mul__( self, b):
        return Mult( self, b)
    def __sub__( self, b):
        return Plus( self, Opp(b))

class Opp(M):
    def __init__(self, a):
        self.a=a
        
    def eval(self, dico):
        return (0 - self.a.eval(dico))
    
    def evalsymb(self, dico):
        return Opp(self.a.evalsymb(dico))
    
    def derivee(self, noumvar):
        return Opp(self.a.derivee(noumvar))
    
    def topolent(self):
        return opp(self.a.topolent()) 


class Plus(M):
    def __init__(self, a, b):
        self.a=a
        self.b=b
        
    def eval(self, dico):
        return(self.a.eval(dico) + self.b.eval(dico))
    
    def evalsymb(self, dico):
        return (self.a.evalsymb(dico) + self.b.evalsymb(dico))
    
    def derivee(self, noumvar):
        return Plus(self.a.derivee(noumvar), self.b.derivee(noumvar))
        
    def topolent(self):
        return plus(self.a.topolent(), self.b.topolent())
        
            


class Mult(M):
    def __init__(self, a, b):
        self.a=a
        self.b=b
        
    def eval(self, dico):
        return(self.a.eval(dico) * self.b.eval(dico))
    
    def evalsymb(self, dico):
        return (self.a.evalsymb(dico) * self.b.evalsymb(dico))
    
    def derivee(self, noumvar):
        return Plus(self.a * self.b.derivee(noumvar), self.b * self.b.derivee(noumvar))
    
    def topolent(self):
        return mult(self.a.topolent(), self.b.topolent())


class Nb(M):
    def __init__(self, n):
        self.nb=n

    def eval(self, dico):
        return self.nb
    
    def evalsymb(self, dico):
        return self
    
    def derivee(self, noumvar):
        return (Nb(0))
    
    def topolent(self):
        return [self.nb]



class Var(M):
    def __init__(self, nom):
        self.nom=nom

    def eval(self, dico):
        if self.nom in dico:
            return dico[self.nom]
        else:
            return 1/0
    
    def evalsymb(self, dico):
        ret = dico.get(self.nom)
        if ret != None:
            return ret
        return self
    
    def derivee(self, noumvar):
        if self.nom == noumvar:
            return Nb(1)
        else:
            return Nb(0)
        
    def topolent(self):
        return [0, 1]
    
#method not used   
def tobernsteindags(a, n = -1):
    ''' 
    Devuelve una lista con:
        [0]: el polinomio a en la base de Bernstein 
        [1]: loc coeficientes de a para la base de berstein c0, c1, c2...
        [2]: expresion de berstein (1-t)^2 + 2*t*(1-y) + t^2
    '''
    
    if n == -1:
        n = len(a)-1
    C = []#coieficientes de berstein f(i/n) 
    B = []#polinomios de berstein
    exp = Nb(0) #expresion de berstein exp: c0*(1-t)^2 + c1*2*t*(1-y) + c2*t^2
    
    #calcular t, t^2, t^3 y los factoriales (n!)
    t = [ [1, Var('t')] ] 
    for i in range(1,n+1):
        t.append( [t[-1][0] * max(i,1), t[-1][1] *  Var('t')] )

    #calculo del polinomio    
    for i in range(n+1):
    
        if i == 0:
            a0 = t[n-i-1][1].evalsymb( {'t': Nb(1) - Var('t') } )
        elif i == n:
            a0 = t[i-1][1]
        else:
            a0 = (t[i-i][1]* t[n-i-1][1].evalsymb( {'t': Nb(1) - Var('t') } ))
            
        C.append( evaluate(a, i/(n)))
        B.append( Nb(t[n][0]/(t[i][0]* t[n-i][0])) * a0 )
        exp += Nb(C[-1]) * B[-1]
    
    return [exp.topolent(),C, B]
