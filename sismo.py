import numpy as np
import matplotlib.pyplot as plt

x = np.array([3., 3., 4., 4., 5., 5.])
y = np.array([15., 16., 15., 16., 15., 16.])

t = np.array([3.12, 3.26, 2.98, 3.12, 2.84, 2.98])

sigma = 0.1
v = 5.

N = 20000

delta = 0.1

x_c = np.array([1])
y_c = np.array([2])

def p_obs(x_c, y_c, x, y):
    t_t = np.sqrt((x-x_c)**2+(y-y_c)**2)/v
    return  -0.5/sigma**2*np.sum((t-t_t)**2)

for i in range(1, N-1):
    Ux = np.random.random()*2*delta-delta
    Uy = np.random.random()*2*delta-delta

    x_cnew = x_c[i-1] + Ux
    y_cnew = y_c[i-1] + Uy
    
    alfa = min(1, np.exp(p_obs(x_cnew, y_cnew, x, y)-p_obs(x_c[i-1], y_c[i-1], x, y)))

    u = np.random.random()
    if u<alfa:
        x_c = np.append(x_c, x_cnew)
        y_c = np.append(y_c, y_cnew)
    else:
        x_c = np.append(x_c, x_c[i-1])
        y_c = np.append(y_c, y_c[i-1])


plt.scatter(x_c[10000:], y_c[10000:])
plt.show()
