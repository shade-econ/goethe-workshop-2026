"""
Simple partial equilibrium transition code for r and y shocks in sim model
Adapted from example iteration in lecture1_sim.ipynb
"""

import numpy as np
import sim_steady_state_fast as sim

def transition(ss, T, dr=None, dy=None):
    dr = np.zeros(T) if dr is None else dr
    dy = np.zeros((T, len(ss['y']))) if dy is None else dy
    calib = {k: ss[k] for k in ('a_grid', 'Pi', 'beta', 'eis')}
        
    # backward iteration to get policies
    Va = ss['Va']
    a, c = np.empty((T, *ss['a'].shape)), np.empty((T, *ss['c'].shape))
    for t in reversed(range(T)):
        Va, a[t], c[t] = sim.backward_iteration(
            **{**calib, 'Va': Va, 'y': ss['y'] + dy[t], 'r': ss['r'] + dr[t]}
        )

    # forward iteration to get distributions and aggregates
    D = ss['D']
    A, C = np.empty(T), np.empty(T)
    for t in range(T):
        A[t], C[t] = np.vdot(a[t], D), np.vdot(c[t], D)
        a_i, a_pi = sim.interpolate_lottery_loop(a[t], ss['a_grid'])
        D = sim.forward_iteration(D, ss['Pi'], a_i, a_pi)

    return A, C
