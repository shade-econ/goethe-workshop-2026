## Slide 1: The Standard Incomplete Markets (SIM) Model

Matthew Rognlie

Goethe Heterogeneous-Agent Macro Workshop, 2026

## Slide 2: Individual household problem

## Slide 3: The “standard incomplete markets” model (steady state)

* Individual household $i$ optimizes

$$
\max_{\{a_{it},c_{it}\}_{t=0}^{\infty}} \mathbb{E}_0 \sum_{t=0}^{\infty} \beta^t u(c_{it})
$$

subject to period-by-period budget constraint and borrowing constraint

$$
a_{it} + c_{it} = (1+r)a_{i,t-1} + Z e_{it}, \qquad a_{it} \ge \underline{a}.
$$

* Exogenous income state $e_{it}$ follows Markov chain, which we’ll usually normalize to 1; $Z$ scales aggregate after-tax income.
* Initial assets $a_{i,-1}$ taken as given, standard assumptions on $u$ (CRRA).

## Slide 4: Can convert sequential form to Bellman equation

Sequential form:

$$
\max_{\{a_{it},c_{it}\}_{t=0}^{\infty}} \mathbb{E}_0 \sum_{t=0}^{\infty} \beta^t u(c_{it})
$$

$$
a_{it} + c_{it} = (1+r)a_{i,t-1} + Z e_{it}, \qquad a_{it} \ge \underline{a}.
$$

Bellman equation:

$$
V(e,a)=\max_{c,a'} u(c) + \beta \mathbb{E}\left[V(e',a')\mid e\right]
$$

subject to

$$
a' + c = (1+r)a + Ze, \qquad a' \ge \underline{a}.
$$

Solved by policies $a'(e,a)$ and $c(e,a)$ in two state variables, exogenous income state $e$ and endogenous asset state $a$.

**Image note:** Red arrows show the conversion from the sequential problem and constraints to the Bellman equation, then from the Bellman equation to policy functions.

## Slide 5: Solving the Bellman equation

* Policies $a'(e,a)$ and $c(e,a)$ satisfy standard first-order condition

$$
u'(c) \ge \beta \mathbb{E}\left[V_a(e',a')\mid e\right]
$$

with equality unless borrowing constraint binds, and envelope condition

$$
V_a(e,a) = (1+r)u'(c).
$$

* Combined, same as sequential Euler equation

$$
u'(c_{it}) \ge \beta(1+r)\mathbb{E}_t\left[u'(c_{i,t+1})\right].
$$

* Can use first-order and envelope conditions to iterate backward on $V_a$ and policies.

  * Best way: interpolation and “endogenous gridpoints” (Carroll 2006).
  * Iterating until convergence gives $V_a$ and steady-state policies on a grid.

## Slide 6: See computation supplement (on GitHub) for more!

```python
def backward_iteration(Va, Pi, a_grid, y, r, beta, eis):
    # step 1: discounting and expectations
    Wa = (beta * Pi) @ Va

    # step 2: solving for asset policy using the first-order condition
    c_endog = Wa**(-eis)
    coh = y[:, np.newaxis] + (1+r)*a_grid

    a = np.empty_like(coh)
    for e in range(len(y)):
        a[e, :] = np.interp(coh[e, :], c_endog[e, :] + a_grid, a_grid)

    # step 3: enforcing the borrowing constraint and backing out consumption
    a = np.maximum(a, a_grid[0])
    c = coh - a

    # step 4: using the envelope condition to recover the derivative of the value function
    Va = (1+r) * c**(-1/eis)

    return Va, a, c
```

Basic backward iteration takes just 9 lines of standard Python code.

Consolidated in `sim_steady_state.py`, GitHub links to supplementary notebook, video lectures, and also 2x sped-up version.

## Slide 7: Distribution of households

## Slide 8: Solved household problem, now aggregate

* We’ve solved problem facing individual household.
* Now aggregate into economies with a continuum of such households.

  * Soon will put in general equilibrium …
  * But for now interested in properties of “partial equilibrium” model, i.e. taking return $r$ as given.
* This is a heterogeneous-agent economy.

  * Has a distribution of households across the two states, $e$ and $a$.

## Slide 9: What is distribution of households?

* In principle, it’s a measure $\mu$.
* If finitely many $e$, then can define $\mu(e,\mathbb{A})$ separately for each $e$, as measure on subsets $\mathbb{A}$ of the asset space.
* Law of motion:

