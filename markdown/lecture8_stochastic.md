## Slide 1: Stochastic economies and estimation

Adrien Auclert

Goethe Heterogeneous-Agent Macro Workshop, 2026

## Slide 2: Introduction

- **Workshop so far:** MIT shocks (nonlinear and linear)
- Fine object for very rare events, but for business-cycle-like shocks, **rational expectations** is more useful benchmark
  - How useful are MIT shocks for rational expectations solution?
- Our answer (over today and tomorrow’s lectures): **very useful!**
  - In fact, for practical purposes, **MIT shocks are all you need!**  
    (“certainty correspondence”)
  - Today: first instance of this: MIT shocks are all you need **to first order**  
    (“certainty equivalence”). Apply this to **simulations + estimation**.

## Slide 3: First-order certainty equivalence

First-order certainty equivalence

## Slide 4: Setup

- Consider general macro model:

$$
F\left(X_{t-1}, X_t, \mathbb{E}_t[X_{t+1}], \epsilon_t\right)=0
$$

- $X_t \in \mathbb{R}^n$ are endogenous variables  
  [het-agent applications: $n$ large, eg $n = 2{,}000$]

- $\epsilon_t \in \mathbb{R}$ are exogenous innovations (realized shock process)  
  [naturally extends to $>1$ shocks]

  - Distributed $\epsilon_t = \sigma_R \cdot \bar{\epsilon}_t$ with $\bar{\epsilon}_t$ iid, mean 0, variance 1, and symmetric density

- Expectations $\mathbb{E}_t[\cdot]$ are taken assuming future distribution of $\epsilon_t$ is $\sigma \cdot \bar{\epsilon}_t$

  - **Rational expectations:** $\sigma = \sigma_R$  
    (perceived distribution of future $\epsilon_t$ = truth)

  - **Perfect foresight:** $\sigma = 0$  
    (agents think all future $\epsilon_t$ will realize to 0 for sure)

- **Deterministic steady state** $X \in \mathbb{R}^n$ solves $F(X,X,X,0)=0$  
  (i.e. $\sigma = \sigma_R = 0$)

## Slide 5: PE SIM example

- For concreteness, consider the PE SIM model

$$
V_t(e,a)=\max_{c,a'} u(c)+\beta \mathbb{E}_{e'}[V_{t+1}(e',a')\mid e]
$$

$$
\text{s.t.}\quad a' + c = (1+r)a + Z_t e \qquad a' \ge 0
$$

- Aggregate income $Z_t$ follows AR(1) process:

$$
Z_t - 1 = \rho(Z_{t-1}-1)+\epsilon_t
$$

- Here, $X_t \equiv (v_t,\phi_t,C_t,Z_t)$ where $v_t$ stores marginal value $V_{a,t}$ over gridpoints $(e,a)$, $\phi_t$ stores the p.d.f, and $C_t$ aggregates consumption policy over distribution

- Equations describing $F$: the law of motion of $Z_t$, plus

$$
v_t = \mathcal{V}(Z_t,\mathbb{E}_t v_{t+1})
$$

$$
\phi_t = \Lambda(Z_t,\mathbb{E}_t v_{t+1},\phi_{t-1})
$$

$$
C_t = \mathcal{C}(Z_t,\mathbb{E}_t v_{t+1},\phi_{t-1})
$$

Dynamic programming: expectations enter via $\mathbb{E}_t[v_{t+1}]$.

## Slide 6: (Stochastic) sequence space solution

- Given $\sigma$, consider **nonlinear sequence-space solution** to $F$:

$$
X_t = \mathcal{X}(\sigma;\epsilon_t,\epsilon_{t-1},\epsilon_{t-2},\ldots)
$$

[Lan-Meyer-Gohde, Lombardo-Uhlig]

[eg, obtained from stable state-space solution $X_t = g(X_{t-1},\epsilon_t;\sigma)$]

- We are going to relate this to the **perfect-foresight solution**

$$
X_t^{PF} = \mathcal{X}(0;\epsilon_t,\epsilon_{t-1},\epsilon_{t-2},\ldots)
$$

[eg, obtained from $\infty$-long sequence of repeated-surprise MIT shocks]

- Use **perturbation approach:** linearize $\mathcal{X}$ around $\sigma = \sigma_R = 0$ (i.e. $\epsilon = 0$)

- Helpful result:

$$
\mathcal{X}(\sigma;\epsilon_t,\epsilon_{t-1},\ldots)
=
\mathcal{X}(-\sigma;\epsilon_t,\epsilon_{t-1},\ldots)
$$

so, e.g.,

$$
\mathcal{X}_\sigma(0)=0
$$

## Slide 7: MIT shock impulse response

- Special case of $X^{PF}$ is the MIT shock impulse response

$$
X_j^{MIT}(\nu) \equiv \mathcal{X}(0;0,\ldots,0,\nu,0,\ldots)
$$

where $\nu$ is at position $j$.

