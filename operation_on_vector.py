from math import cos, sin, pi, acos, sqrt

def normeVect(v):
    v1, v2 = v
    return sqrt(v1 ** 2 + v2 ** 2)

def getAngleDegFromVector(u, v):
    u1, u2 = u
    v1, v2 = v
    prod_scal = u1*v1 + u2*v2
    rad = acos( prod_scal / (normeVect(u) * normeVect(v)) )
    det = u1 * v2 - u2 * v1
    return rad * 360 / 2 / pi if det >= 0 else (-rad * 360 / 2 / pi) % 360

def distancePoints(p, q):
    p1, p2 = p
    q1, q2 = q
    return normeVect((q1-p1, q2-p2))