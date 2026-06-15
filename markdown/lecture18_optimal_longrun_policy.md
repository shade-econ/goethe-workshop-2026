## Slide 1: Ramsey taxation in the sequence space

Ramsey taxation in the sequence space

Ludwig Straub

Goethe Heterogeneous Agents Workshop, 2026


## Slide 2: Optimal Policy with heterogeneous agents?

- So far, focused on HANK, discussed lots of **positive** questions
  - e.g. effects of fiscal policy on output, monetary policy, …
- Very little work on **normative** implications (hard!)
  - optimal capital & labor taxation? optimal level of public debt?
- **Next:** A first step …
  - Optimal long-run fiscal policy
  - … in a canonical HA model without NK


## Slide 3: Ramsey steady state

- We focus on characterizing the **Ramsey steady state (RSS)**
  - long-run steady state of the full-commitment Ramsey plan
- A long literature characterizes the RSS in simpler models (RA, TA)
  - e.g. Chamley (1986), Judd (1985), Straub Werning (2020)
- We study the RSS in neoclassical HA models, à la Aiyagari
- Compare with “optimal steady state” (OSS)


## Slide 4: Next: New “sequence-space” approach

1. Heterogeneous-agent household side, introduce **discounted elasticities**
2. Set up Ramsey problem and derive FOCs
3. Numerically evaluate FOCs, get Ramsey steady state for many specifications

Note: Generalizes to other stationary household sides (bonds in utility, OLG,…)


## Slide 5: 1. Heterogeneous-agent household side

1. Heterogeneous-agent household side


## Slide 6: Households

Just like before, except hours are optimally chosen by households:

$$
\max_{\{c_{it},n_{it},a_{it}\}} \mathbb{E}_0 \sum_{t=0}^{\infty} \beta^t u(c_{it},n_{it})
$$

$$
c_{it}+a_{it}=(1+r_t)a_{it-1}+(1-\tau_t)e_{it}n_{it}, \qquad a_{it}\ge 0
$$

Inputs: interest rate and labor tax

Given $\{r_t\}, \{\tau_t\}$, can again aggregate household behavior using **sequence-space functions**:

Assets:

$$
\mathcal{A}_t(\{r_s,\tau_s\})=\int a_t\,dD_t
$$

Effective labor:

$$
\mathcal{N}_t(\{r_s,\tau_s\})=\int e n_t\,dD_t
$$

Utility:

$$
\mathcal{U}_t(\{r_s,\tau_s\})=\int u(c_t,n_t)\,dD_t
$$

**Image note:** The slide visually highlights $r_t$ and $\tau_t$ in the household budget constraint as the inputs, and groups the three sequence-space functions in a boxed panel.


## Slide 7: Infinitely anticipated shocks

- Consider **anticipated one-time shock** at some far-out future date $s$

Chart label: Response of assets to $r$

$$
\frac{\partial \log \mathcal{A}_{s+h}}{\partial r_s}
$$

Chart label: Response of labor supply to $\tau$

$$
\frac{\partial \log \mathcal{N}_{s+h}}{\partial \tau_s/(1-\tau)}
$$

**Image note:** Two impulse-response charts are shown. The asset response to an anticipated interest-rate increase peaks sharply at $h=0$. The labor-supply response to an anticipated tax increase has a sharp negative spike at $h=0$ with small positive responses around it.


## Slide 8: $\delta$-discounted elasticities

- Define “discounted” version of these derivatives (around steady state with $r,\tau$)

$$
\epsilon^{A,r}(r,\tau)
\equiv
\lim_{s\to\infty}
\sum_{h=-\infty}^{\infty}
\delta^h
\frac{\partial \log \mathcal{A}_{s+h}}{\partial r_s}
$$

$$
\epsilon^{N,\tau}(r,\tau)
\equiv
\lim_{s\to\infty}
\sum_{h=-\infty}^{\infty}
\delta^h
\frac{\partial \log \mathcal{N}_{s+h}}{\partial \tau_s/(1-\tau_s)}
$$

