class Poly():
    def __init__(self, *coeffs):
        self.coeffs = coeffs
    def __repr__(self):
        return 'Poly(*{!r})'.format(self.coeffs)
    def __add__ (self, other):
        return Poly(*(x + y for x,y in zip(self.coeffs, other.coeffs)))
    def __len__(self):
        return len(self.coeffs)
        
p1 = Poly(1,2,3)
p2 = Poly(3,4,3)






