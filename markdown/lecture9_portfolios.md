## Slide 1: Endogenous portfolios and risk premia

Adrien Auclert

Goethe Heterogeneous-Agent Macro Workshop, 2026

## Slide 2: Portfolios in heterogeneous-agent macro

- **So far:** single asset models (from the perspective of households)
- In models with several assets available, used “mutual fund trick”
  - see stocks + bonds model, but could also do this with nominal and real bonds, short and long term bonds, home and foreign bonds...
  - from this we got no-arbitrage conditions + initial $r_0^p$
- **Now:** what if we let households trade these different assets directly?
  - MIT shock world: portfolios are **indeterminate**
    - can feed in distribution of portfolios from the data
  - Expected shocks world: portfolios are **determinate!**

## Slide 3: What does second order perturbation give us?

Orders in aggregate risk:

- 2nd order
- 1st order
- 0th order

Image note: Diagram with “Steady state” at 0th order pointing up to “IRFs” at 1st order; “Exog. portfolios” also points to “IRFs.” Text near the arrow says “e.g. via SSJ, Reiter, etc.”

## Slide 4: What does second order perturbation give us?

Orders in aggregate risk:

- 2nd order
- 1st order
- 0th order

Image note: Diagram with “Steady state” at 0th order, “IRFs” at 1st order, “Steady state risk premium” at 2nd order, and “Endog. portfolios” at 0th order. Arrows show steady state leading to IRFs and risk premium, with endogenous portfolios interacting with IRFs and the risk premium.

## Slide 5: What does second order perturbation give us?

Orders in aggregate risk:

- 2nd order
- 1st order
- 0th order

Augmented SSJ

Image note: Diagram similar to Slide 4, highlighting “Augmented SSJ.” Arrows run from “Steady state” to “IRFs,” from “IRFs” to “Steady state risk premium,” and from “IRFs” to “Endog. portfolios.”

## Slide 6: Canonical model with locally complete markets

## Slide 7: General setting (one account, many assets)

- Heterogeneous households $i$ can allocate wealth $a_i$ to $K+1$ assets
- Aggregate risk: random variable $\epsilon$; asset $k$ has stochastic return $R^k(\epsilon)$
- Given value function $V_i$, problem of household $i$ is:

$$
\max_{\{a_i^k\}}
\mathbb{E}_{\epsilon}
\left[
V_i\left(
\sum_{k=0}^{K} R^k(\epsilon)a_i^k,\epsilon
\right)
\right]
\quad
\text{s.t.}
\quad
\sum_{k=0}^{K} a_i^k = a_i
$$

- Classic first-order condition, letting $\gamma_i \equiv$ multiplier on $i$'s budget constraint:

$$
\mathbb{E}_{\epsilon}
\left[
R^k(\epsilon)\frac{\partial V_i}{\partial a}(\epsilon)
\right]
=
\gamma_i
\quad
\forall i,k
$$

## Slide 8: Implications of asset spanning

- Suppose finite $\epsilon$'s (label one $\epsilon_{ss}$). With enough assets, we get **complete markets**:

$$
\frac{\frac{\partial V_i}{\partial a}(\epsilon)}
{\frac{\partial V_i}{\partial a}(\epsilon_{ss})}
=
\lambda(\epsilon)
\quad
\forall \epsilon
$$

- $\lambda$ is (cross-sectional) stochastic discount factor, gives us risk premia:

$$
\mathbb{E}_{\epsilon}
\left[
R^k(\epsilon)-R^0(\epsilon)
\right]
=
-
\operatorname{Cov}_{\epsilon}
\left(
R^k(\epsilon)-R^0(\epsilon),
\frac{\lambda(\epsilon)}
{\mathbb{E}_{\epsilon}[\lambda(\epsilon)]}
\right)
\quad
\forall k
$$

- With continuous $\epsilon$'s, but finite $K$, can still get this “locally” (ie to 1st-order)
  - 2nd-order perturbation to $\epsilon$ shows we need $K \ge \dim \epsilon$ + spanning condition
  - “0th order portfolios” $a_i^k$; well-defined in the limit as $\epsilon \to \epsilon_{ss}$