- Can compute $\{X_j^{MIT}(\nu)\}_j$ with nonlinear perfect foresight starting from s.s.

  - cf lecture 1 and 3 methods!

- **Next:** why this is sufficient to get the first-order solution with aggregate risk!

## Slide 8: Certainty equivalence

- Expand $X_t = \mathcal{X}(\sigma,\epsilon_t,\epsilon_{t-1},\ldots)$ to first order in $(\sigma,\epsilon)$:

$$
X_t
=
X
+
\mathcal{X}_\sigma \sigma
+
\frac{\partial \mathcal{X}}{\partial \epsilon_0}(0)\epsilon_t
+
\frac{\partial \mathcal{X}}{\partial \epsilon_{-1}}(0)\epsilon_{t-1}
+
\cdots
+
O(\sigma^2)
$$

Visual annotations on the slide:
- The $\mathcal{X}_\sigma \sigma$ term is crossed out.
- “Symmetry: Steady state unchanged”
- “No anticipated risk, no past realization”

- So, to first order, $X_t$ follows linear MA process, with coefficients equal to

$$
\frac{\partial \mathcal{X}}{\partial \epsilon_{-j}}(0)
=
\frac{dX_j^{MIT}}{d\nu}(0)
\equiv
\mathcal{X}_j
$$

**Certainty equivalence.** To first order, $X_t$ follows a linear MA process whose coefficients are given by the first order MIT shock impulse response of $X$ to $\epsilon$ [Boppart-Krusell-Mitman].

## Slide 9: Implementation using SSJ

- To first-order, $X_t$ (so all its elements!) follows linear $MA(\infty)$

$$
X_t
=
X
+
\mathcal{X}_0\epsilon_t
+
\mathcal{X}_1\epsilon_{t-1}
+
\mathcal{X}_2\epsilon_{t-2}
+
\cdots
+
O(\sigma^2)
$$

$$
\mathcal{X}_j
\equiv
\frac{dX_j^{MIT}}{d\nu}(0)
$$

- Convenient: we can use SSJ to very effectively get $\mathcal{X}_j$!

- For instance, suppose that we want the behavior of aggregate outcome $X_t$ to monetary shock $r_s$ in the canonical HANK model, with $MA(\infty)$ shock process

$$
r_t
=
r
+
\mathcal{R}_0\epsilon_t
+
\mathcal{R}_1\epsilon_{t-1}
+
\mathcal{R}_2\epsilon_{t-2}
+
\cdots
$$

- Then we get the SSJ $G^{X,r}$ of $X$ to $r$, then apply vector-matrix multiplication

$$
(\mathcal{X}_0,\mathcal{X}_1,\mathcal{X}_2,\ldots)^\prime
=
G^{X,r}
\cdot
(\mathcal{R}_0,\mathcal{R}_1,\mathcal{R}_2,\ldots)^\prime
$$

## Slide 10: Applications: simulation, second moments, estimation

Applications: simulation, second moments, estimation

## Slide 11: Application to simulation

- Suppose we want to do stochastic simulations of $X_t$. Since

$$
X_t
\simeq
X
+
\mathcal{X}_0\epsilon_t
+
\mathcal{X}_1\epsilon_{t-1}
+
\mathcal{X}_2\epsilon_{t-2}
+
\cdots
\qquad
(\star)
$$

- Once we have $\mathcal{X}_t$, we can just simulate by applying $(\star)$!

Visible code screenshot:

```python
rho = 0.9
dishock = rho**np.arange(T)
dY = G['Y', 'ishock'] @ dishock
```

Output indicator:

```text
✓ 0.0s
```

Visible code screenshot:

```python
sigma = 0.005
Tsim = 1_000_000             # will simulate for 1 million quarters
np.random.seed(40)
eps = np.random.randn(Tsim+T) # draw epsilons for T additional pre-per
dY_sim = np.empty(Tsim)
for t in range(Tsim):
    # at each t, take window of current up to T-1 previous epsilons
    # take dot product with MA coefficients implied by MIT shock
    dY_sim[t] = np.dot(dY, eps[t:t+T][::-1]) * sigma
```

Output indicator:

```text
✓ 0.7s
Python
```

## Slide 12: Simulating output response to monetary shock

Chart axes:
- x-axis: Quarter $t$
- y-axis: % change in output $dY_t$

Image note: Line chart of simulated output response over quarters 0–40. The series starts slightly negative, briefly rises above zero near quarter 12, then trends more negative, reaching around $-1.4$ near quarter 30 and ending near $-1.0$. Generated by `notebooks/lecture8_stochastic.ipynb`; figure `lecture8_output_monetary.pdf`.

## Slide 13: Application to second moments

- Suppose we want to obtain second moments of $X_t$ (with $\sigma_R=\sigma$). Have

$$
X_t
\simeq
X
+
\mathcal{X}_0\epsilon_t
+
\mathcal{X}_1\epsilon_{t-1}
+
\mathcal{X}_2\epsilon_{t-2}
+
\cdots
\qquad
(\star)
$$

and we can just apply time series formulas to get these!

