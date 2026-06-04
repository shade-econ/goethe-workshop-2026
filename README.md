# 2026 Goethe heterogeneous-agent macro workshop

**Note: This repository is in progress and will be updated as the workshop gets closer.**

This repository provides materials and code for the 2026 Goethe Macro Training School for Heterogeneous-Agent Macroeconomics, to be held June 8–10 at Goethe University Frankfurt. (See hourly schedule [here](https://sequence-space.com/goethe/).)

Slides for each lecture will be included below. Most lectures will have accompanying notebooks, with code that generates figures from the slides or otherwise illustrates the methods of the lecture. Some notebooks require support files that are also contained in the `notebooks/` folder.

All code is in Python and requires the standard numerical Python libraries (`numpy`, `scipy`, `matplotlib`, `numba`, `pandas`). Later lecture notebooks, starting with lecture 5, will often require installing the [sequence-space Jacobian toolkit](https://github.com/shade-econ/sequence-jacobian).

Three key references for the workshop are:
* [Fiscal and Monetary Policy with Heterogeneous Agents](https://shade-econ.github.io/annual-review/annual_review_hank.pdf) [[repo](https://github.com/shade-econ/annual-review)], Annual Review of Economics (Aug 2025). This introduces the canonical model and covers a variety of fiscal and monetary policy exercises.
* [The Intertemporal Keynesian Cross](https://shade-econ.github.io/ikc/ikc.pdf) [[repo](https://shade-econ.github.io/ikc/)], Journal of Political Economy (Dec 2024). This covers fiscal policy, intertemporal MPCs, and the intertemporal Keynesian cross framework in more depth.
* [Using the Sequence-Space Jacobian to Solve and Estimate Heterogeneous-Agent Models](https://shade-econ.github.io/sequence_space_jacobian.pdf), Econometrica (Sep 2021). This covers sequence-space Jacobians as a solution tool, including the fake news algorithm, solving general equilibrium models using DAGs, and estimation.

Feel free to also check out the material from the [spring 2025](https://github.com/shade-econ/nber-workshop-2025) and [spring 2023](https://github.com/shade-econ/nber-workshop-2023) NBER workshops.

# Lectures

### Monday, June 8
1. [The Standard Incomplete Markets (SIM) Model](https://shade-econ.github.io/goethe-workshop-2026/lecture1_sim.pdf), Matthew Rognlie. [[notebook](https://github.com/shade-econ/goethe-workshop-2026/blob/main/notebooks/lecture1_sim.ipynb)]

   * For more on computation and the SIM model, see the [supplementary notebook on computation](https://github.com/shade-econ/goethe-workshop-2026/blob/main/supplements/sim_steady_state_computation.ipynb) and [accompanying video lectures from a previous year](https://github.com/shade-econ/nber-workshop-2023/tree/main?tab=readme-ov-file#first-lecture-online). We recommend watching the video lectures before the workshop. Also see the [additional notebook on speeding up code](https://github.com/shade-econ/goethe-workshop-2026/blob/main/supplements/sim_steady_state_speed.ipynb). The two notebooks explain the details of [`sim_steady_state.py`](https://github.com/shade-econ/goethe-workshop-2026/blob/main/notebooks/sim_steady_state.py) and [`sim_steady_state_fast.py`](https://github.com/shade-econ/goethe-workshop-2026/blob/main/notebooks/sim_steady_state_fast.py), two modules for basic SIM steady-state computation.
