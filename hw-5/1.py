import itertools

class Vector():
    def __init__(self, x, y, z):
        assert isinstance(x, (int, float)) and not isinstance(x, bool)
        assert isinstance(y, (int, float)) and not isinstance(y, bool)
        assert isinstance(z, (int, float)) and not isinstance(z, bool)
        self.x=x
        self.y=y
        self.z=z
    def __abs__(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    def __subtraction__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __scal__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x*other.x+self.y*other.y+self.z*other.z)
        if isinstance(other,(int,float)):
            return Vector(self.x*other,self.y*other,self.z*other)
    def str(self):
        return f'x={self.x}, y={self.y}, z={self.z}'
    
v1=Vector(1,2,3)
v2=Vector(2,3,4)
v3=Vector(3,4,5)
a=[v1,v2,v3]

def center(L):
    res=Vector(0,0,0)
    for i in L:
        res+=i
    return Vector(res.x/len(L), res.y/len(L), res.z/len(L))

print(center(a))


