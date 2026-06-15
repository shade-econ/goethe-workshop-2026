## Slide 1: Certainty Correspondence: Higher-Order Perturbation in the Sequence Space

Certainty Correspondence:  
Higher-Order Perturbation in the Sequence Space

Matthew Rognlie  
(based on work in progress with Adrien Auclert, Rodolfo Rigato, Ludwig Straub)

Goethe Heterogeneous-Agent Macro Workshop, 2026


## Slide 2: Aggregate risk in heterogeneous-agent models

- Heterogeneous-agent (HA) models with aggregate risk are difficult to solve
- **Common strategy:** solve with perfect foresight, appeal to **certainty equivalence**
  - 1st order perfect foresight $\Leftrightarrow$ 1st order perturbation solution  
    [e.g. Boppart-Krusell-Mitman, Auclert-Bardoczy-Rognlie-Straub,...]
- Critique: “not suitable for Qs in which aggregate risk and non-linearities play a key role”  
  [Moll, 2024]

- This paper: **certainty correspondence!**
  - Perfect foresight still enough to get **2nd, 3rd (+) order perturbation solution!**
  - Obtain same answer as “pruned” state-space perturbation, but much faster!

[state-space perturbation as in Bhandari-Bourany-Evans-Golosov, Bilal, Bayer-Luetticke, Reiter...; $\neq$ “global solution”]


## Slide 3: Certainty correspondence

| Order in agg. risk | Perfect foresight solution<br>Agents perceive no aggregate risk | Rational expectations solution<br>Agents have correct expectations of aggregate risk |
|---:|---|---|
| 0 | Deterministic steady state | Deterministic steady state |
| 1 | 1st order response | Linear $MA(\infty)$ |
| 2 | {2nd order responses} | Quadratic $MA(\infty)$ |
| 3 | {3rd order responses} | Cubic $MA(\infty)$ |
| $n$ | {nth order responses} | nth order Volterra expansion |

- Order 1 arrow label: **Certainty equivalence**
- Order 2 and higher arrow label: **Certainty correspondence**
- Between the $n$-order entries: etc...

Image note: Diagram/table with arrows connecting perfect-foresight responses to rational-expectations MA/Volterra expansions, highlighting certainty equivalence at first order and certainty correspondence at higher orders.


## Slide 4: Setup

Setup


## Slide 5: Setup (same as in lecture 8)

- Consider macro model:

$$
F\left(X_{t-1}, X_t, \mathbb{E}_t[X_{t+1}], \epsilon_t\right)=0
$$

Contrast with usual formulation:

$$
\mathbb{E}_t\left[F\left(X_{t-1},X_t,X_{t+1},\epsilon_t\right)\right]=0
$$

- $X_t \in \mathbb{R}^n$ are endogenous variables  
  [het-agent applications: $n$ large, eg $n=2{,}000$]
- $\epsilon_t \in \mathbb{R}$ are exogenous innovations (realized shock process)  
  [paper extends to $>1$ shock]
  - Distributed $\epsilon_t=\sigma_R\cdot \bar{\epsilon}_t$ with $\bar{\epsilon}_t$ iid, mean 0, variance 1, and symmetric density
- Expectations $\mathbb{E}_t[\cdot]$ are taken assuming future distribution of $\epsilon_t$ is $\sigma \cdot \bar{\epsilon}_t$
  - **Rational expectations:** $\sigma=\sigma_R$ (perceived distribution of future $\epsilon_t$ = truth)
  - **Perfect foresight:** $\sigma=0$ (agents think all future $\epsilon_t$ will realize to 0 for sure)
- **Deterministic steady state** $X\in \mathbb{R}^n$ solves $F(X,X,X,0)=0$ (i.e. $\sigma=\sigma_R=0$)


## Slide 6: (Stochastic) sequence space solution

- Given $\sigma$, consider **nonlinear sequence-space solution** to $F$:

$$
X_t=\mathcal{X}\left(\sigma;\epsilon_t,\epsilon_{t-1},\epsilon_{t-2},\ldots\right)
$$

[Lan-Meyer-Gohde, Lombardo-Uhlig]

[eg, obtained from stable state-space solution $X_t=g(X_{t-1},\epsilon_t;\sigma)$]

- Our paper relates this to the perfect-foresight solution

$$
X_t^{PF}=\mathcal{X}\left(0;\epsilon_t,\epsilon_{t-1},\epsilon_{t-2},\ldots\right)
$$

