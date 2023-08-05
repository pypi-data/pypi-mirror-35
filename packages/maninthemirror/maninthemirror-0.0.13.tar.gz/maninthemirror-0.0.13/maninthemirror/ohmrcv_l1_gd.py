import matplotlib.pyplot as plt
import numpy as np

n = 10
m = 3
l = 10000

v = np.random.normal(size=m)
w = np.random.normal(size=(n, m, m))

v -= v.mean()
for i in range(n):
    w[i] += 1. / float(m) - w[i].mean(1)[:, np.newaxis]

x = np.random.randint(m, size=(l, n), dtype=int)
h = v + w[range(n), x].sum(1)
p = np.exp(h)
p /= p.sum(1)[:, np.newaxis]
y = (p.cumsum(1) < np.random.uniform(size=(l, 1))).sum(1)


def fit(x, y, step_size=1.0, atol=1e-8, rtol=1e-5, max_it=500):

    v = np.zeros(m)
    w = np.array([np.identity(m) for _ in range(n)])

    dv = np.empty(m)
    dw = np.empty((n, m, m))

    y_oh = np.zeros((l, m), dtype=bool)
    y_oh[range(l), y] = True

    d, e = [np.inf], []

    for it in range(max_it):

        h = v + w[range(n), x].sum(1)
        p = np.exp(h)
        p /= p.sum(1)[:, np.newaxis]

        p_hot = p[y_oh]
        p[y_oh] -= 1
        p *= p_hot[:, np.newaxis]

        dv = 2 * p.mean(0)
        dw = np.zeros((n, m, m))
        for i in range(l):
            for j in range(n):
                dw[j][x[i, j]] += p[i]
        dw *= 2 / float(l)

        v -= step_size * dv
        w -= step_size * dw

        d.append(2 * (1 - p_hot).mean(0))
        e.append([np.linalg.norm(v_true - v), np.linalg.norm(w_true - w)])

        aerr = d[-2] - d[-1]
        rerr = aerr / d[-2]
        if aerr < atol or rerr < rtol:
            break

        print it, d[-1], e[-1]

    d = np.array(d)
    e = np.array(e)
    return v, w, d[1:], e


v_true = v.copy()
w_true = w.copy()

v, w, d, e = fit(x, y)

fig, ax = plt.subplots(1, 3, figsize=(12, 4))
ax[0].plot(e[:, 0], 'r-')
ax0 = ax[0].twinx()
ax0.plot(e[:, 1], 'b-')
ax[1].plot(d, 'k-')
lo = min(v.min(), w.min())
hi = max(v.max(), w.max())
grid = np.linspace(lo, hi)
ax[2].plot(grid, grid, 'k--')
ax[2].scatter(v, v_true, c='r', s=1)
ax[2].scatter(w.flatten(), w_true.flatten(), c='b', s=0.5)
ax[0].set_xlabel('iteration')
ax[0].set_ylabel('$E$')
ax[1].set_xlabel('iteration')
ax[1].set_ylabel('$D$')
ax[2].set_xlabel('fitted')
ax[2].set_ylabel('true')
plt.tight_layout()
plt.show()