- These elasticities are discounted with some $\delta$ (later social discount factor)
- Well-defined for $\delta \in [\beta,1]$ precisely because the model is stationary!
- Define all the other elasticities similarly, e.g. $\epsilon^{N,r}$, $\epsilon^{A,\tau}$, $\epsilon^{U,r}$ etc.


## Slide 9: $\beta$-discounted elasticities

$$
\epsilon^{A,r}
\equiv
\lim_{s\to\infty}
\sum_{h=-\infty}^{\infty}
\beta^h
\frac{\partial \log \mathcal{A}_{s+h}}{\partial r_s}
\approx 25
$$

$$
\epsilon^{N,\tau}
\equiv
\lim_{s\to\infty}
\sum_{h=-\infty}^{\infty}
\beta^h
\frac{\partial \log \mathcal{N}_{s+h}}{\partial \tau_s/(1-\tau)}
\approx 0.15
$$

**Image note:** Two charts repeat the asset and labor-supply impulse responses, now with green dashed “$\beta$-weighted” curves and shaded weighted areas. The left chart illustrates a large discounted asset elasticity; the right chart illustrates a much smaller discounted labor-supply elasticity.


## Slide 10: 2. Ramsey problem

2. Ramsey problem


## Slide 11: Model description

- We’ve seen how we can summarize household behavior using “sequence space” functions $\mathcal{A}_t$, $\mathcal{N}_t$, $\mathcal{U}_t$

- **Next:**
  - set up the rest of the model: supply side, government policies
  - derive an implementability condition
  - set up the Ramsey problem!


## Slide 12: Production and government policy

- Representative firm: $Y_t=\mathcal{N}_t$, pre-tax wage $=1$

- Government: spends fixed $G>0$ (can relax)
  - controls labor taxes $\{\tau_s\}$, budget constraint:

$$
G+(1+r_t)B_{t-1}=B_t+\tau_t N_t
$$

Implementability condition: $\{r_s\}, \{\tau_s\}$ part of an equilibrium iff

$$
G+(1+r_t)\mathcal{A}_{t-1}(\{r_s,\tau_s\})
=
\mathcal{A}_t(\{r_s,\tau_s\})
+
\tau_t \mathcal{N}_t(\{r_s,\tau_s\})
$$

**Image note:** The implementability condition is emphasized in a large boxed panel.


## Slide 13: Ramsey problem

Full-commitment Ramsey problem, with arbitrary social discount factor $\delta$

$$
\max_{\{r_s,\tau_s\}_{s=0}^{\infty}}
\sum_{t=0}^{\infty}
\delta^t
\mathcal{U}_t(\{r_s,\tau_s\})
$$

subject to

$$
G+(1+r_t)\mathcal{A}_{t-1}(\{r_s,\tau_s\})
=
\mathcal{A}_t(\{r_s,\tau_s\})
+
\tau_t \mathcal{N}_t(\{r_s,\tau_s\})
$$

- If solution converges to well-defined steady state $(r_s \to r < 1/\beta - 1,\ \tau_s \to \tau < 1)$ we call this steady state a **Ramsey steady state (RSS)**.
- Multiplier on the constraint $\lambda_t$ may or may not converge!
  - For today, assume it does, $\lambda_t \to \lambda$. Relax this in the paper.


## Slide 14: Characterizing the Ramsey steady state

Ramsey problem shown at top:

$$
\max_{\{r_s,\tau_s\}_{s=0}^{\infty}}
\sum_{t=0}^{\infty}
\delta^t
\mathcal{U}_t(\{r_s,\tau_s\})
$$

$$
G+(1+r_t)\mathcal{A}_{t-1}(\{r_s,\tau_s\})
=
\mathcal{A}_t(\{r_s,\tau_s\})
+
\tau_t \mathcal{N}_t(\{r_s,\tau_s\})
$$

- Begin with the FOCs with respect to $r_s$:

