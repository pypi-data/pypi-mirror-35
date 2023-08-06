# -*- coding: utf-8 -*-
"""
    femagtools.windings
    ~~~~~~~~~~~~~~~~~~~

    Handling windings

 Conventions

 Number of slots: Q
 Numper of pole pairs: p
 Number of phases: m
 Number of layers: l
 Number of wires per slot side: n
 Number of parallel circuits: g
 Number of slots per pole and phase: q = Q/p/2/m
 Number of windings per phase: w1 = Q * n * l/2/m/g
"""
import numpy as np
import femagtools.bch


def gcd(a, b):
    """calc greatest common divisor"""
    while b:
        a, b = b, a % b
    return a


class Windings(object):

    def __init__(self, arg):
        if isinstance(arg, femagtools.bch.Reader):
            self.m = bch.machine['m']
            self.Q = bch.machine['Q']
            self.p = bch.machine['p']
            self.windings = bch.windings
        else:
            for k in arg.keys():
                setattr(self, k, arg[k])

    def sequence(self):
        """returns sequence of winding keys"""
        return list(zip(*sorted([(k, self.windings[k]['PHI'][0])
                                 for k in self.windings.keys()],
                                key=lambda wdg: wdg[1])))[0]

    def slots(self, key):
        """returns slot indexes of winding key"""
        ngen = self.m*self.Q//gcd(self.m*self.Q, self.m*2*self.p)
        # slots in model
        mslots = [int(x/360*self.Q) for x in self.windings[key]['PHI']]
        layers = 1 if len(mslots) == len(set(mslots)) else 2
        pt = gcd(layers*self.Q//2, self.p)
        dim = int(layers*ngen/self.m)
        slots = [s + ngen*n for n in range(self.Q//ngen)
                 for s in mslots[:dim]]
        return np.array(slots).reshape((pt, -1))

    def axis(self):
        """returns axis angle of winding 1 in electrical system"""
        n = [d*w for d, w in zip(self.windings[1]['dir'],
                                 self.windings[1]['N'])]
    
        a = [self.p*np.pi/self.Q*(1+2*s)
             for s in self.slots(1)[0]]
        if len(a) > len(n):
            n = n + [-i for i in n]
        return np.arctan2(np.dot(np.sin(a), n),
                          np.dot(np.cos(a), n))*180/np.pi


if __name__ == "__main__":
    import sys
    #bch = femagtools.bch.read(sys.argv[1])
    Q = 90
    p = 12
    m = 3
    w = {1: {
        'dir': [1, 1, 1, -1, -1, -1, 1, 1, -1, -1],
        'N': [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
        'PHI': [2.0, 6.0, 6.0, 18.0, 18.0, 22.0, 34.0, 34.0, 50.0, 50.0]}}
    wdgs = Windings(dict(Q=Q, p=p, m=m, windings=w))
    a = (wdgs.axis() - 90)/p
    if a < 0:
        a += 360/p
    print(a)
    
#    response = {"node_angle": 0.277778,
#                "node_distance": 0.000782,
#                "coil_angles": [5.817757e-02, 5.817757e-02,
#                                1.745328e-01, 5.235983e-01,
#                                6.399536e-01, 6.399536e-01],
#                "coil_directions": [1, 1, 1, -1, -1, -1],
#                "phases": [1, 7, 3]}
