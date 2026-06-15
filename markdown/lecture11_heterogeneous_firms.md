## Slide 1: Heterogeneous firms

Adrien Auclert

Goethe Heterogeneous-Agent Macro Workshop, 2026


## Slide 2: Investment and firm heterogeneity

- **Workshop so far:** household heterogeneity in NK model
  - Changes transmission of monetary policy to consumption!
- **Parallel literature:** firm heterogeneity, though mostly in flexible-price models
  - **Q:** How does this change transmission of monetary policy to investment?
- Paper in preparation for Journal of Economic Literature, with Tom Winberry


## Slide 3: Plan

1. Canonical HANK model with **representative firm** investment
2. New transmission mechanisms for $I$ with added **firm heterogeneity**
3. Complementarities from combining heterogeneous households and firms


## Slide 4: Adding investment to canonical HANK model


## Slide 5: Adding investment with rep. firm

- No investment in canonical HANK model so far. Let’s change this!

- **Representative firm** produces $Y_t = K_{t-1}^{\alpha}N_t^{\nu}$, faces capital adjustment costs, solves

$$
\max_{K_t,N_t}\sum_{t\ge 0}\prod_{s\le t}\frac{1}{1+r_s}D_t
$$

$$
D_t \equiv Y_t - w_tN_t - I_t
-\frac{1}{2}\phi\left(\frac{I_t}{K_{t-1}}-\delta\right)^2K_{t-1}
+T_t^f
$$

- Flexible prices and perfect competition:

$$
w_t = MPN_t = \nu Y_t/N_t
$$

- Households take $N_t$ as given, receive labor income $w_tN_t$ and transfers $T_t^h$

- Government issues debt to fund all transfers,

$$
B_t = (1+r_{t-1})B_{t-1}+T_t^h+T_t^f
$$


## Slide 6: Implications of quadratic adjustment costs

- Q theory equations:

$$
\frac{I_t}{K_{t-1}}-\delta = \frac{1}{\phi}(Q_t-1)
$$

$$
p_t = Q_tK_t = \frac{p_{t+1}+D_{t+1}}{1+r_t}
$$

- Use mutual fund trick, assume $B=0$ in steady state: 100% s.s. stock allocation

- So connection to household block is

$$
1+r_0^p = \frac{p_0+d_0}{p_{ss}}
$$

- Asset market clearing: $A_t = p_t+B_t$.

- Goods market clearing:

$$
C_t+I_t=Y_t=K_{t-1}^{\alpha}N_t^{\nu}
$$


## Slide 7: Calibration of HANK model with investment

- Standard functional forms:

$$
u(C)=\frac{C^{1-\sigma}}{1-\sigma}
$$

  adj cost for firms:

$$
\frac{1}{2}\phi x^2
$$

- Set $\alpha,\nu,\delta,\psi$ exogenously (here $\alpha+\nu<1$), $\beta$ to hit $r=1\%$ quarterly

- Pick remaining 2 parameters to hit the **peak impulse response** to an identified monetary policy shock [in spirit of Christiano-Eichenbaum-Evans]
  - Elasticity of intertemporal substitution $1/\sigma$ controls consumption response
  - Degree of capital adjustment costs $\phi$ controls investment response

| $\alpha$ | $\nu$ | $\delta$ | $\psi$ | $\beta$ | $\sigma$ | $\phi$ |
|---:|---:|---:|---:|---:|---:|---:|
| 0.32 | 0.6 | 2.5% | 1 | 0.99 | 1.6 | 9 |


## Slide 8: Impulse response to monetary policy shock

$I$ accounts for $\sim 60\%$ of the $Y$ response, $C$ for $\sim 40\%$

source: Christiano, Eichenbaum, Evans 2005

Image note: The slide shows a model impulse-response chart titled “Impulse response to a monetary policy shock,” with x-axis “Quarters since shock” and y-axis “% from steady state.” Legend: Consumption, Investment, Output, Real rate. Investment jumps the most and then decays; output and consumption rise less; the real rate falls below steady state. Two inset VAR-style charts on the right are titled “investment” and “consumption” and show confidence bands around responses.


## Slide 9: Transmission mechanism to $I$

