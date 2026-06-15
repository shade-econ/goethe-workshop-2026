## Slide 1: Intro to HANK models: Fiscal Policy

Ludwig Straub

Goethe Heterogeneous-Agent Workshop, 2026

## Slide 2: This session

- Just saw: How to solve steady states and simple transitional dynamics
- Next: Introducing “HANK” & how to use it for fiscal policy
  1. Canonical HANK model
  2. Fiscal policy in HANK
  3. Fiscal policy simulations

## Slide 3: The canonical HANK model

The canonical HANK model

## Slide 4: Introducing the canonical HANK model

- Embed standard het. agent model into standard NK model
- Will allow for a government: bonds, taxes, gov. spending
- Build on “Intertemporal Keynesian cross” (IKC) and Annual Review papers
- Set up the model in the sequence space
  - assume economy in steady state, feed in perfect foresight shock at $t = 0$
  - keep in mind certainty equivalence

## Slide 5: Household side

- Household $i \in [0,1]$ solves:

$$
\max_{\{c_{it}\}} \mathbb{E}_0 \sum_{t=0}^{\infty} \beta_{it}
\left(u(c_{it}) - v(N_t)\right)
$$

subject to

$$
c_{it} + a_{it}
\leq
(1+r_t^p)a_{it-1}
+
(1-\tau_t)\frac{W_t}{P_t}N_t e_{it},
\qquad
a_{it} \geq \underline{a}.
$$

Annotations on the household problem:

- Discount factor shocks as before to avoid “asset-MPC trade-off”
- Same hours worked for everyone (details coming up)
- [Can also capture progressive taxation as in Heathcote-Storesletten-Violante]

Total post-tax labor income:

$$
Z_t = (1-\tau_t)\frac{W_t}{P_t}N_t
$$

First example of a “block”:

$$
\{r_t^p, Z_t\}_{t=0}^{\infty}
\longrightarrow
\{C_t, A_t\}_{t=0}^{\infty}
$$

*Image note:* The slide uses arrows to label discount factor shocks, common hours worked, total post-tax labor income, and the household “block” mapping from prices/income to aggregate consumption and assets.

## Slide 6: Nominal rigidity

- Standard RANK model uses sticky prices with flexible wages:

Diagram text:

- Goods demand $\uparrow$
- Firms
- Firms can’t raise prices!
- Labor demand $\uparrow$
- Workers demand higher wages!
- Workers
- Markups fall!
- Real wages surge!
- Sticky prices effectively redistribute resources from firm owners to workers
- Not an issue in RANK. Could be huge issue in HANK!
- [Bilbiie 2008, Broer et al. 2020]

*Image note:* Flow diagram shows higher goods demand raising labor demand; with sticky prices and flexible wages, markups fall and real wages surge, redistributing resources from firm owners to workers.

## Slide 7: Sticky wages

- Our canonical HANK model uses sticky wages as in Erceg et al (2000)

Diagram text:

- Goods demand $\uparrow$
- Firms
- Firms don’t raise prices!
- Labor demand $\uparrow$
- Workers can’t raise wages!
- Workers
- Markups constant
- Real wages constant
- No redistribution here!

- How are wages adjusted?  
  Unions set wages on behalf of workers…

$$
\pi_t^w
=
\kappa
\left(
v'(N_t)
-
\frac{\epsilon-1}{\epsilon}
(1-\tau_t)
\frac{W_t}{P_t}
u'(C_t)
\right)
+
\beta \pi_{t+1}^w
$$

*Image note:* Flow diagram contrasts sticky wages with the previous slide: firms do not raise prices, workers cannot raise wages, markups and real wages stay constant, and there is no redistribution.

## Slide 8: Production

- Monopolistic competition, linear production in labor. In aggregate:

$$
Y_t = N_t
$$

- With flexible prices, price equals constant markup times marginal cost:

$$
P_t = \mu W_t
\iff
\frac{W_t}{P_t} = \mu^{-1}
$$

- Real wage exogenous. Goods inflation = wage inflation:

$$
\pi_t = \pi_t^w
$$

- For this lecture: no markups, $\mu = 1$. Will revisit later.

## Slide 9: Government: Fiscal policy

- Government sets fiscal policy, consisting of three paths:
  - $G_t$ government spending
  - $T_t = \tau_t Y_t$ total tax revenue, governed via tax rate $\tau_t$
  - $B_t$ government bonds (uniformly bounded to avoid Ponzi schemes)

- … subject to budget constraint:

$$
B_t = (1+r_t)B_{t-1} + G_t - T_t
$$

