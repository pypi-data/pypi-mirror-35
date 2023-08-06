from numpy import sqrt, ones_like, pi, clip, arccos, arcsin, arctan2
from numba import jit

def qpower2(z,p,c,a):

    I_0 = (a+2)/(pi*(a-c*a+2))
    g = a/2

    result = ones_like(z)

    j = (z < (1-p)).nonzero()
    s = 1-z[j]**2
    c0 = I_0*(1-c+c*s**g)
    c2 = 0.125*I_0*a*c*(2*(g-1)*s**(g-2) - s**(g-1))
    result[j] = 1 - c0*pi*p**2 - c2*pi*p**4

    j = (abs(z-1) < p).nonzero()
    zj = z[j]
    d = clip((zj**2 - p**2 + 1)/(2*zj),0,1)
    ra = 0.5*(zj-p+d)
    rb = 0.5*(1+d)
    sa = clip(1-ra**2,0,1)
    sb = clip(1-rb**2,0,1)
    s = clip(1-z**2,0,1)
    q = sqrt(clip(p**2-(d-zj)**2,0,1))
    c0a = I_0*(1-c+c*sa**g)
    c0b = I_0*(1-c+c*sb**g)
    aa0 = (p**2 * arccos(clip((zj-d)/p,-1,1)) 
            - (zj-d)*sqrt(clip(p**2-(d-zj)**2,0,1)) )
    ab0 = arccos(d) - d*sqrt(clip(1-d**2,0,1))
    c1a =  -I_0*c*a*sa**(g-1)*ra
    aa1 = ( q*((d-zj)*(zj+2*d-3*ra)-2*p**2)/3
           + p**2*(ra-zj)*(arctan2(zj-d,q) - pi/2) )
    c2a = I_0*a*c*((g-1)*sa**(g-2) - 0.5*sa**(g-1))
    aa2 = (q*(12*ra**2*(d-zj)+8*ra*(2*p**2-2*d**2+d*zj+zj**2)
           - p**2*(3*d+13*zj)-2*(zj**3+d*zj**2+d**2*zj-3*d**3))/12
           - 0.25*p**2*(4*ra**2-8*ra*zj+p**2+4*zj**2)*(arctan2(zj-d,q)-pi/2) )
    result[j] = 1 - c0a*aa0 - c0b*ab0 - c1a*aa1 - c2a*aa2

    return result
