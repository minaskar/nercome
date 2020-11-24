import numpy as np


def cov(m, fs=2.0/3.0, n=100, rowvar=True):

    if rowvar:
        m = m.T

    nsamples, ndim = m.shape

    assert fs < 1.0
    s = int(fs * nsamples)

    idx = np.arange(nsamples)

    cov = np.zeros((ndim, ndim))

    for i in range(n):

        choice = np.random.choice(idx, size=s, replace=False)
        mask1 = np.in1d(idx, choice)
        mask2 = ~mask1
        x1 = m[mask1]
        x2 = m[mask2]

        cov1 = np.cov(x1.T)
        cov2 = np.cov(x2.T)

        _, eigvec = np.linalg.eigh(cov1)
        D = np.diag(np.diag(eigvec.T @ cov2 @ eigvec))
        cov += eigvec @ D @ eigvec.T

    return cov / n