## Slide 10: Government: Monetary policy

- Monetary authority follows an interest rate rule. Allow for two kinds of rules:

- standard Taylor rule:

$$
i_t = r + \phi_\pi \pi_t + \epsilon_t
$$

(linearized)

Labels:

- $r$: steady state real rate
- $\phi_\pi$: Taylor rule coefficient

- real interest rate rule:

$$
i_t = r + \pi_{t+1} + \epsilon_t
\quad \Longrightarrow \quad
r_{t+1} = r + \epsilon_t
$$

Labels:

- Focus on this rule first
- Exogenous path of real rates!
- Will be hugely helpful for tractability…

- Two differences:  
  (i) $\pi_t$ vs. $\pi_{t+1}$ (not crucial);  
  (ii) $\phi_\pi = 1$ (key)

*Image note:* The real-rate rule result $r_{t+1}=r+\epsilon_t$ is circled and emphasized as the tractable rule to focus on first.

## Slide 11: Definition of equilibrium

- All agents optimize and markets clear

Aggregate consumption and assets:

$$
C_t = \int c_t^*(a_-,e)\,dD_t(a_-,e)
$$

$$
A_t = \int a_t^*(a_-,e)\,dD_t(a_-,e)
$$

Market clearing:

$$
G_t + C_t = Y_t
$$

$$
A_t = B_t
$$

Label:

- equivalent by Walras’ law
- Bonds are only asset here
- Later: add capitalized profits with $\mu > 1$

*Image note:* Diagram shows goods-market clearing $G_t+C_t=Y_t$ and asset-market clearing $A_t=B_t$ as equivalent by Walras’ law.

## Slide 12: Computing the steady state

- Simple to compute the steady state:

1. Normalize output $Y = 1$, pick $r, B, G$. Gov. budget:

$$
T = rB + G
$$

2. Can use same code as before:
   - use as income $Z e_{it}$ with

$$
Z = Y - T
$$

   - choose $\beta$ to match

$$
A = B
$$

3. $G + C = Y$ holds by Walras’ law! Done!

- Next: Solve for dynamic responses to fiscal policy shocks!

## Slide 13: Fiscal Policy

Fiscal Policy

## Slide 14: Fiscal policy shocks

- We just introduced the canonical HANK model.
- Next: Focus on fiscal policy!
  - Switch off monetary policy shocks:

$$
r_t = r = \text{const}
$$

  - Focus on first-order shocks to fiscal policy $dG=\{dG_t\}$, $dT=\{dT_t\}$ s.t.

$$
\sum_{t=0}^{\infty}(1+r)^{-t}(dG_t-dT_t)=0
$$

## Slide 15: Aggregate consumption function

- Recall household “block”: mapping sequences $\{r_t^p, Z_t\}$ into $\{C_t,A_t\}$

- With constant $r$, this means that date-$t$ consumption can be written as

$$
C_t = \mathcal{C}_t(Z_0,Z_1,Z_2,\ldots)
=
\mathcal{C}_t(\{Z_s\})
$$

- We call this the intertemporal consumption function.

- With $\mathcal{C}_t$ we can write goods market clearing as

$$
Y_t = G_t + \mathcal{C}_t(\{Y_s - T_s\})
$$

Annotation:

- This exactly describes the equilibrium output response $Y_t$!

## Slide 16: Intertemporal MPCs

$$
Y_t = G_t + \mathcal{C}_t(\{Y_s - T_s\})
$$

- Feed in small shock $\{dG_t,dT_t\}$

$$
dY_t
=
dG_t
+
\sum_{s=0}^{\infty}
\frac{\partial \mathcal{C}_t}{\partial Z_s}
\cdot
(dY_s-dT_s)
$$

- Response entirely characterized by Jacobian of $\mathcal{C}$, “intertemporal MPCs”

$$
M_{t,s}
\equiv
\frac{\partial \mathcal{C}_t}{\partial Z_s}
$$

- $M_{t,s}$ = % of date-$s$ income gain spent at date-$t$. Note:

$$
\sum_{t=0}^{\infty}(1+r)^{s-t}M_{t,s}=1
$$

## Slide 17: Intertemporal MPCs

Response to income increase at $s=0$

$$
\mathbf{M}
=
\begin{pmatrix}
M_{0,0} & M_{0,1} & M_{0,2} & M_{0,3} & \cdots \\
M_{1,0} & M_{1,1} & M_{1,2} & M_{1,3} & \cdots \\
M_{2,0} & M_{2,1} & M_{2,2} & M_{2,3} & \cdots \\
M_{3,0} & M_{3,1} & M_{3,2} & M_{3,3} & \cdots \\
\vdots  & \vdots  & \vdots  & \vdots  & \ddots
\end{pmatrix}
$$

