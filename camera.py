from ray import Ray
from polynomes import interpole
from vector import Vector

class Camera( object):
    def __init__( self, o, dir, width, height, ctype = -1, aspx0 = -1, aspx1 = 1  ):
        self.o=o
        self.dir = dir.normalize()
        self.width = width
        self.height = height
        self.ctype = ctype
        
        self.aspect_ratio = float(width) / height
        self.x0 = aspx0
        self.x1 = aspx1
        self.xstep = (self.x1 - self.x0) / (width - 1)
        self.y0 = aspx0 / self.aspect_ratio
        self.y1 = aspx1 / self.aspect_ratio
        self.ystep = (self.y1 - self.y0) / (height - 1)

        
    def generate_ray( self, j, i):
        """
        i: posicion horizontal del pixel 
        j: posicion vertical del pixel  
        """
        """camara hortogonal:
            en cada rayo lanzado la direccion en la que apunta la camara no cambia,
            solo cambia la posicion de la camara"""
        """
        kx = interpole( 0., 0., self.hsizewin, self.hsizeworld, float(x))
        kz = interpole( 0., 0., self.hsizewin, self.hsizeworld, float(y))
        v = Vector(  self.o.x + kx*self.ox.x + kz*self.oz.x, 
                     self.o.y + kx*self.ox.y + kz*self.oz.y, 
                     self.o.z + kx*self.ox.z + kz*self.oz.z)
         """
        
        
        #Ray(camera, Point(x, y) - camera)
        x = self.x0 + i * self.xstep
        y = self.y0 + j * self.ystep
         #vector de dezplazamiento de la camara
        if self.ctype == 0:
            desp = Vector(x, 0, y)
            return Ray( self.o - desp , self.dir )
        elif self.ctype == 1:
            desp = Vector(x, 0, y)
            return Ray( self.o - desp , self.dir )
        else:
            desp = Vector(x, y)
            return Ray( self.o  ,  desp - self.o)
            