- For instance ergodic variance is area under squared impulse response

$$
\operatorname{Var}(X_t)
=
\sigma^2
\sum_{j=0}^{\infty}
(\mathcal{X}_j)^2
$$

- More generally

$$
\operatorname{Cov}(X_t,X_{t-k})
=
\sigma^2
\sum_{j=0}^{\infty}
\mathcal{X}_j\mathcal{X}_{j+k}
$$

## Slide 14: Implementation: second moments in HANK model

Visible code screenshot:

```python
var_dY = sigma**2 * (dY @ dY)
```

Output indicator:

```text
✓ 0.0s
Python
```

Compare to the sample variance to make sure this is right. Note that it's close but not exact, reflecting Monte Carlo error:

Visible code screenshot:

```python
sample_var_dY = (dY_sim - dY_sim.mean()) @ (dY_sim - dY_sim.mean()) / Tsim
print(f"Sample variance: {sample_var_dY:.4e} | theoretical : {var_dY:.4e}")
```

Output indicator:

```text
✓ 0.0s
Python
```

Visible output:

```text
Sample variance: 3.1761e-05 | theoretical : 3.1870e-05
```

## Slide 15: Application to impulse-response matching

- Straightforward to estimate by **matching impulse responses**

- Suppose model parameters are $\theta$, giving impulse response $IRF_t(\theta)$, and identified empirical impulse response $\widehat{irf}_t$

- Then we can just search for

$$
\hat{\theta}
=
\arg\min
\left(IRF(\theta)-\widehat{irf}\right)^\prime
V^{-1}
\left(IRF(\theta)-\widehat{irf}\right)
$$

where, e.g. $V$ has sample variances of $\widehat{irf}_t$ (Christiano, Eichenbaum, Evans)

- This is especially fast if we do not have to recompute all Jacobians for $IRF(\theta)$, such as we estimate shock process parameters ($G$ unchanged!)

## Slide 16: Application to method of moments

- Also straightforward to estimate by **matching moments**

- Suppose model parameters are $\theta$, giving model moments $M(\theta)$

  - eg second moments, HP-filtered moments, regression coefficients…

- Then we can confront to empirical counterparts $\hat{m}$ by taking

$$
\hat{\theta}
=
\arg\min
\left(M(\theta)-\hat{m}\right)^\prime
V^{-1}
\left(M(\theta)-\hat{m}\right)
$$

where, e.g. $V$ is model’s

$$
\mathbb{E}\left[M(\theta)M(\theta)^\prime\right]
$$

(Minimum distance estimation, aka “simulated” method of moments)

## Slide 17: Application to likelihood-based estimation

- Let’s assume that model innovations $\epsilon_t$ are normally distributed

- Given parameter $\theta$, first-order process followed by $X_t$ is

$$
X_t
\simeq
X(\theta)
+
\mathcal{X}_0(\theta)\epsilon_t
+
\mathcal{X}_1(\theta)\epsilon_{t-1}
+
\mathcal{X}_2(\theta)\epsilon_{t-2}
+
\cdots
$$

- Given data $X$, we know the (log) likelihood function

$$
\mathcal{L}(X;\theta)
=
-\frac{1}{2}\log \det V(\theta)
-
\frac{1}{2}X^\prime V(\theta)^{-1}X
$$

where $V(\theta)$ is variance-covariance matrix of $X_t$ at all lags

- In practice, use Cholesky decomposition to calculate $\det V$ and $X^\prime V^{-1}X$

## Slide 18: Application to likelihood-based estimation

- Given likelihood function $\mathcal{L}(X;\theta)$ we can in turn do:

  - Maximum likelihood estimation

$$
\hat{\theta}
=
\arg\max \mathcal{L}(Y,\theta)
$$

  - Bayesian estimation given prior $p(\theta)$: find posterior distribution

$$
p(\theta\mid Y)
=
\frac{\mathcal{L}(Y\mid\theta)p(\theta)}{p(Y)}
\propto
\mathcal{L}(Y\mid\theta)p(\theta)
$$

- For instance, posterior mode just solves

$$
\hat{\theta}
=
\arg\max p(\theta\mid Y)
$$

[More complex: simulate from posterior using MCMC]

## Slide 19: Practical implementation: estimate HANK model!

- Notebook estimates HANK model with

  - 3 shocks (government spending, TFP, monetary policy)

  - 3 observables (output, inflation, interest rates)

- Look for

  - shock process parameters (assumed AR(1)’s: $3\sigma + 3\rho$)

  - coefficient on Taylor rule $\phi_\pi$, fiscal rule $\phi_\tau$, slope of Phillips curve $\kappa_w$

- Done in less than a minute on a laptop!

## Slide 20: Conclusion

- MIT shocks from SSJ are all you need for first-order solution!

  - Simulation, model moments, estimation

- Obtain same answer as state-space models linearized to first order

  - But speed gains can be significant

- More to come in next lecture, and then tomorrow: beyond certainty equivalence, MIT shocks are still all you need!