- Using $Q$ eqns, get decomposition of investment response similar to usual for $C$:

$$
\frac{I_t}{K_{t-1}}-\delta
=
\frac{1}{\phi}
\left(
\frac{1}{1+r_t}
\left[
MPK(w_{t+1},K_t)
+1-\delta
-\frac{\phi}{2}\left(\frac{I_{t+1}}{K_t}-\delta\right)^2
+\phi\left(\frac{I_{t+1}}{K_t}-\delta\right)\frac{K_{t+1}}{K_t}
\right]
-1
\right)
$$

$\to$ discounting channel $(r_t^*)$ + expected $MPK$ channel $(w_{t+1})$

Magnitudes governed by (inverse) adjustment cost $1/\phi$


## Slide 10: Impulse response to monetary shock

- Investment is exclusively driven by direct effects! (Here indirect effect $<0$)
- Similar to representative household consumption.

Image note: Three charts decompose a monetary shock response. “Aggregates” plots real rate $r_t$, real wage $w_t$, labor income $w_tN_t$, and output $Y_t$ against quarters since shock. “Consumption decomposition” plots consumption $C_t$, direct effects from $r_t$, and indirect effects from $w_tN_t$ and $D_t$. “Investment Decomposition” plots investment $I_t$, direct effect from $r_t$, and indirect effect from $E[MPK_{t+1}]$. The investment response is almost entirely the direct real-rate effect.


## Slide 11: Impulse response to household transfer shock

- Fiscal transfers to hh have large & persistent effects on $C$... but no effect on $I$
- Fiscal transfers to firms have no effect because inside = outside liquidity ($MPI=0$)
- **Next:** what does firm heterogeneity do?

Image note: Three charts decompose a household transfer shock. “Aggregates” plots transfer $T_t^h$ (% of $Y$), real wage $w_t$, output $Y_t$, and labor income $w_tN_t$. “Consumption decomposition” plots consumption $C_t$, direct effect from $T_t^h$, and indirect effects from $w_tN_t$ and $D_t$. “Investment Decomposition” plots investment $I_t$, direct effect from $T_t^h$, and indirect effect from $E[MPK_{t+1}]$. Investment stays essentially flat.


## Slide 12: Under hh. hood: policies, MPCs, and distribution

- Buffer-stock behavior generates stationary distribution over assets
- Concave consumption function: MPCs negatively correlated with cash-on-hand

Image note: Left chart, “Net savings policy,” plots savings $a'(e,a)-a$ against incoming assets $a$, with lines for low income $(e_L)$ and high income $(e_H)$, annotations $a^*(e_L)=0$ and $a^*(e_H)$, and a zero-savings dashed line. Right chart, “MPCs and distribution,” plots $MPC=\partial c(e,a)/\partial a$ against incoming assets $a$, with low-income and high-income MPC lines plus grey density bars.


## Slide 13: Adding heterogeneous firms


## Slide 14: Heterogeneous firm model

- To get higher $MPI$s, build on tradition of models with idiosyncratic productivity risk + entry-exit + financial frictions [Hopenhayn; Khan-Thomas; Ottonello-Winberry...]

- Firm in idiosyncratic productivity state $z$ with incoming capital $k$ and debt $b$ solves

