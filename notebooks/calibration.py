import json
from pathlib import Path

import numpy as np

import sim_steady_state_fast as sim


def load_betas(path="betas.json"):
    path = Path(__file__).with_name(path)
    with open(path) as f:
        return json.load(f)


def make_calibration(lowA=False):
    """Default household calibration. See lecture1_sim.ipynb for details."""
    rho_e = 0.91**(1/4)     # annual rho=0.91 from IKC
    sd_e = 0.92             # cross-sectional sd from IKC
    n_e = 11                # 11 points for Rouwenhorst approximation
    e, _, Pi_e = sim.discretize_income(rho_e, sd_e, n_e)

    a_grid = sim.discretize_assets(0, 4000, 400)

    q = 0.01                # draw new beta every 25 years
    pi_b = np.array([1/4, 1/4, 1/4, 1/4])
    Pi_b = (1-q)*np.eye(4) + q*np.outer(np.ones(4), pi_b)

    Pi = np.kron(Pi_b, Pi_e)
    e = np.kron(np.ones(4), e)

    # Default is calibration that targets A=500% of GDP, but 'lowA' gives 100%
    key = "A_100" if lowA else "A_500"
    betas = load_betas()[key]
    beta_hi, dbeta = betas["beta_hi"], betas["dbeta"]
    beta = np.kron([beta_hi-3*dbeta, beta_hi-2*dbeta, beta_hi-dbeta, beta_hi],
                   np.ones(n_e))[:, np.newaxis]

    calib = dict(a_grid=a_grid, Pi=Pi, y=0.7*e, r=0.02/4, beta=beta, eis=1)
    return calib, e
