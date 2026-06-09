# 2026 Goethe heterogeneous-agent macro workshop

**Note: This repository is still in progress and will be updated Tuesday and Wednesday with additional lectures.**

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

2. [Intro to HANK: Fiscal Policy](https://shade-econ.github.io/goethe-workshop-2026/lecture2_fiscal_policy.pdf), Ludwig Straub. [[notebook](https://github.com/shade-econ/goethe-workshop-2026/blob/main/notebooks/lecture2_fiscal.ipynb)] [key papers: [IKC](https://shade-econ.github.io/ikc/ikc.pdf) and [Annual Review](https://shade-econ.github.io/annual-review/annual_review_hank.pdf)]

3. [Calculating and Using Sequence-Space Jacobians](https://shade-econ.github.io/goethe-workshop-2026/lecture3_jacobians.pdf), Matthew Rognlie. [[notebook](https://github.com/shade-econ/goethe-workshop-2026/blob/main/notebooks/lecture3_sequence_space.ipynb)] [key paper: [SSJ](https://shade-econ.github.io/sequence_space_jacobian.pdf)]

   * See end of notebook for hands-on implementation of the fake news algorithm, which is generalized in [`sim_fake_news.py`](https://github.com/shade-econ/goethe-workshop-2026/blob/main/notebooks/sim_fake_news.py). Also see this [note from a previous class](https://mrognlie.github.io/econ411-3/econ411_3_lecture7_supplement.pdf) explaining the algorithm.

4. [Intro to HANK: Monetary Policy](https://shade-econ.github.io/goethe-workshop-2026/lecture4_monetary.pdf), Adrien Auclert. [[notebook](https://github.com/shade-econ/goethe-workshop-2026/blob/main/notebooks/lecture4_monetary.ipynb)] [key paper: [Annual Review](https://shade-econ.github.io/annual-review/annual_review_hank.pdf)]

5. [SSJ toolkit and approach](https://shade-econ.github.io/goethe-workshop-2026/lecture5_ssj_toolkit.pdf), Matthew Rognlie. [[notebook](https://github.com/shade-econ/goethe-workshop-2026/blob/main/notebooks/lecture5_ssj_toolkit.ipynb)] [[SSJ toolkit website](https://github.com/shade-econ/sequence-jacobian/)]

### Tuesday, June 9
6. [Monetary policy topics](https://shade-econ.github.io/goethe-workshop-2026/lecture6_monetary_topics.pdf), Adrien Auclert. [[notebook](https://github.com/shade-econ/goethe-workshop-2026/blob/main/notebooks/lecture6_monetary_topics.ipynb)] [key paper: [Annual Review](https://shade-econ.github.io/annual-review/annual_review_hank.pdf)]