$$
v_t(z,k,b)
=
\max_{n,k',b',d}
d+
\frac{1}{1+r_t}
\mathbb{E}_t
\left[
\theta v_{t+1}(z',k',b')
+
(1-\theta)v_{t+1}^{end}(z',k',b')
\right]
$$

$$
d
=
zk^{\alpha}n^{\nu}
-w_tn
-\left(k'-(1-\delta)k\right)
-\varphi\left(\frac{k'-k}{k}\right)k
-b
+\frac{b'}{1+r_t}
+T_t^f
$$

$$
d\ge 0,\ [\lambda]
\qquad
b'\le \chi k',\ [\mu]
$$

$$
v_t^{end}(z,k,b)
=
zk^{\alpha}n^{\nu}
-w_tn
+(1-\delta)k
-b
+T_t^f
$$

Additional notes shown on the slide:
- Exit prevents firms from growing out of constraints
- Cannot issue equity
- Multiplier $\lambda$ on equity issuance
- Can borrow in addition to retaining earnings subject to classic collateral constraint


## Slide 15: Calibration

- Additional parameters relative to representative firm model
  - Death probability $1-\theta=2\%$ $\leftarrow$ firm exit rate [Business Dynamics Statistics]
  - Firm productivity process $\leftarrow$ estimated log AR(1) [Syverson 2011]
  - $\chi=0.35$ $\leftarrow$ ability to recover assets in bankruptcy [Kermani-Ma 2023]
  - Initial conditions $(k_0,b_0=\chi k_0)$ $\leftarrow$ size of new entrants $\ll$ average firm
- Calibration generates average $MPI=0.50$; ideally could use this as a data moment
- Not readily available: corporate finance $MPI$ literature hasn’t yet given us reliable estimates for broad set of firms (contrast with household finance $MPC$ literature!)
  - [Some promising work using surveys or semi-structural estimation]


## Slide 16: Steady state capital policy

- Consider an unconstrained firm $(b\ll 0)$
- Diminishing returns + adjustment costs generate target $k^*(z)$

FOC for unconstrained (assuming no exit, $\theta=1$):

$$
\frac{k'-k}{k}
=
\frac{1}{\phi}
\left(
\frac{1}{1+r_t}
\mathbb{E}
\left[
MPK(z',k',w_{t+1})+\tilde{\varphi}(k',k'')
\right]
-1
\right)
$$

Like rep. firm, unconstrained affected by m.p. via discounting and expected $MPK$ effects.

Image note: Chart plots net investment $k'(z,k,b)-k$ against initial capital $k$. A downward-sloping unconstrained policy crosses zero at the target $k^*(z)$.


## Slide 17: Steady state capital policy

- Next consider a firm that pays $d=0$ and borrows maximally $b'=\chi k'$

For borrowing and dividend constrained firm:

$$
k'-(1-\delta)k
+
\varphi\left(\frac{k'-k}{k}\right)k
=
\pi_t(z,k)+T_t^f-b+\frac{\chi k'}{1+r_t}
$$

where $\pi_t$ is profits, so

$$
k'=\bar{k}(z,k,b;r_t,w_t,T_t^f)
$$

Constrained firms affected by a cash flow effect:

$$
\text{lower } w_t \text{ today}
\to
\text{higher } \pi_t
\to
\text{higher } I_t
$$

Image note: Chart overlays the unconstrained investment policy with a constrained policy. The constrained policy is higher over a range of initial capital and reflects borrowing/dividend constraints.


## Slide 18: Steady state capital policy

- Full policy pastes the two, with additional intermediate $\lambda>0,\ b'<\chi k'$ region

Multiplier dynamics (with $\theta=1$):

$$
\lambda_t(z,k,b)
=
(1+r_t)\mu_t(z,k,b)
+
\mathbb{E}\left[\lambda_{t+1}(z',k',b')\right]
$$

pay divs only if can avoid constraint forever

General investment FOC:

$$
\frac{k'-k}{k}
=
\frac{1}{\phi}\frac{1}{1+r_t}
\mathbb{E}
\left[
\frac{\lambda_{t+1}(z',k',b')}{\lambda_t(z,k,b)}
\left(
MPK(z',k',w_{t+1})+\tilde{\varphi}(k',k'')
\right)
\right]
$$

Variation in $\lambda$ acts like effective risk aversion.

Image note: Chart plots net investment $k'(z,k,b)-k$ against initial capital $k$, showing the unconstrained policy, the constraint policy, and the full policy that pastes regimes together around the target $k^*(z)$.


## Slide 19: Investment policy, MPIs and distribution

- Concave investment function: MPIs negatively correlated with dist. to constraint
- $MPI>1$ possible due to ability to lever up $1/(1-\chi)$ - contrary to household model

Image note: Left chart, “Net investment policy,” plots net investment $k'(z,k,b)-k$ against distance to constraint $\chi k-b$, with annotations “Actively constrained” near zero distance and “Unconstrained” at larger distance. Right chart, “MPIs and distribution,” plots $MPI=-\partial i(z,k,b)/\partial b$ against distance to constraint $\chi k-b$, with low-productivity and high-productivity lines plus grey density bars. MPIs are highest near the constraint.


## Slide 20: Impulse response to monetary shock

- New cash flow channel of monetary policy to investment:

$$
w_t\downarrow \to \pi_t\uparrow \to I_t\uparrow
$$

- Magnitude controlled by profit-weighted $\overline{MPI}$ (since $\pi_{it}\propto Y_t$). Here, $\overline{MPI}$ small.

Image note: Three charts decompose a monetary shock with heterogeneous firms. “Aggregates” plots real rate $r_t$, real wage $w_t$, output $Y_t$, and labor income $w_tN_t$. “Consumption decomposition” plots consumption $C_t$, direct effects from $r_t$, and indirect effect from $w_tN_t$ and $D_t$. “Investment Decomposition” plots investment $I_t$, direct effect from $r_t$, $E[MPK]$ effect, and cash flow effect. The cash flow effect is positive but small.


## Slide 21: Impulse response to firm transfer shock

- Inside $\ne$ outside liquidity: PV-0 transfers to firms boost output today!
- Large direct effect from firm transfer (large $MPI$), small multiplier (small $\overline{MPI}$)

Image note: Three charts decompose a firm transfer shock. “Aggregates” plots transfer $T_t^f$ (% of $Y$), real wage $w_t$, labor income $w_tN_t$, and output $Y_t$. “Consumption decomposition” plots consumption $C_t$ and effect from $w_tN_t$ and $D_t$. “Investment Decomposition” plots investment $I_t$, direct effect from $T_t^f$, $E[MPK]$ effect, and cash flow effect. The direct investment effect is large on impact and falls quickly.


## Slide 22: Analogies...

| Section | Heterogeneous households | Heterogeneous firms |
|---|---|---|
| Steady state | MPCs / iMPCs | MPIs / iMPIs |
| Steady state | Concave consumption function out of liquidity | Concave investment function out of free cash flow |
| Steady state | Prudence | Concern about hitting constraints |
| Steady state | Target (buffer) stock of assets | Target stock of capital (diminishing returns) |
| Steady state | Impatience | Life cycle (entry-exit) |
| Steady state | Income vs substitution effects | Income vs substitution effects |
| Response to shocks | Indirect effects of monetary policy | Cash flow effects of monetary policy |
| Response to shocks | Departure from Ricardian equivalence | Departure from inside = outside liquidity |
| Response to shocks | Income-weighted MPC governs multiplier | Profit-weighted MPI governs multiplier |


## Slide 23: How much do we get from the combination?


## Slide 24: Households vs firm transfers

Impact on GDP (net of adj. cost) of 1% of GDP transfer...

### To households

|  | Rep firm | Het firm |
|---|---:|---:|
| Rep household | 0 | 0 |
| Het household | 0.29 | 0.31 |

Formula under 0.29:

$$
\frac{MPC}{1-\overline{MPC}}
$$

Formula under 0.31:

$$
\frac{MPC}{1-(\overline{MPC}+\overline{MPI})}
$$

### To firms

|  | Rep firm | Het firm |
|---|---:|---:|
| Rep household | 0 | 0.52 |
| Het household | 0 | 0.64 |

Formula beside 0.52:

$$
\frac{MPI}{1-\overline{MPI}}
$$

Formula under 0.64:

$$
\frac{MPI}{1-(\overline{MPC}+\overline{MPI})}
$$

- Implications for stimulus policy ultimately depend on our views of $MPC$s vs $MPI$s!

Image note: Two side-by-side tables compare transfers to households versus transfers to firms. The entries 0.31 and 0.64 are circled, emphasizing the heterogeneous-household/heterogeneous-firm combination.


## Slide 25: Bringing firm heterogeneity to HANK

- Firms have been left out but have their rightful place in HANK!

- With non-zero $MPI$s as in the data:
  - ... cash flow transmission channel to $I$, paralleling indirect effect on $C$
  - ... PV-0 transfers to firms have large and persistent effects on $Y$
  - ... activates Keynesian feedback effects: $Y\to I\to Y\to C$ and $Y\to C\to Y\to I$

- More empirical work needed to measure MPIs & covariance with firm observables