*Image note:* Matrix diagram highlights the first column, corresponding to the consumption response over time to an income increase at $s=0$.

## Slide 18: Intertemporal MPCs

Response to income increase at $s=1$

$$
\mathbf{M}
=
\begin{pmatrix}
M_{0,0} & M_{0,1} & M_{0,2} & M_{0,3} & \cdots \\
M_{1,0} & M_{1,1} & M_{1,2} & M_{1,3} & \cdots \\
M_{2,0} & M_{2,1} & M_{2,2} & M_{2,3} & \cdots \\
M_{3,0} & M_{3,1} & M_{3,2} & M_{3,3} & \cdots \\
\vdots  & \vdots  & \vdots  & \vdots  & \ddots
\end{pmatrix}
$$

*Image note:* Matrix diagram highlights the second column, corresponding to the consumption response over time to an income increase at $s=1$.

## Slide 19: Intertemporal MPCs

Response to income increase at $s=2$

$$
\mathbf{M}
=
\begin{pmatrix}
M_{0,0} & M_{0,1} & M_{0,2} & M_{0,3} & \cdots \\
M_{1,0} & M_{1,1} & M_{1,2} & M_{1,3} & \cdots \\
M_{2,0} & M_{2,1} & M_{2,2} & M_{2,3} & \cdots \\
M_{3,0} & M_{3,1} & M_{3,2} & M_{3,3} & \cdots \\
\vdots  & \vdots  & \vdots  & \vdots  & \ddots
\end{pmatrix}
$$

Note: $\mathbf{M}$ preserves present values:

$$
\sum_{t=0}^{\infty}
\frac{1}{(1+r)^t}M_{t,s}
=
\frac{1}{(1+r)^s}
$$

Labels:

- PV of spending response
- PV of date-$s$ income increase

Equivalently:

$$
\mathbf{q}'\mathbf{M} = \mathbf{q}'
$$

where

$$
\mathbf{q}
=
\left(1,(1+r)^{-1},(1+r)^{-2},\ldots\right)'
$$

*Image note:* Matrix diagram highlights the third column, corresponding to the consumption response over time to an income increase at $s=2$.

## Slide 20: The intertemporal Keynesian cross

$$
dY_t
=
dG_t
+
\sum_{s=0}^{\infty}
\frac{\partial \mathcal{C}_t}{\partial Z_s}
\cdot
(dY_s-dT_s)
$$

$$
d\mathbf{Y}
=
d\mathbf{G}
-
\mathbf{M}d\mathbf{T}
+
\mathbf{M}d\mathbf{Y}
$$

Intertemporal Keynesian cross

- Entire complexity of model is in $\mathbf{M}$
- “Sufficient statistic” — only $\mathbf{M}$ matters!

*Image note:* The slide shows an arrow from the component equation to the boxed vector equation defining the intertemporal Keynesian cross.

## Slide 21: Comparison with old-Keynesian cross

- Very similar to the Old-Keynesian cross in IS-LM:

$$
dY_t
=
dG_t
-
\mathrm{mpc}\cdot dT_t
+
\mathrm{mpc}\cdot dY_t
$$

- Intertemporal Keynesian cross: microfounded, vector-valued, dynamic
- But: Many intuitions in HANK are similar to IS-LM intuitions
  - in some sense, HANK much more Keynesian than NK models!

## Slide 22: Solving the intertemporal Keynesian cross

$$
d\mathbf{Y}
=
d\mathbf{G}
-
\mathbf{M}d\mathbf{T}
+
\mathbf{M}d\mathbf{Y}
\quad \Rightarrow \quad
(\mathbf{I}-\mathbf{M})d\mathbf{Y}
=
d\mathbf{G}
-
\mathbf{M}d\mathbf{T}
$$

- Can’t we simply invert $\mathbf{I}-\mathbf{M}$?
- No! Because $\mathbf{M}$ preserves present value:

$$
\mathbf{q}'(\mathbf{I}-\mathbf{M})=0
$$

- With some advanced math, can show that inverse still exists iff unique bounded $d\mathbf{Y}$ exists:

$$
d\mathbf{Y}
=
\mathcal{M}(d\mathbf{G}-\mathbf{M}d\mathbf{T})
$$

where

