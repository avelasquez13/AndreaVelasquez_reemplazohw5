import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt

rx = np.array([0.324190175,-0.701534590,-0.982564148,1.104185888,3.266443877,-9.218802228,19.930781147,24.323085642])
ry = np.array([0.090955208,-0.168809218,-0.191145980,-0.826097003,-3.888055863,1.788299816,-2.555241579,-17.606227355])
rz = np.array([-0.022920510,0.037947785,-0.000014724,-0.044595990,-0.057015321,0.335737817,-0.267710968,-0.197974999])
vx = np.array([-4.627851589,1.725066954,1.126784520,3.260215854,2.076140727,-0.496457364,0.172224285,0.664855006])
vy = np.array([10.390063716,-7.205747212,-6.187988860,4.524583075,1.904040630,-2.005021061,1.357933443,0.935497207])
vz = np.array([1.273504997,-0.198268558,0.000330572,0.014760239,-0.054374153,0.054667082,0.002836325,-0.034716967])

r = np.sqrt(rx**2+ry**2+rz**2)
v = np.sqrt(vx**2+vy**2+vz**2)

x = np.log(r)
y = np.log(v)

G = const.G
N = 100000
delta_m = 0.01
delta_b = 0.01

m = [2]
b = [8]


def p_obs(m, b, x, y):
    return -0.5*np.sum((y-m*x-b)**2)


for i in range(1, N-1):
    Um = np.random.random()*2*delta_m-delta_m
    m_new = m[i-1] + Um
    Ub = np.random.random()*2*delta_b-delta_b
    b_new = b[i-1] + Ub
    
    alfa = min(1, np.exp(p_obs(m_new, b_new, x, y)-p_obs(m[i-1], b[i-1], x, y)))

    u = np.random.random()
    if u<alfa:
        m.append(m_new)
        b.append(b_new)
    else:
        m.append(m[i-1])
        b.append(b[i-1])


alpha = -2*np.median(m) + 1
logM_s = 2*np.median(b)-np.log(G)

print alpha, logM_s

plt.scatter(x, y)
plt.plot(x, np.median(m)*x+np.median(b))
plt.show()