$$
\mu_{t+1}(e',\mathbb{A}) =
\sum_e \mu_t\left(e,(a')^{-1}(e,\mathbb{A})\right)\cdot P(e,e')
$$

where $P(e,e')$ is transition probability, $(a')^{-1}(e,\cdot)$ is inverse of policy $a'(e,\cdot)$.

* Measure of $\mathbb{A}$ today is sum of measures yesterday that send you there today.

## Slide 10: Why measure?

* You might want some nice density function …

  * But if $\beta(1+r)<1$, there will be a positive mass at borrowing constraint.
  * (If $\beta(1+r)\ge 1$, can show everyone’s assets will diverge to $\infty$, so we generally don’t consider that case…)
  * If finitely many $e$, this implies discrete distribution with only mass points!

    * Countably many histories of $e$ since last time hitting constraint.
* So for generality, we assume an arbitrary measure over assets.

  * Will revisit much later when we build a “smoother” model.

## Slide 11: Calculating distribution in practice

```python
def get_lottery(a, a_grid):
    # step 1: find the i such that a' lies between gridpoints a_i and a_(i+1)
    a_i = np.searchsorted(a_grid, a) - 1

    # step 2: obtain lottery probabilities pi
    a_pi = (a_grid[a_i+1] - a)/(a_grid[a_i+1] - a_grid[a_i])

    return a_i, a_pi
```

```python
@numba.njit
def forward_policy(D, a_i, a_pi):
    Dend = np.zeros_like(D)
    for e in range(a_i.shape[0]):
        for a in range(a_i.shape[1]):
            # send pi(e,a) of the mass to gridpoint i(e,a)
            Dend[e, a_i[e,a]] += a_pi[e,a]*D[e,a]

            # send 1-pi(e,a) of the mass to gridpoint i(e,a)+1
            Dend[e, a_i[e,a]+1] += (1-a_pi[e,a])*D[e,a]

    return Dend
```

Approximate distribution by point masses on finite grid; when asset policy $a'(e,a)$ lies between two gridpoints, convert it to “lottery” between gridpoints with same expectation.

Also in `sim_steady_state.py`, notebook, and videos.

## Slide 12: Steady state of aggregate model

## Slide 13: What is a steady state of model?

* Consists of:

  * policy functions $a'(e,a)$ and $c'(e,a)$ that solve Bellman equation
  * distribution $\mu(e,\mathbb{A})$ that satisfies steady-state law of motion

$$
\mu(e',\mathbb{A}) =
\sum_e \mu\left(e,(a')^{-1}(e,\mathbb{A})\right)\cdot P(e,e')
$$

* Can show such a “stationary distribution” exists and is unique if $\beta(1+r)<1$.
* Aggregate assets and consumption:

$$
A = \int a,d\mu = \int a'(e,a),d\mu,
\qquad
C = \int c,d\mu.
$$

## Slide 14: Nice features of model

* Captures key features of consumption-saving problem with risk.

  * income smoothing, precautionary savings, etc.
* Endogenously generates wealth distribution (of assets $a$).
* Consistent with high marginal propensities to consume (MPCs) out of cash on hand, here

$$
\operatorname{mpc}(e,a) \equiv \frac{\partial c(e,a)/\partial a}{1+r}.
$$

* Unlike representative-agent model, steady-state asset demand not infinitely elastic in $r$, so $r$ can be endogenous.
* Easy to extend: other shocks, preference heterogeneity, endogenous labor, life-cycle structure, other assets…

## Slide 15: Consumption functions: increasing, concave

**Image note:** Line chart of consumption $c(e,a)$ against assets $a$. The x-axis is “assets $a$” with tick labels 0.0, 0.2, 0.4, 0.6, 0.8, 1.0. The y-axis is “consumption $c(e,a)$” with tick labels 0.1, 0.2, 0.3, 0.4. Legend entries are $e=0.04$, $e=0.06$, $e=0.11$, $e=0.21$, and $e=0.37$. Each consumption function is increasing and concave; higher-$e$ curves lie above lower-$e$ curves. Generated by `notebooks/lecture1_sim.ipynb`; figure `lecture1_fig1.pdf`.

## Slide 16: Buffer-stock behavior for each household

“Target” asset levels increase dramatically as we go to higher $e$, leading to inequality in stationary wealth distribution.

**Image note:** Line chart of net saving $a'(e,a)-a$ against assets $a$. The x-axis is “assets $a$” with tick labels 0, 2, 4, 6, 8, 10, 12, 14, 16. The y-axis is “net saving $a'(e,a)-a$” with tick labels $-0.4$, $-0.2$, 0.0, 0.2, and a dashed horizontal zero line. Legend entries are $e=0.11$, $e=0.21$, $e=0.37$, $e=0.66$, and $e=1.18$. Higher-$e$ curves cross zero at higher asset levels. Generated by `notebooks/lecture1_sim.ipynb`; figure `lecture1_fig2.pdf`.

## Slide 17: Rich asset distribution, endogenous wealth inequality

**Image note:** CDF plot of all assets. The x-axis is “assets $a$” with tick labels 0, 10, 20, 30, 40, 50, 60, 70. The y-axis is “CDF $F(a)$ of all assets” with tick labels 0.2, 0.4, 0.6, 0.8, 1.0. The curve rises steeply at low asset levels and then flattens as assets increase. Generated by `notebooks/lecture1_sim.ipynb`; figure `lecture1_fig3.pdf`.

## Slide 18: Calibration of model

## Slide 19: What parameters do we need to calibrate?

* Calibrate to quarterly frequency.
* Income process $e$: [usually normalize average $e$ to 1, entire ss scales in $Z$]

  * calibrate as discrete approximation of lognormal AR(1)
  * annual persistence $\rho=0.91$, cross-sectional sd $\sigma=0.92$ (IKC paper), rough approximation of pretax income process in US
  * 11-point Rouwenhorst approximation (see supplement for details)
* Real rate $r$ to 2% annually, borrowing constraint $\underline{a}$ to 0, utility to $u(c)=\log c$.
* One parameter remains: discount factor $\beta$.

## Slide 20: Two common strategies for calibrating $\beta$

* Calibrate to hit target for aggregate assets, taken from data.

  * Our Ann Rev calibration: assets $A$ at 500% of GDP, given after-tax labor income $Z$ of 70% of GDP, following US.
  * (Some others target lower $A$, interpreted as some notion of “liquid” assets.)
* Calibrate to average marginal propensity to consume, also taken from data.

  * Our Ann Rev calibration: average income-weighted quarterly MPC of 0.2.
* Problem: tradeoff between two, $\beta$ that matches one fails other.

## Slide 21: Asset-MPC tradeoff as we vary $\beta$

**Image note:** Line chart of average quarterly MPC against assets as $\beta$ varies. The x-axis is “Assets (% of annual GDP)” with tick labels 0, 100, 200, 300, 400, 500, 600, 700, 800. The y-axis is “Average quarterly MPC” with tick labels 0.0, 0.2, 0.4, 0.6, 0.8, 1.0. Legend entries are “income-weighted” and “unweighted.” Dashed target lines appear at assets = 500% of annual GDP and MPC = 0.2. Generated by `notebooks/lecture1_sim.ipynb`; figure `lecture1_fig4.pdf`.

## Slide 22: Our solution: $\beta$ heterogeneity

* By mixing different $\beta$, we can target both aggregate assets and MPCs.
* Exogenous state is now $(\beta,e)$, can make $\beta$ either permanent or stochastic.

  * Stochastic limits polarization into “spenders” vs. “savers”.
* We’ll be inspired by Annual Review stochastic $\beta$ process (independent of $e$):

  * Four equispaced $\beta$s with equal shares, each household gets fresh $\beta$ draw 1% of time.
  * Loosely interpret as new draw of preferences every “generation” (25 years).
  * Calibrate to hit both asset (500% of GDP) and income-weighted MPC (0.2) targets.
  * Calibrated quarterly $\beta$s: approximately 0.94, 0.96, 0.98, 1.0.
  * [For next few lectures, will also calculate “bonds only” calibration (assets = 100% of GDP).]

## Slide 23: New vs. old asset-MPC tradeoff

(In $\beta$ heterogeneity line, we keep gap between high and low $\beta$ fixed as we vary the mean.)

**Image note:** Line chart of average income-weighted quarterly MPC against assets. The x-axis is “Assets (% of annual GDP)” with tick labels 0, 100, 200, 300, 400, 500, 600, 700. The y-axis is “Average inc-weighted quarterly MPC” with tick labels 0.0, 0.2, 0.4, 0.6, 0.8, 1.0. Legend entries are “original” and “$\beta$ heterogeneity.” Dashed target lines appear at assets = 500% of annual GDP and MPC = 0.2. The $\beta$ heterogeneity line stays near the 0.2 MPC target around 500% assets, unlike the original line. Generated by `notebooks/lecture1_sim.ipynb`; figure `lecture1_fig5.pdf`.

## Slide 24: Untargeted moment: Lorenz curve vs. US data

Model not bad at all since distribution is untargeted, but overstates “middle-class” wealth (50th to 90th percentiles), understates wealth in upper tail (difficult to match without other features).

**Image note:** Lorenz curve chart with x-axis “Population share” and y-axis “Wealth share,” both running from 0.0 to 1.0. Legend entries are “Model” and “SCF 2019.” A dotted 45-degree equality line is also shown. The model and SCF 2019 curves are close in the lower and middle portions, with differences in the upper tail. Generated by `notebooks/lecture1_sim.ipynb`; figure `lecture1_fig6.pdf`.

## Slide 25: Partial equilibrium dynamics

## Slide 26: Time-varying aggregate inputs to household problem

* Revisit individual household problem [ignoring $\beta$ process for notational simplicity]:

$$
\max_{\{a_{it},c_{it}\}_{t=0}^{\infty}} \mathbb{E}_0 \sum_{t=0}^{\infty} \beta^t u(c_{it})
$$

allowing returns $r_t^p$ and aggregate after-tax income $Z_t$ to vary over time:

$$
a_{it} + c_{it} = (1+r_t^p)a_{i,t-1} + Z_t e_{it},
\qquad
a_{it} \ge \underline{a}.
$$

* Add $p$ to emphasize that $r_t^p$ is ex-post return from $t-1$ to $t$, determined at date $t$.
* Assume distribution of $a_{i,-1}$ is steady state, perfect foresight over $\{r_t^p,Z_t\}_{t=0}^{\infty}$ from date 0 onward (“MIT shock”).

## Slide 27: Solution uses similar iterations to steady state

1. Start with $V_{aT}=V_{a,ss}$ and iterate backward $T$ times, using time-varying $r_t^p$ and $Z_t$ to obtain policies $a'_t(e,a)$, $c_t(e,a)$ at $t=0,\ldots,T-1$.

2. Start with distribution $\mu_0=\mu_{ss}$ and iterate forward $T-1$ times, using time-varying policy function $a'_t(e,a)$ to get $\mu_t(e,\cdot)$ at each $t$.

3. Aggregate policies $a'_t(e,a)$, $c_t(e,a)$ against $\mu_t(e,\cdot)$ at each $t$ to get $A_t$, $C_t$.

**Image note:** Timeline diagram showing backward iteration from terminal $V_{a,ss}$, forward iteration from initial $\mu_{ss}$, and aggregation at each time. Curved arrows indicate repeated backward and forward updates; ellipses indicate many intervening periods.

## Slide 28: Key observation: $r_t^p$ and $Z_t$ determine everything

* Given sequences of ex-post returns $r_t^p$ and aggregate after-tax income $Z_t$:

  * We can solve for time-varying policy functions $a'_t(e,a)$ and $c_t(e,a)$.
  * These imply a time-varying distribution $\mu_t(e,\cdot)$.
  * And together these imply time-varying $A_t$ and $C_t$.
* Hence, we can think of $A_t$ and $C_t$ as being functions of $\{r_s^p\}_{s=0}^{\infty}$ and $\{Z_s\}_{s=0}^{\infty}$.

  * These are sequence-space functions $\mathcal{A}_t(\{r_s^p,Z_s\})$ and $\mathcal{C}_t(\{r_s^p,Z_s\})$.
  * Plot around steady-state; later, compute derivatives (“sequence-space Jacobians”).

## Slide 29: Response to 0.1% $Z_s$ shocks at different dates $s$

Elevated spending out of income at other dates as well (will call these “intertemporal MPCs”).

**Image note:** Line chart of $C_t$ change as a percent of the $Z_s$ shock against quarter $t$. The x-axis is “Quarter $t$” with tick labels 0, 5, 10, 15, 20. The y-axis is “$C_t$ change (% of $Z_s$ shock)” with tick labels 0, 5, 10, 15, 20. Legend entries are $s=0$, $s=5$, $s=10$, and $s=15$. Each series spikes at the date of its income shock and shows smaller positive responses in other periods. Generated by `notebooks/lecture1_sim.ipynb`; figure `lecture1_fig7.pdf`.

## Slide 30: Response to -1 pp $r_s^p$ shocks at different dates $s$

Consumption increases in anticipation of falling returns, but less than standard Euler equation.

If $s=0$ then it’s a surprise negative return (“capital loss”). Implied MPC out of loss is only 0.011, very low but persistent.

**Image note:** Line chart of $C_t$ change as a percent of steady state against quarter $t$. The x-axis is “Quarter $t$” with tick labels 0, 5, 10, 15, 20. The y-axis is “$C_t$ change (% of steady state)” with tick labels $-0.4$, $-0.2$, 0.0, 0.2, 0.4. Legend entries are $s=0$, $s=5$, $s=10$, and $s=15$. Anticipated return shocks raise consumption before the shock date and lower it afterward; the $s=0$ surprise negative return gives a persistent negative consumption response. Generated by `notebooks/lecture1_sim.ipynb`; figure `lecture1_fig8.pdf`.

## Slide 31: Conclusion

## Slide 32: Conclusion

* Introduced standard incomplete markets model.
* Nice features: concave consumption functions, buffer-stock behavior, endogenous wealth distribution.
* Resolve steady-state “asset-MPC tradeoff” by introducing $\beta$ heterogeneity.
* Aggregate dynamics a function of the $\{r_s^p,Z_s\}$ path.
* Elevated consumption in period of income shock, some before and after too.
* Consumption response to $r$ smaller than rep agent; MPC out of cap gains still low.