[eg, obtained from $\infty$-long sequence of repeated-surprise “MIT” shocks]

- Use **perturbation approach:** linearize $\mathcal{X}$ around $\sigma=\sigma_R=0$ (i.e. $\epsilon=0$)
- Helpful result:

$$
\mathcal{X}\left(\sigma;\epsilon_t,\epsilon_{t-1},\ldots\right)
=
\mathcal{X}\left(-\sigma;\epsilon_t,\epsilon_{t-1},\ldots\right)
$$

so, e.g.,

$$
\mathcal{X}_{\sigma}(0)=0
$$


## Slide 7: MIT shock impulse responses

- Special case of $X^{PF}$ is the MIT shock impulse response

$$
X_j^{MIT}(\nu)\equiv \mathcal{X}(0;0,\ldots,0,\nu,0,\ldots)
$$

where $\nu$ is at position $j$.

- Can compute $\{X_j^{MIT}(\nu)\}_j$ with nonlinear perfect foresight starting from $X$
- Similarly, for $\ell\ge 1$ we have the sequence of two MIT impulse responses

$$
X_j^{MIT,\ell}(\nu,\epsilon)\equiv
\mathcal{X}(0;0,\ldots,0,\nu,0,\ldots,0,\epsilon,0,\ldots)
$$

where $\nu$ is at position $j$ and $\epsilon$ is at position $j+\ell$.

- For each $\ell$, can compute $\{X_j^{MIT,\ell}(\nu,\epsilon)\}_j$ starting from $X_\ell^{MIT}(\epsilon)$
- **Next:** why these are sufficient to get the second-order solution!


## Slide 8: Warm-up: certainty equivalence

- Expand $X_t=\mathcal{X}(\sigma,\epsilon_t,\epsilon_{t-1},\ldots)$ to first order in $(\sigma,\epsilon)$:

$$
X_t
=
X
+
\mathcal{X}_{\sigma}(0)\sigma
+
\frac{\partial \mathcal{X}}{\partial \epsilon_0}(0)\epsilon_t
+
\frac{\partial \mathcal{X}}{\partial \epsilon_{-1}}(0)\epsilon_{t-1}
+
\cdots
+
\mathcal{O}(\sigma^2)
$$

Annotation: the $\mathcal{X}_{\sigma}(0)\sigma$ term is crossed out.  
Symmetry: steady state unchanged.  
No anticipated risk, no past realization.

- So, to first order, $X_t$ follows linear MA process, with coefficients equal to

$$
\frac{\partial \mathcal{X}}{\partial \epsilon_{-j}}(0)
=
\frac{dX_j^{MIT}}{d\nu}(0)
\equiv
\mathcal{X}_j
$$

**Certainty equivalence.** To first order, $X_t$ follows a linear MA process whose coefficients are given by the first order MIT shock impulse response of $X$ to $\epsilon$ [Boppart-Krusell-Mitman]


## Slide 9: Second-Order Certainty Correspondence

Second-Order Certainty Correspondence


## Slide 10: Second-order sequence space perturbation

- Now expand to second order in $(\sigma,\epsilon)$ around $(0,0)$ (“Volterra expansion”)
- Use symmetry result again:

$$
\frac{\partial^2 \mathcal{X}}{\partial \sigma \partial \epsilon_{-j}}(0)=0
$$

- Find:

$$
X_t
=
X
+
\sum_{j=0}^{\infty}\mathcal{X}_j\epsilon_{t-j}
+
\frac{1}{2}
\left(
\mathcal{X}_{\sigma\sigma}(0)\sigma^2
+
\sum_{j,k\ge 0}
\frac{\partial^2 \mathcal{X}}
{\partial \epsilon_{-j}\partial \epsilon_{-k}}(0)
\epsilon_{t-j}\epsilon_{t-k}
\right)
+
\mathcal{O}(\sigma^3)
$$

Annotations:
- Still no anticipated risk or past realization
- quadratic MA process

- Rearrange and interpret...


## Slide 11: Interpreting the quadratic MA process