$$
\sum_{h=-s}^{\infty}
\delta^h
\frac{\partial \mathcal{U}_{s+h}}{\partial r_s}
+
\sum_{h=-s}^{\infty}
\delta^h \lambda_{s+h}
\left(
\frac{\partial \mathcal{A}_{s+h}}{\partial r_s}
+
\tau_{s+h}
\frac{\partial \mathcal{N}_{s+h}}{\partial r_s}
-
(1+r_{s+h})
\frac{\partial \mathcal{A}_{s+h-1}}{\partial r_s}
\right)
-
\lambda_s \mathcal{A}_{s-1}
=0
$$

Term labels shown on the slide:

- $\epsilon^{U,r}$, as $s \to \infty$
- $A\lambda \cdot \epsilon^{A,r}$
- $\tau N\lambda \cdot \epsilon^{N,r}$
- $A\lambda(1+r)\delta \cdot \epsilon^{A,r}$
- $\lambda A$

**Image note:** Colored arrows and boxes map pieces of the FOC to their limiting discounted-elasticity terms.


## Slide 15: Characterizing the Ramsey steady state

Ramsey problem shown at top:

$$
\max_{\{r_s,\tau_s\}_{s=0}^{\infty}}
\sum_{t=0}^{\infty}
\delta^t
\mathcal{U}_t(\{r_s,\tau_s\})
$$

$$
G+(1+r_t)\mathcal{A}_{t-1}(\{r_s,\tau_s\})
=
\mathcal{A}_t(\{r_s,\tau_s\})
+
\tau_t \mathcal{N}_t(\{r_s,\tau_s\})
$$

- From the $r_s$ derivative around the (unknown) RSS:

$$
\lambda^{-1}\epsilon^{U,r}
=
A
-
\left(1-\delta(1+r)\right)A\epsilon^{A,r}
-
\tau N\epsilon^{N,r}
$$

- Same procedure applied to the $\tau_s$ derivative:

$$
\lambda^{-1}\epsilon^{U,\tau}
=
(1-\tau)N
-
\left(1-\delta(1+r)\right)A\epsilon^{A,\tau}
-
\tau N\epsilon^{N,\tau}
$$

Two helpful objects:

$$
\ell \equiv \frac{A}{(1-\tau)N}
\quad \text{as liquidity;}
\qquad
m \equiv -\frac{\epsilon^{U,\tau}}{\epsilon^{U,r}}>0
\quad \text{as effective MRS.}
$$


## Slide 16: RSS optimality condition

- If allocation converges to a well-defined RSS with interest rate $r$ and tax rate $\tau$, and if $\lambda_t$ converges, then $(r,\tau)$ are characterized by:

1. The steady-state government budget constraint

$$
G+r\mathcal{A}(r,\tau)=\tau\mathcal{N}(r,\tau)
$$

2. Optimality condition

$$
\left(1-(1+r)\delta\right)\ell
\left(m\epsilon^{A,r}+\epsilon^{A,\tau}\right)
-
\frac{\tau}{1-\tau}
\left(-\epsilon^{N,\tau}-m\epsilon^{N,r}\right)
-
(\ell m-1)
=0
$$

Term labels:

- liquidity **benefit** of greater debt
- cost (?) lower labor supply
- cost: redistribution from workers to savers

**Image note:** Colored bars underneath the optimality condition identify the liquidity-benefit term, labor-supply-cost term, and redistribution-cost term.


## Slide 17: The RSS first order condition

Visible chart text:

- Interest rate $r$
- $1/\beta - 1$
- Labor income tax $\tau$
- $0\%$
- $100\%$
- Optimality condition (for some social discount factor $\delta$)
- gov. budget constraint
- Ramsey steady state
- immiseration (zero income)

**Image note:** A diagram plots interest rate $r$ against labor income tax $\tau$. A downward-sloping optimality-condition curve intersects an upward-sloping government-budget-constraint curve; an orange arrow marks the intersection as the Ramsey steady state. A blue dotted vertical line near $100\%$ tax is labeled “immiseration (zero income).”