$$
\mathcal{M}
\equiv
\left(\mathbf{K}(\mathbf{I}-\mathbf{M})\right)^{-1}\mathbf{K}
\quad \text{with} \quad
\mathbf{K}
=
-
\sum_{t=1}^{\infty}
(1+r)^{-t}\mathbf{F}^t
$$

## Slide 23: Solving using asset market clearing

- An equivalent way to solve the model:

$$
\mathcal{A}_t(\{Y_s-T_s\}) = B_t
$$

- Linearized:

$$
\mathbf{A}(d\mathbf{Y}-d\mathbf{T}) = d\mathbf{B}
\quad \Rightarrow \quad
d\mathbf{Y}
=
d\mathbf{T}
+
\mathbf{A}^{-1}d\mathbf{B}
$$

- Same solution (can show):

$$
d\mathbf{Y}
=
\mathcal{M}(d\mathbf{G}-\mathbf{M}d\mathbf{T})
=
\underbrace{\mathcal{M}(\mathbf{I}-\mathbf{M})d\mathbf{T}}_{=d\mathbf{T}}
+
\underbrace{\mathcal{M}}_{=\mathbf{A}^{-1}\mathbf{K}}
\underbrace{(d\mathbf{G}-d\mathbf{T})}_{\mathbf{K}(d\mathbf{G}-d\mathbf{T})=d\mathbf{B}}
$$

## Slide 24: The balanced budget multiplier

- In some cases, solution is simple!
- E.g. suppose $d\mathbf{G}=d\mathbf{T}$, i.e. gov. spending increase financed by tax hike.
- Result:

$$
d\mathbf{Y}=d\mathbf{G}
$$

- Why? Simple to verify:

$$
d\mathbf{Y}
=
d\mathbf{G}
-
\mathbf{M}d\mathbf{T}
+
\mathbf{M}d\mathbf{Y}
\quad \Rightarrow \quad
d\mathbf{G}
=
d\mathbf{G}
-
\mathbf{M}d\mathbf{G}
+
\mathbf{M}d\mathbf{G}
$$

or using asset market:

$$
d\mathbf{Y}
=
d\mathbf{T}
+
\mathbf{A}^{-1}d\mathbf{B}
=
d\mathbf{T}
=
d\mathbf{G}
$$

- IS-LM antecedents: Gelting (1941), Haavelmo (1945)

## Slide 25: Deficit financed fiscal policy

- With deficit-financing $d\mathbf{G}\neq d\mathbf{T}$ we have

$$
d\mathbf{Y}
=
d\mathbf{G}
+
\underbrace{
\mathcal{M}\cdot \mathbf{M}\cdot(d\mathbf{G}-d\mathbf{T})
}_{d\mathbf{C}}
$$

Interaction term: large if $\mathbf{M}$ is large and primary deficits $d\mathbf{G}-d\mathbf{T}$ large.

- Next: Compute $\mathbf{M}$ and simulate this!

## Slide 26: Fiscal policy simulations

Fiscal policy simulations

## Slide 27: Getting the intertemporal MPCs

- To solve the intertemporal Keynesian cross, all we need is $\mathbf{M}$
- Potentially costly!
- Quick to solve using “fake-news algorithm” (see later today)
- What does $\mathbf{M}$ look like in other models? (repr. agent? two-agent?)

*Image note:* Chart titled “Columns of M” plots intertemporal MPC $M_{t,s}$ against Quarter $t$ for $s=0$, $s=10$, $s=20$, and $s=30$. Annotation: “Peaks on dates when income is received.” Generated by `notebooks/lecture2_fiscal.ipynb`; figure `lecture2_impc.pdf`.

## Slide 28: RA and TA

- Repr. agent (RA):

$$
\beta = \frac{1}{1+r}
$$

$$
C_t
=
(1-\beta)
\sum_{s\geq 0}
\beta^s Z_s
+
r a_{-1}
\quad \Rightarrow \quad
M_{t,s}
=
\frac{\partial C_t}{\partial Z_s}
=
(1-\beta)\beta^s
$$

$$
\mathbf{M}^{RA}
=
\begin{pmatrix}
1-\beta & (1-\beta)\beta & (1-\beta)\beta^2 & \cdots \\
1-\beta & (1-\beta)\beta & (1-\beta)\beta^2 & \cdots \\
1-\beta & (1-\beta)\beta & (1-\beta)\beta^2 & \cdots \\
\vdots  & \vdots           & \vdots             & \ddots
\end{pmatrix}
$$

- Two-agent (TA): Like RA, except a fraction $\lambda$ of households is hand-to-mouth

