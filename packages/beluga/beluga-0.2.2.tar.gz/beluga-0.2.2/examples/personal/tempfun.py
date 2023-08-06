import matplotlib.pyplot as plt
import numpy as np

# from beluga.ivpsol import Trajectory
# from beluga.liepack.domain.hspaces import HLie
from beluga.liepack import *
from beluga.liepack.domain.liegroups import *
from beluga.liepack.domain.liealgebras import *
# from beluga.liepack.field import VectorField
# from beluga.ivpsol import Flow
# from beluga.ivpsol import RKMK

from beluga.utils import keyboard

# class Add(Morphism):
#     inputs = 2
#     outputs = 1
#     domain = (float, float)
#     range = (float,)
#     @staticmethod
#     def map(x: float, y:float) -> float:
#         return x + y

x = so(3)
y = so(3)
z = so(3)
zero = so(3)
x = SO(3)
y = RN(3)
z.set_vector([0,0,1])
zero.zero()

x.Identity()

a = 2
b = 3

# print(x.data)
# print(exp(x).data)

print((Commutator(a * x + b * y, z)) == (a * Commutator(x, z) + b * Commutator(y, z)))



# y0 = np.array([1, 0], dtype=np.float64)
# tspan = [0, 2*np.pi]
# maxstep = 1
#
# def eom_func(t, y):
#     return (-y[1], y[0])
#
# dim = y0.shape[0]
# y = HLie(RN(dim), y0)
# vf = VectorField(y, evaltype='vector')
# vf.set_equationtype('general')
# vf.set_M2g(eom_func)
# ts = RKMK()
# ts.setmethod('rk45')
# f = Flow(ts, vf, variablestep=True)
# ti, yi = f(y, tspan[0], tspan[-1], maxstep)
# gamma = Trajectory(ti, np.vstack([_.data for _ in yi]))
#
# plt.plot(gamma.t, gamma.y[:,0])
# plt.show()