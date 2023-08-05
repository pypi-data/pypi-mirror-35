from numpy import matlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse.linalg import svds
from scipy.sparse import csc_matrix

n = 10
m = 3
l = 1000

v = np.random.normal(size=m)
w = np.random.normal(size=(n, m, m))

v -= v.mean()
for i in range(n):
    w[i] -= w[i].mean(0)
    w[i] -= w[i].mean(1)[:, np.newaxis]

x = np.random.randint(m, size=(l, n), dtype=int)
h = v + w[range(n), x].sum(1)
p = np.exp(h)
p /= p.sum(1)[:, np.newaxis]
y = (p.cumsum(1) < np.random.uniform(size=(l, 1))).sum(1)

v_true = v.copy()
w_true = w.copy()
# w_true = np.swapaxes(w_true, 0, 1)
w_true = np.reshape(w_true, (m * n, m))


def fit(x, y, max_iter=100):

    v = matlib.zeros(m)
    w = matlib.zeros((m * n, m))

    x_oh = csc_matrix((np.ones(l * n), (np.repeat(range(l), n),
                                        (x + m * np.arange(n)).flatten())))
    x_oh_svd = svds(x_oh, k=m * n - n + 1)
    x_oh_sv_pinv = x_oh_svd[1].copy()
    zero_sv = np.isclose(x_oh_sv_pinv, 0)
    x_oh_sv_pinv[zero_sv] = 0
    x_oh_sv_pinv[~zero_sv] = 1. / x_oh_sv_pinv[~zero_sv]
    x_oh_pinv = (x_oh_svd[2].T, x_oh_sv_pinv[:, np.newaxis], x_oh_svd[0].T)

    y_oh = csc_matrix((np.ones(l), (range(l), y)))

    e = []

    for it in range(1, max_iter):

        h0 = v
        h1 = x_oh * w
        p = np.exp(h0 + h1)
        p /= p.sum(1)

        p_hot = p[range(l), y]
        e.append(2 * (1 - p_hot).mean())

        dh = y_oh - p
        v = (h0 + dh).mean(0)

        w = x_oh_pinv[2].dot(h1 + dh)
        w = np.multiply(x_oh_pinv[1], w)
        w = x_oh_pinv[0] * w

        v -= v.mean()
        w -= w.mean(1)
        for j in range(n):
            j1, j2 = j * m, (j + 1) * m
            w[j1:j2] -= w[j1:j2].mean(0)

        print it, np.linalg.norm(v_true - v), np.linalg.norm(w_true - w)

    return v, w, e


v, w, e = fit(x, y)

fig, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].plot(e, 'k-')
lo = min(v.min(), w.min())
hi = max(v.max(), w.max())
grid = np.linspace(lo, hi)
ax[1].plot(grid, grid, 'k--', alpha=0.5)
ax[1].scatter(np.asarray(v).flatten(), v_true, c='r', s=10)
ax[1].scatter(np.asarray(w).flatten(), w_true.flatten(), c='b', s=1)
ax[0].set_xlabel('iteration')
ax[0].set_ylabel('$E$')
ax[1].set_xlabel('fitted')
ax[1].set_ylabel('true')
plt.tight_layout()
plt.show()
