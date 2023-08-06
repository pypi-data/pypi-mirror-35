from beluga.ivpsol import Propagator

from beluga.liepack.domain.liealgebras import sp
from beluga.liepack.domain.liegroups import SP
from beluga.liepack.domain.hspaces import HLie
from beluga.liepack.field import VectorField
from beluga.liepack import exp, Adjoint, Commutator
from beluga.ivpsol import RKMK, Flow

from beluga.ivpsol import Trajectory

from beluga.utils import keyboard
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

y0 = np.array([1,1])

space0 = np.eye(2)

def fm2g(t, y):
    dat = np.array([[0, 1], [-1, 0]])
    return sp(2, dat)

dim = y0.shape[0]
y = HLie(SP(dim), space0)



vf = VectorField(y)
vf.set_equationtype('general')
vf.set_M2g(fm2g)
ts = RKMK()
ts.setmethod('rk45')
f = Flow(ts, vf, variablestep=True)
ti, yi = f(y, 0, 2.5, 0.01)
for ii in np.linspace(0.5, 1.5, 20):
    y0 = np.array([ii,ii])
    gamma = Trajectory(ti, np.vstack([_.data @ y0 for _ in yi]))
    plt.plot(gamma.y[:,0], gamma.y[:,1])
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot(gamma.y[:,0], gamma.y[:,1], gamma.y[:,2])
#
# print(gamma.y)


plt.show()