$$
X_t
\simeq
X
+
\sum_{j=0}^{\infty}\mathcal{X}_j\epsilon_{t-j}
+
\frac{1}{2}\mathcal{X}_{\sigma\sigma}\sigma^2
+
\frac{1}{2}
\sum_{j=0}^{\infty}
\frac{\partial^2\mathcal{X}}{\partial \epsilon_{-j}^2}
\epsilon_{t-j}^2
+
\sum_{j=0}^{\infty}\sum_{\ell=1}^{\infty}
\frac{\partial^2\mathcal{X}}
{\partial\epsilon_{-j}\partial\epsilon_{-(j+\ell)}}
\epsilon_{t-j}\epsilon_{t-(j+\ell)}
$$

Labels on the formula:
- Anticipated risk
- Size dependence
- State dependence

- Size and state dependence are second-order MIT shock impulses

$$
\frac{\partial^2\mathcal{X}}{\partial \epsilon_{-j}^2}
=
\frac{d^2X_j^{MIT}}{d\nu^2}(0)
\equiv
\mathcal{X}_{jj}
$$

$$
\frac{\partial^2\mathcal{X}}
{\partial\epsilon_{-j}\partial\epsilon_{-(j+\ell)}}
=
\frac{\partial^2X_j^{MIT,\ell}}{\partial\epsilon\partial\nu}(0,0)
\equiv
\mathcal{X}_{j,j+\ell}
$$

- **Next:** How to solve for $\mathcal{X}_{\sigma\sigma}$ using only perfect foresight as well!


## Slide 12: Anticipated risk term

- How do we compute **anticipated risk term** $\frac{1}{2}\mathcal{X}_{\sigma\sigma}\sigma^2$?
- Idea: solve for the **risky steady state** with $\sigma_R=0$ but $\sigma>0$
- If all shocks have realized to $\epsilon_{t-j}=0$ in the past then we have:

$$
X_t=X_{t-1}\simeq X+\frac{1}{2}\mathcal{X}_{\sigma\sigma}\sigma^2
$$

Risky steady state (unknown)

$$
\mathbb{E}_t X_{t+1}
\simeq
X
+
\frac{1}{2}\mathcal{X}_{\sigma\sigma}\sigma^2
+
\frac{1}{2}\mathcal{X}_{00}\sigma^2
$$

Anticipation of impact size dependence (known)

- Find this $X^*$ by using steady state code to solve

$$
F\left(X^*,X^*,X^*+\frac{1}{2}\mathcal{X}_{00}\sigma^2,0\right)=0
$$

i.e. add impact size dependence $\mathcal{X}_{00}\sigma^2/2$ to $v$ in equations where $\mathbb{E}_t[v_{t+1}]$ appears


## Slide 13: Bottom line: solving the quadratic MA process

$$
X_t
\simeq
X
+
\sum_{j=0}^{\infty}\mathcal{X}_j\epsilon_{t-j}
+
\frac{1}{2}\mathcal{X}_{\sigma\sigma}\sigma^2
+
\frac{1}{2}\sum_{j=0}^{\infty}\mathcal{X}_{jj}\epsilon_{t-j}^2
+
\sum_{j=0}^{\infty}\sum_{\ell=1}^{\infty}
\mathcal{X}_{j,j+\ell}\epsilon_{t-j}\epsilon_{t-(j+\ell)}
$$

Labels on the formula:
- Anticipated risk: Compute by modifying steady state equations
- Size dependence: Compute with second-order MIT shock
- State dependence: Compute this with two successive MIT shocks, $\times L$

- **Next:** Implications for model impulse responses and moments

Image note: The slide boxes the three second-order components of the quadratic MA process: anticipated risk, size dependence, and state dependence.


## Slide 14: Generalized impulse response

- Define generalized IRF of $X$ as

$$
IRF_j\left(\nu,\{\epsilon_{-k}\}_{k=1}^{\infty}\right)
\equiv
\mathbb{E}\left[X_j\mid \epsilon_0=\nu,\{\epsilon_{-k}\}_{k=1}^{\infty}\right]
-
\mathbb{E}\left[X_j\mid \{\epsilon_{-k}\}_{k=1}^{\infty}\right],
\qquad
j\ge 0
$$

- We have:

$$
IRF_j\left(\epsilon_0=\nu,\{\epsilon_{-k}\}_{k=1}^{\infty}\right)
=
x_j\nu
+
\frac{1}{2}\mathcal{X}_{jj}(\nu^2-\sigma^2)
+
\sum_{\ell=1}^{\infty}\mathcal{X}_{j,j+\ell}\nu\epsilon_{-\ell}
$$

