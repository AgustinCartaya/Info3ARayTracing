from dags import *
import polynomes
from math import sqrt

from color import Color
from material import *
from point import Point
from vector import Vector

class Obj(object):
    def __init__( self):
        " "
        

class Prim(Obj):
    def __init__( self, fonc_xyz, material):
        self.fonc=fonc_xyz
        self.material = material
    
    def intersects( self, rayon):
        dico = { "x": Nb(rayon.origin.x) + Nb(rayon.direction.x)*Var("t"),
        "y": Nb(rayon.origin.y) + Nb(rayon.direction.y)*Var("t"),
        "z": Nb(rayon.origin.z) + Nb(rayon.direction.z)*Var("t")}
        expression_en_t=self.fonc.evalsymb( dico )
        pol_t = expression_en_t.topolent()
        return racines( pol_t)
    
    def normal( self, tpl):
        fx=self.fonc.derivee("x")
        fy=self.fonc.derivee("y")
        fz=self.fonc.derivee("z")
        dico={"x":tpl.x , "y": tpl.y , "z":tpl.z}
        (a,b,c)= ( fx.eval( dico), fy.eval( dico), fz.eval( dico))
        normal = Vector(a,b,c).normalize()
        return normal
    
class Sphere(Prim):
    
    def __init__( self, origin, r, material):
        Prim.__init__( self, Sphere.ecuation([origin,r]), material)
        self.origin = origin
        self.r = r
            
    @staticmethod
    def ecuation(args):
        (cx,cy,cz,r) = (args[0].x,args[0].y,args[0].z, args[1])
        x=Var("x")
        y=Var("y")
        z=Var("z")
        return (x-Nb(cx))*(x-Nb(cx)) + (y-Nb(cy))*(y-Nb(cy)) + (z-Nb(cz))*(z-Nb(cz)) - Nb(r*r) 

    def intersects(self, ray):
        """Checks if ray intersects this sphere. Returns distance to intersection or None if there is no intersection"""
        sphere_to_ray = ray.origin - self.origin
        # a = 1
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - self.r * self.r
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return (dist,None)
        return None

    def normal(self, surface_point):
        """Returns surface normal to the point on sphere's surface"""
        return (surface_point - self.origin).normalize()
    
class Tore(Prim):    

    def __init__( self,  r, R, material):
        Prim.__init__( self, Tore.ecuation([r,R]), material)
        self.r = r
        self.R = R
        
    @staticmethod
    def ecuation(args):
        (r, R) = (args[0],args[1])
        x=Var("x")
        y=Var("y")
        z=Var("z")
        tmp=x*x+y*y+z*z+Nb(R*R-r*r)
        return tmp*tmp- Nb(4.*R*R)*(x*x+z*z)
    
class Steiner2(Prim):    

    def __init__( self, material):
        Prim.__init__( self, Steiner2.ecuation(None), material)

    @staticmethod
    def ecuation(args):
        x=Var("x")
        y=Var("y")
        z=Var("z")
        return (x * x * y * y - x * x * z * z + y * y * z * z - x * y * z)
    
class Steiner4(Prim):    

    def __init__( self, material):
        Prim.__init__( self, Steiner4.ecuation(None), material)

    @staticmethod
    def ecuation(args):
        x=Var("x")
        y=Var("y")
        z=Var("z")
        return y * y - Nb( 2.) * x * y * y - x * z * z + x * x * y * y + x * x * z * z - z * z * z * z

class Hyperboloide_2nappes(Prim):    

    def __init__( self, material):
        Prim.__init__( self, Hyperboloide_2nappes.ecuation(None), material)

    @staticmethod
    def ecuation(args):
        x=Var("x")
        y=Var("y")
        z=Var("z")
        return Nb(0.) - (z * z - (x * x + y * y + Nb(0.1)))
    
    
    
    
class Hyperboloide_1nappe(Prim):    

    def __init__( self, material):
        Prim.__init__( self, Hyperboloide_1nappe.ecuation(None), material)

    @staticmethod
    def ecuation(args):
        x=Var("x")
        y=Var("y")
        z=Var("z")
        return Nb(0.) - (z * z - (x * x + y * y - Nb(0.1)))

    
    
    
class Roman(Prim):    

    def __init__( self, material):
        Prim.__init__( self, Roman.ecuation(None), material)

    @staticmethod
    def ecuation(args):
        x=Var("x")
        y=Var("y")
        z=Var("z")
        return ( x * x * y * y + x * x * z * z + y * y * z * z - Nb(2.) * x * y * z)