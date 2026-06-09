import numpy as np
from numpy.fft import irfft, rfft
from scipy.sparse.linalg import LinearOperator, gmres

# Multicountry IKC solved by GMRES, preconditioned by T(j^{-1}).


def solve(M, A, Pi, dG, dT, dB, tol=1e-9, verbose=True):
    T, N = len(M), len(Pi)
    K = 2*T - 1

    # Invert the block symbol frequency by frequency; apply_precond applies
    # the Toeplitz operator with symbol j(z)^{-1}.
    inv_symbol_rfft = np.linalg.inv(block_symbol_rfft(M, A, Pi))

    def apply_precond(x):
        x_rfft = rfft(x.reshape(T, N), K, axis=0)
        y_rfft = inv_symbol_rfft @ x_rfft[:, :, np.newaxis]
        return irfft(y_rfft, K, axis=0)[:T, :, 0].ravel()

    precond = LinearOperator((N*T, N*T), apply_precond, dtype=float)

    def system(x):
        dY = np.asarray(x, dtype=float).reshape(T, N)
        res = dY.copy()
        res -= M @ dY @ Pi                  # IKC residual: dY - M dY Pi
        res[:, 0] = A @ dY.sum(axis=1)      # replace country 0 with world asset clearing
        return res.ravel()

    sys = LinearOperator((T*N, T*N), system, dtype=float)

    counter = 0

    def report(pr_norm):
        nonlocal counter
        counter += 1
        if verbose:
            print(f"Iteration {counter}")
            print(pr_norm)

    partialY = dG - M @ dT @ Pi
    rhs = partialY.copy()
    rhs[:, 0] = dB.sum(axis=1) + A @ dT.sum(axis=1)
    dY, info = gmres(sys, rhs.ravel(), M=precond, rtol=tol,
                     callback_type="pr_norm", callback=report)
    if info != 0:
        raise RuntimeError(f"GMRES did not converge: info={info}")

    dY = dY.reshape(T, N)
    dY_alt = M @ dY @ Pi + partialY
    err = np.max(np.abs(dY_alt - dY))
    if verbose:
        print(f"Max error in solution is {err:.3e}")

    return dY


def toeplitz_symbol_rfft(J):
    """rFFT-grid values of the Toeplitz symbol from bottom/right diagonals."""
    return rfft(np.concatenate((J[-1, ::-1], J[:-1, -1])))


def block_symbol_rfft(M, A, Pi):
    """rFFT-grid values of the block symbol for IKC plus asset clearing."""
    T, N = len(M), len(Pi)
    m_rfft, a_rfft = toeplitz_symbol_rfft(M), toeplitz_symbol_rfft(A)

    symbol_rfft = np.empty((T, N, N), dtype=np.complex128)

    # Row 0 is world asset-market clearing: A maps every country's dY into
    # world assets, replacing one redundant IKC equation.
    symbol_rfft[:, 0, :] = a_rfft[:, None]

    # Rows 1..N-1 are IKC residuals:
    # dY_i - sum_j Pi_{i,j} M dY_j.
    symbol_rfft[:, 1:, :] = -m_rfft[:, None, None] * Pi.T[None, 1:, :]
    for i in range(1, N):
        symbol_rfft[:, i, i] += 1

    return symbol_rfft