Labels on the formula:
- First-order IRF: Linear, not state dependent
- Size dependence: Subtracts expected size dependence
- State dependence: Interaction of date-0 shock with shock $\ell$ periods ago

Image note: Bottom formula is visually divided into colored boxes for first-order IRF, size dependence, and state dependence.


## Slide 15: Model moments

- Ergodic (long-run) mean under rational expectations ($\sigma_R=\sigma$)

$$
\mathbb{E}[X]
=
X
+
\frac{1}{2}\mathcal{X}_{\sigma\sigma}\sigma^2
+
\frac{1}{2}\sum_{j=0}^{\infty}\mathcal{X}_{jj}\sigma^2
$$

Labels:
- Risky steady state
- Expected size dependence

- Ergodic variance from 2nd-order $MA$:

$$
\mathrm{Var}(X)
=
\sigma^2\sum_{j=0}^{\infty}(\mathcal{X}_j)^2
+
\frac{\sigma^4}{2}
\sum_{j,k=0}^{\infty}(\mathcal{X}_{jk})^2
$$

Labels:
- Implied by 1st-order MA (3rd order accurate)
- Same as in pruned 2nd-order state-space

- In paper: 4th-order accurate

$$
\mathrm{Var}\left(\mathcal{X}(\sigma;\sigma\bar{\epsilon}_t,\sigma\bar{\epsilon}_{t-1},\ldots)\right)
$$

adds terms from 3rd-o. $MA$


## Slide 16: Application: size dependence in consumption

- Nonlinear iMPCs! Large shock $\to$ lower MPC today ... but higher tomorrow!

Image note: Two line charts compare First order, Second order, and Nonlinear perfect foresight.
- Left chart: **Consumption at $t=0$**.  
  - x-axis: Shock size (% income)
  - y-axis: Consumption (% d.s.s.)
  - annotation: “Consumption function concave at $t=0$ ...”
- Right chart: **Consumption at $t=1$**.  
  - x-axis: Shock size (% income)
  - y-axis: Consumption (% d.s.s.)
  - annotation: “... but convex at $t=1$!”
- Legend: First order; Second order; Nonlinear perfect foresight.


## Slide 17: Application: history dependence in consumption

- High income shock in past implies more assets today, lower MPCs

Image note: Two line charts compare consumption responses by shock size.
- Left chart: **Consumption at $t=0$**.  
  - x-axis: Shock size (% income)
  - y-axis: Consumption (% d.s.s.)
- Right chart: **Consumption at $t=1$**.  
  - x-axis: Shock size (% income)
  - y-axis: Consumption (% d.s.s.)
- Legend: First order; Second order; Second order, $\epsilon_{-1}=0.1$.


## Slide 18: Application: aggregate precautionary savings

- Perceived aggregate income risk raises risky steady-state savings, lowers MPCs

Image note: Two charts show aggregate precautionary savings.
- Left chart: savings rise convexly with risk.  
  - x-axis: $\sigma$ (%)
  - y-axis: Savings (% d.s.s. income)
- Right chart: cumulative asset distributions.  
  - x-axis: Assets
  - y-axis: Cumulative distribution
  - legend: Deterministic steady state; Risky steady state.


## Slide 19: Third-Order Certainty Correspondence

Third-Order Certainty Correspondence


## Slide 20: Third-order sequence space perturbation

- Continue expanding to 3rd order, with symmetry implying

$$
\mathcal{X}_{\sigma jk}=0
$$

- Obtain **cubic** MA process:

$$
X_t
\approx
X_t^{(2)}
+
\frac{1}{6}
\sum_{j=0}^{\infty}
\frac{\partial^3\mathcal{X}}{\partial\epsilon_{-j}\partial\sigma^2}
\epsilon_{t-j}\sigma^2
+
\frac{1}{6}
\sum_{j=0}^{\infty}\sum_{k=0}^{\infty}\sum_{\ell=0}^{\infty}
\frac{\partial^3\mathcal{X}}
{\partial\epsilon_{-j}\partial\epsilon_{-k}\partial\epsilon_{-\ell}}
\epsilon_{t-j}\epsilon_{t-k}\epsilon_{t-\ell}
$$

- All **triple interactions** can be obtained from 1, 2, or 3 consecutive MIT shocks
- **New term** includes 2 effects:
  - How concerns about future risk affects first-order impulse response
  - How past shocks affect strength of precautionary motive