## Slide 18: 3. Searching for an RSS

3. Searching for an RSS


## Slide 19: Utility functions

- To solve this system of equations, need to go to the computer.

- Begin with $u(c,n)=\log c-v(n)$ with constant Frisch elasticity $=1$

- Standard calibration: (details are not important)
  - AR(1) income process, initial debt $=100\%$, $G=20\%$, initial $r=2\%$

- **Idea:** For each $\tau$, solve government budget constraint for $r$ and evaluate FOC


## Slide 20: The missing RSS

- Assume “correct” social discount factor, $\delta=\beta$. Left hand side of FOC:

$$
\left(1-\beta(1+r)\right)\ell
\left(m\epsilon^{A,r}+\epsilon^{A,\tau}\right)
-
\frac{\tau}{1-\tau}
\left(-\epsilon^{N,\tau}-m\epsilon^{N,r}\right)
-
(\ell m-1)
$$

Term labels:

- liquidity **benefit** of greater debt
- cost: lower labor supply
- benefit: greater labor supply
- cost: redistribution

Always $>0$!

No RSS!

labor supply effect positive!

Chart legend:

- total
- liquidity
- labor
- redistribution

Chart axis label:

- labor tax rate $\tau$

**Image note:** The chart plots the left-hand side of the FOC and its components against the labor tax rate. The black total line stays above zero, supporting the slide’s “No RSS!” conclusion. The red labor component is labeled as having a positive labor-supply effect.


## Slide 21: Optimal steady state exists

- Same with infinitely patient planner, $\delta=1$:

$$
\left(1-(1+r)\right)\ell
\left(m\epsilon^{A,r}+\epsilon^{A,\tau}\right)
-
\frac{\tau}{1-\tau}
\left(-\epsilon^{N,\tau}-m\epsilon^{N,r}\right)
-
(\ell m-1)
$$

Term labels:

- liquidity **benefit** of greater debt
- cost: lower labor supply
- cost: redistribution

unique OSS exists!

labor supply effect negative!

Chart legend:

- total
- liquidity
- labor
- redistribution

Chart axis label:

- labor tax rate $\tau$

**Image note:** The chart plots the FOC components for $\delta=1$. The black total line crosses zero once, and the slide labels this as a unique optimal steady state. The red labor component is negative and labeled “labor supply effect negative!”


## Slide 22: How the RSS vanishes

- Next, vary social discount factor $\delta$ between $\beta$ and $1$:

Visible chart text:

- Consumption drops to zero!
- Labor tax approaches $100\%$
- RSS
- OSS
- RSS
- OSS
- Debt

Left chart legend:

- GDP
- Consumption

Right chart legend:

- After-tax wage
- Labor tax

Chart axis label:

- Social discount factor

**Image note:** Two charts show outcomes as the social discount factor moves from the RSS region toward the OSS. The left chart shows GDP and consumption, with consumption dropping toward zero near the RSS end. The right chart shows the labor tax approaching $100\%$ and the after-tax wage approaching zero near the RSS end.


## Slide 23: Standard Aiyagari economy: Why no RSS?

**Benefits and costs** to greater liquidity and higher labor taxes

Visible boxes:

- liquidity benefit
- labor supply $\uparrow$
- labor supply $\downarrow$
- redistribution

cost of redistribution is quantitatively small!

**Image note:** A balance-scale diagram contrasts benefits and costs. The “labor supply $\downarrow$” cost box is crossed out with a red X, while an arrow emphasizes that the redistribution cost is quantitatively small.


## Slide 24: Taking stock

- New method to compute Ramsey steady states in richer models than RA, TA

- Discounted elasticities of “sequence space” functions are key!

- **Insight:** RSS very extreme for standard balanced-growth Aiyagari models!

- Wide open field with many possible applications !


## Slide 25: THANK YOU !!

THANK YOU !!