$$
\mathbf{M}^{TA}
=
(1-\lambda)\mathbf{M}^{RA}
+
\lambda \mathbf{I}
$$

## Slide 29: RA and TA iMPCs

*Image note:* Two side-by-side charts compare intertemporal MPCs $M_{t,s}$ by Quarter $t$ for $s=0$, $s=10$, $s=20$, and $s=30$. Generated by `notebooks/lecture2_fiscal.ipynb`; figures `lecture2_impc_ra.pdf` and `lecture2_impc_ta_zoomedout.pdf`.

- Left chart: “Representative agent”
  - x-axis: Quarter $t$
  - y-axis: Intertemporal MPC $M_{t,s}$
  - y-axis range shown approximately from 0.0050 to 0.0057
  - lines are nearly flat

- Right chart: “Two agent”
  - x-axis: Quarter $t$
  - y-axis: Intertemporal MPC $M_{t,s}$
  - y-axis range shown from 0.000 to 0.200
  - sharp spikes occur at the dates corresponding to $s=0$, $s=10$, $s=20$, and $s=30$

## Slide 30: RA and TA iMPCs

*Image note:* Two side-by-side charts again compare intertemporal MPCs $M_{t,s}$ by Quarter $t$ for $s=0$, $s=10$, $s=20$, and $s=30$. Generated by `notebooks/lecture2_fiscal.ipynb`; figures `lecture2_impc_ra_zoomedout.pdf` and `lecture2_impc_ta_zoomedout.pdf`.

- Left chart: “Representative agent”
  - x-axis: Quarter $t$
  - y-axis: Intertemporal MPC $M_{t,s}$
  - y-axis range shown from 0.000 to 0.200
  - representative-agent lines are close to zero at this scale

- Right chart: “Two agent”
  - x-axis: Quarter $t$
  - y-axis: Intertemporal MPC $M_{t,s}$
  - y-axis range shown from 0.000 to 0.200
  - sharp spikes occur at the dates corresponding to $s=0$, $s=10$, $s=20$, and $s=30$

## Slide 31: Comparing the first columns

*Image note:* Chart titled “First columns of the iMPC matrix $M_{t,0}$” plots Intertemporal MPC $M_{t,0}$ against Quarter $t$. Legend: Heterogeneous agents, Two agents, Representative agent. The heterogeneous-agent line has a substantial delayed response after the initial spike; the two-agent response drops quickly; the representative-agent response is nearly flat and close to zero. Generated by `notebooks/lecture2_fiscal.ipynb`; figure `lecture2_impc_comparison.pdf`.

- Substantial delayed $C$ response in HA
- Supported by several recent studies:
  - Fagereng, Holm, Natvik (2021)
  - Colarieti, Mei, Stantcheva (2024)
  - Guerreiro, Eichenbaum (2026)
- Some find noisy zero (can’t reject delayed $C$ response)
  - Boehm, Fize, Jaravel (2025)

## Slide 32: Deficit financed tax cut

*Image note:* Two side-by-side charts show the shock paths. Generated by `notebooks/lecture2_fiscal.ipynb`; figures `lecture2_tax_cut_shock.pdf` and `lecture2_debt_shock.pdf`.

- Left chart: “Tax cut shock”
  - x-axis: Quarter $t$
  - y-axis: Tax cut shock $dT_t$
  - legend: Tax cut shock $dT_t$
  - path starts near $-1.0$ and rises toward zero, eventually slightly positive

- Right chart: “Debt shock”
  - x-axis: Quarter $t$
  - y-axis: Debt shock $dB_t$
  - legend: Debt shock $dB_t$
  - path rises from about $1$ to above $6$, then gradually declines

## Slide 33: Deficit financed tax cut in RA, TA, HA

*Image note:* Chart titled “Output response to tax cut shock” plots Output response $dY_t$ against Quarter $t$. Legend: Heterogeneous agents, Two agents, Representative agent. Generated by `notebooks/lecture2_fiscal.ipynb`; figure `lecture2_output_response.pdf`.

Annotations:

- HA: sustained boom!
- TA gets boom, but zero NPV
- RA is Ricardian!

## Slide 34: Summary

Summary

## Slide 35: Summary

- We introduced a canonical HANK model:
  - standard heterogeneous-agent household side
  - standard New-Keynesian supply side, but sticky wages + flexible prices
  - real rate rule for now, later Taylor rule

- Matters for fiscal policy!
  - deficit financing & front loading amplifies initial + cumulative multipliers
  - not the case in RA, and not even in TA