Image note: The cubic MA formula visually boxes the $\epsilon_{t-j}\sigma^2$ term and the triple-interaction term.


## Slide 21: New term in $\epsilon_{t-j}\sigma^2$

- Split the new term into these two effects

$$
\frac{\partial^3\mathcal{X}}{\partial\epsilon_{-j}\partial\sigma^2}
=
\left(
\frac{\partial^3\mathcal{X}}{\partial\epsilon_{-j}\partial\sigma^2}
\right)^{rss}
+
\left(
\frac{\partial^3\mathcal{X}}{\partial\epsilon_{-j}\partial\sigma^2}
\right)^{tvps}
$$

Labels:
- Effect of risky steady state on impulse response
- Effect of shock at date $-j$ on precautionary motive at date 0

- Get **1st** using impulse routines starting from the RSS distribution and expectations
- Get **2nd** by constructing a deterministic sequence $X_t$ of perturbed expectations:

$$
F\left(
X_{t-1},
X_t,
X_{t+1}
+
\frac{1}{6}
\frac{\partial^3\mathcal{X}}{\partial\epsilon_{-t}\partial\epsilon_0^2}
\sigma^2,
0
\right)
=0
$$


## Slide 22: Application: third order iMPCs

- Generalized impulse response of $C_t$ to innovation in income:

Image note: Stacked bar chart with a black “Total” line over years 0 through 5.
- x-axis: Years
- Legend:
  - Total
  - First order
  - Second order
  - Third order: size and hist.
  - Third order: risky s.s.
  - Third order: precautionary
- The chart decomposes the generalized impulse response into first-order, second-order, and several third-order components.


## Slide 23: Summary: certainty correspondence

- **Certainty correspondence:** can obtain 2nd and 3rd(+) order perturbation solutions to rational expectation solutions with perfect foresight methods!
  - ... despite agents being forward looking and anticipating future aggregate risk!

- Opens up lots of possibilities for research
  - state-dependent or size-dependent policies (e.g. fiscal or monetary)
  - welfare cost of business cycles
  - steady-state and time variation in precautionary savings or risk premia...


## Slide 24: Brief application to GE HANK model

Brief application to GE HANK model


## Slide 25: Speeding up the GE solution using Jacobians

- Asset market clearing error:

$$
H_t(\{Y_s\},\{B_s\})
\equiv
A_t(\{Y_s-T_s(B_s)\})-B_t
$$

- Given $\{B_s\}$, output solves

$$
\mathbf{H}(Y,B)=0
$$

- First-order solution:

$$
dY=-\mathbf{H}_Y^{-1}\mathbf{H}_B\,dB
$$

[ABRS 2021]

- Size-dependent impulse response, avoiding solving nonlinearly for $Y_t(\{B_s\})$!

$$
d^2Y
=
-\mathbf{H}_Y^{-1}
\left(
\lim_{\nu\to 0}
\frac{\mathbf{H}(Y+\nu dY,B+\nu dB)}{\nu^2}
\right)
$$

Annotations:
- same as for $dY$
- nonlinear error from $dY$
- Use similar approach for state dependence (just using different initial distribution)


## Slide 26: Generalized impulse response: size dependence

- Concavity / convexity of responses translate to GE!

Image note: Two charts show output responses to transfers.
- Left chart: **Output response at $t=0$**
  - x-axis: Transfers (% s.s. output)
  - y-axis: Output (% d.s.s.)
  - legend: First order; Second order
  - annotation: “Output multiplier smaller for larger shock at $t=0$ ...”
- Right chart: **Output response at $t=1$**
  - x-axis: Transfers (% s.s. output)
  - y-axis: Output (% d.s.s.)
  - annotation: “... but multiplier larger at $t=1$!”


## Slide 27: Generalized impulse response: state dependence

- Same with history: past transfers imply more excess savings today, lower MPCs

Image note: Two charts show state-dependent output responses to transfers.
- Left chart: **Output response at $t=0$**
  - x-axis: Transfers (% s.s. output)
  - y-axis: Output (% d.s.s.)
  - legend: First order; Second order; Second order, following shock at $t=-1$
- Right chart: **Output response at $t=0$**
  - x-axis: Transfers (% s.s. output)
  - y-axis: Output (% d.s.s.)


## Slide 28: Conclusion

Conclusion

MIT shocks (on a smooth model) are all you need!