[eg Tille-van Wincoop 2010, Devereux-Sutherland 2011, Coeurdacier-Rey 2013, etc.]

## Slide 9: Application to one-account, many-asset model

- Consider now standard one-account model with idiosyncratic risk $e$ + aggregate risk:

$$
V_t(a_0,\ldots,a_K,e)
=
\max_{c,\{a_k'\}}
\frac{c^{1-\sigma}}{1-\sigma}
+
\beta
\mathbb{E}
\left[
V_{t+1}(a_0',\ldots,a_K',e')
\right]
$$

$$
c+\sum_{k=0}^{K} a_k'
=
\sum_{k=0}^{K} R_t^k a_k + W_t e,
\qquad
\sum_{k=0}^{K} a_k' \ge \underline{a}
$$

- Say all agg. risk realized at date 0. For $t \ge 1$: same return $R_t$, only $a \equiv \sum a_k$ matters

$$
V_t(a,e)
=
\max_{c,a'}
\frac{c^{1-\sigma}}{1-\sigma}
+
\beta
\mathbb{E}
\left[
V_{t+1}(a',e')
\right]
$$

$$
c+a' = R_t a + W_t e,
\qquad
a' \ge \underline{a}
$$

## Slide 10: Complete markets in the one-account model

- At $t=0$, $\epsilon$ realizes, so paths $R_t^k(\epsilon)$ and $W_t(\epsilon)$ for $t \ge 0$ become known
- At $t=-1$, using envelope $\partial V/\partial a = c^{-\sigma}$, the risk-sharing condition is:

$$
\frac{
\mathbb{E}_e
\left[
c_0^{-\sigma}
\left(
a_0(a_{ss},e_-,\epsilon),e,\epsilon
\right)
\mid e_-
\right]
}{
\mathbb{E}_e
\left[
c_{ss}^{-\sigma}
\left(
a_{ss},e,\epsilon_{ss}
\right)
\mid e_-
\right]
}
=
\lambda(\epsilon)
\quad
\forall \epsilon
$$

- Can use this to **test** for portfolio optimality and **solve** for optimal portfolios
- Equivalently: solve for “transfers” $t_0(a_{ss},e_-,\epsilon)$ relative to baseline portfolios:

$$
\frac{
\mathbb{E}_e
\left[
c_0^{-\sigma}
\left(
a_{ss}+t_0(a_{ss},e_-,\epsilon),e,\epsilon
\right)
\mid e_-
\right]
}{
\mathbb{E}_e
\left[
c_{ss}^{-\sigma}
\left(
a_{ss},e,\epsilon_{ss}
\right)
\mid e_-
\right]
}
=
\lambda(\epsilon)
\quad
\forall \epsilon
$$

  - Later, figure out what portfolios decentralize these transfers

## Slide 11: First-order complete markets heuristic

- Write $\partial c_{i0}$ for date-0 consumption response to shock under baseline portfolios
- To first-order, risk sharing condition says (heuristically):

$$
\frac{d c_{i0}}{c_{i0}}
=
\frac{\partial c_{i0}+mpc_{i0}\,dt_{i0}}{c_{i0}}
=
-\frac{d\lambda}{\sigma}
$$

- Impose $\mathbb{E}_I[dt_{i0}]=0$ to solve for sdf $d\lambda$ and equilibrium transfer $dt_{i0}$:

$$
-\frac{d\lambda}{\sigma}
=
\frac{dc_{i0}}{c_{i0}}
=
\mathbb{E}_I
\left[
\frac{
\frac{c_{i0}}{mpc_{i0}}
}{
\mathbb{E}_I\left[\frac{c_{i0}}{mpc_{i0}}\right]
}
\frac{\partial c_{i0}}{c_{i0}}
\right]
$$

$$
dt_{i0}
=
\frac{
-\frac{d\lambda}{\sigma}c_{i0}
-
\partial c_{i0}
}{
mpc_{i0}
}
$$

➡ Complete markets $\sim$ **undo the heterogeneous consumption effects of shocks**

## Slide 12: General equilibrium

- Consider now general equilibrium:

Image note: Flow diagram: “Shock $\epsilon$” points to “Prices $R_t^k,W_t$,” which points to “Household choices,” which points to “Market clearing.” A feedback arrow goes from market clearing back to prices. A red “Complete market transfers” box interacts with household choices. Red text says “Additional fixed point problem!”

## Slide 13: General equilibrium solution with SSJ

- Tackle this with SSJ as follows
- Just “correct” the household Jacobian for effect of complete markets
- With this correction applied, solve equilibrium as usual in SSJ!
- This correction has simple form!

Image note: Flow diagram: “Shock $\epsilon$” points to “Prices $R_t^k,W_t$,” which points to “Household choices incl. transfers,” which points to “Market clearing,” with a feedback arrow from market clearing to prices. Red boxes labeled “Portfolios” and “Risk premia” connect to prices and household choices.

## Slide 14: Implementation of correction in SSJ

- Intertemporal MPC matrix $\mathbf{M}$: $M_{ts}=\partial C_t/\partial W_s$
- Wage change at $s$ has direct effect on policies $\partial c_{0i}^s$
- From optimal risk-sharing, get date-0 transfer $dt_{0i}^s$
- Together, these imply change in distribution of assets coming into date 0 $\mathcal{D}_s$
- In turn, this affects consumption at $t$ by $\mathcal{E}'_t\mathcal{D}_s$ ($\mathcal{E}_t$ is expectation function for $C$)
- Hence, **simple correction** to sequence space Jacobian gives us effect under CM:

$$
M_{t,s}^{CM}
\equiv
M_{t,s}^{exo}
+
\mathcal{E}'_t \mathcal{D}_s
$$

- See notebook for additional details!

## Slide 15: Sanity check: replicates known state-space results!

- Consider original Krusell-Smith (97) model: TFP shock, 2 assets capital+bond
- Portfolio constraints $k \ge 0, b \ge \underline{b}$ [needs modified, iterative algorithm, cf paper]

Image note: Two-panel comparison. Left panel reproduces a Krusell-Smith paper figure with axes “Total Investment” and “Individual Wealth” and caption “FIGURE 3. Portfolio decision rules of an employed agent: thick line = capital, thin line = bonds.” Right panel is titled “Portfolio positions in capital (solid) and bonds (dashed),” with legend “employed” and x-axis “Asset choice for the next period.” No matching saved PDF in `notebooks/lecture9_portfolios.ipynb`.

## Slide 16: Application to canonical HANK model with traded stocks

## Slide 17: Canonical HANK model

- Application to canonical HANK model
- We now let households trade stocks and bonds directly:

$$
\max_{\{c_{it}\}}
\mathbb{E}_0
\sum_{t=0}^{\infty}
\beta_{it}
\left(
u(c_{it})-v(N_t)
\right)
$$

$$
c_{it}+p_t s_{it}+b_{it}
\le
(p_t+d_t)s_{it-1}
+
(1+r_{t-1})b_{it-1}
+
(1-\tau_t)\frac{W_t}{P_t}e_{it}
$$

$$
p_t s_{it}+b_{it}\ge 0
$$

- $s$ stocks (price $p_t$, dividends $d_t$), $b$ bonds, assume $\sigma=1$
- Rest of the model is as usual, $B_{ss}=0$ (so Werning equivalence result applies)

## Slide 18: Example 1: balanced-budget $\{G_t\}$ shock

No effect from portfolio choice!

Why? Homogeneous consumption effects at exogenous portfolios,

$$
dc_{i0}=0
$$

For endog. portfolios to matter, need unequal consumption effects of shocks

Also, here stock prices constant -> no difference between bonds and stocks

Image note: Four impulse-response charts. Chart titles: “Government spending,” “Output,” “Consumption,” and “Ex-post return on stocks.” X-axis label: “Quarters.” Y-axis labels include “% of $Y_{ss}$” and “%.” Legend: “Exogenous portfolios (100% in stock market)” and “Endogenous portfolios.” The output paths overlap, while consumption and ex-post stock returns are essentially flat at zero. No matching saved PDF in `notebooks/lecture9_portfolios.ipynb`.

## Slide 19: Example 2: monetary policy $\{r_t\}$ shock

Still no effect from portfolio choice!

100% stock portfolios + log utility: homogeneous effects of monetary policy (Werning result!)

100% stocks are only optimal portfolios here

Image note: Four impulse-response charts. Chart titles: “Monetary policy shock,” “Output,” “Consumption,” and “Ex-post return on stocks.” X-axis label: “Quarters.” Y-axis labels include “% of $Y_{ss}$” and “%.” Legend: “Exogenous portfolio (100% in stock market)” and “Endogenous portfolio.” The exogenous and endogenous portfolio lines overlap closely in all panels. Related output response appears in `notebooks/lecture9_portfolios.ipynb`, but there is no matching saved PDF.

## Slide 20: Example 3: deficit-financed transfer $\{B_t\}$ shock

Large baseline output effects of deficit financed fiscal policy....

Largely undone by endogenous portfolios!

Poor disproportionately affected by shock, reduce stock exposure

But... how?

Image note: Four impulse-response charts. Chart titles: “Deficit-financed shock,” “Output,” “Consumption,” and “Ex-post return on stocks.” X-axis label: “Quarters.” Y-axis labels include “% of $Y_{ss}$” and “%.” The deficit-financed shock panel has legend “Government debt” and “Tax revenue.” Other panels compare “Exogenous portfolio (100% in stock market)” with “Endogenous portfolio.” Endogenous portfolios reduce the output and consumption responses relative to the exogenous portfolio baseline. Related output response appears in `notebooks/lecture9_portfolios.ipynb`, but there is no matching saved PDF.

## Slide 21: Under the hood: implausible portfolio shares!

We didn’t restrict gross positions in assets: borrowing constraint applied only to net position!

So “complete markets” transfers achieved with ultra-levered short-selling by the poor.

Image note: Chart titled “Fraction of portfolio in equity.” Y-axis: “Fraction invested in equity.” X-axis: “Asset choice for the next period $a'$.” Legend entries: “low beta (income level 4),” “high beta (income level 4),” “low beta (income level 16),” “high beta (income level 16),” “low beta (income level 29),” and “high beta (income level 29).” Several lines imply extremely negative equity fractions, reaching into the thousands in magnitude. Related portfolio-share chart appears in `notebooks/lecture9_portfolios.ipynb`, but there is no matching saved PDF.

## Slide 22: With portfolio constraints... (no short sales, 1.5x leverage limit)

Constrained endogenous portfolio now ~same as exogenous portfolio: no effect!

For endog. portfolios to matter, need high-MPC agents to be able to take large gross positions

Image note: Chart titled “Deficit financed fiscal shock.” Y-axis: “% of $Y_{ss}$.” X-axis: “Quarters.” Legend: “Exogenous portfolio (100% in stock market),” “Endogenous portfolio (complete markets),” and “Endogenous portfolio (gross constraints).” With gross constraints, the endogenous portfolio response nearly coincides with the exogenous portfolio response. No matching saved PDF in `notebooks/lecture9_portfolios.ipynb`.

## Slide 23: Conclusion

- Simple modification of sequence-space Jacobian algorithm gives us:
  - impulses with endogenous portfolios and second-order risk premia
  - can add portfolio constraints, incomplete markets (see paper)
  - new directions for asset pricing + heterogeneous agent macro
  - new directions for sequence-space macro
- When do endogenous portfolios matter in canonical HANK model?
  - When shocks have heterogeneous consumption effects
  - When high MPC agents are able to take highly leveraged positions
