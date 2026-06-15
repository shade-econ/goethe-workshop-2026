## Slide 1: A HANK Model for the Euro Area and Two Applications

Goethe Workshop, June 2026

Rodolfo Rigato (ECB), based on joint work with Hanno Kase (ECB) and Georg Müller (ECB)

The views expressed here are those of the authors and do not necessarily reflect those of the European Central Bank.

Page/slide number shown: 1

## Slide 2: Introduction

- HANK models are now widely used at central banks
  - One of models at the ECB’s Forecasting and Policy Modelling division: Ciccarelli et al, 2024
- Kase and Rigato (2025): first medium-scale HANK model used in FPM
  - Heterogeneous household block with information stickiness
  - Medium-scale DSGE: investment, price and wage stickiness etc.
  - Various aggregate shocks and policy instruments
  - Estimated on euro area data
- Ongoing work on extending our model along several dimensions
- Today:
  1. Current state of the model, focusing on the household block
  2. Two applications: household savings and fiscal scenarios following an energy shock

Page/slide number shown: 2

## Slide 3: Model overview

- Heterogeneous household block with sticky information
- Nominal rigidities: price and wage stickiness
- Firm block with investment adjustment costs
- Financial frictions block with a financial accelerator mechanism and risk shocks
- Open economy with domestic goods, energy and non-energy imports
- Fiscal policy: government spending, tax rule, and multiple fiscal instruments
- Monetary policy: Taylor rule

Page/slide number shown: 3

## Slide 4: Households

- Households choose consumption $c_{it}$ and liquid asset holdings $b_{it}$ to maximize:

$$
\mathbb{E}_t \sum_{s=0}^{\infty} \beta^s
\exp\left(\sum_{k=0}^{s-1} \varepsilon^C_{t+k}\right)
\left[u(c_{t+s}) - v(n_{t+s})\right]
$$

- The budget constraint is

$$
b_{it} + c_{it}
= y_t e_{it} + (1+r_t^b)b_{i,t-1} + T_{it},
\quad b_{it} \ge \underline{b}
$$

- Disposable income (ex transfers) has a common component $y_t$ and an idiosyncratic term $e_{it}$

$$
y_{it} = (1-\tau_t^{\ell})w_t n_t + (1-\tau_t^d)d_t
$$

- Transfers $T_{it}$ may depend on household characteristics depending on the application

Page/slide number shown: 4

## Slide 5: Sticky information

- Households need to form expectations about $y_t$, $r_t^b$, $\varepsilon_t^C$, and $T_{it}$
- Assume sticky information as in Mankiw and Reis (2002) and Auclert, Rognlie and Straub (2020)
  - Each period, a fraction $1-\lambda$ of households update their information set
- Generates hump-shaped responses of consumption to shocks
- Important degree of freedom when estimating the model
  - Disciplines the time series behavior of $C_t$

Page/slide number shown: 5

## Slide 6: Consumption bundles

- The final good is a CES bundle of energy $C_{Et}$ (imported) and non-energy goods $C_{Nt}$

$$
C_t =
\left[
\omega_E^{1/\eta_E} C_{Et}^{1-1/\eta_E}
+
(1-\omega_E)^{1/\eta_E} C_{Nt}^{1-1/\eta_E}
\right]^{\eta_E/(\eta_E-1)}
$$

- Non-energy goods are a CES bundle of domestic goods $C_{Ht}$ and non-energy imports $C_{Ft}$

$$
C_{Nt} =
\left[
\omega_F^{1/\eta} C_{Ft}^{1-1/\eta}
+
(1-\omega_F)^{1/\eta} C_{Ht}^{1-1/\eta}
\right]^{\eta/(\eta-1)}
$$

- Elasticity $\eta_E < \eta \rightarrow$ difficult to substitute away from energy
- Assume bundles are adjusted infrequently as in Auclert et al. (2024)
  - Each period, a fraction $1-\theta^C$ of households update their entire consumption bundle
- Analogous problem for investment and government consumption

Page/slide number shown: 6

## Slide 7: Mutual fund

- Risk neutral, holds long-term government bonds, equity, and foreign bonds
- The total value of its assets is $A_t$ evolves according to

$$
A_t = (1+r_t^a)A_{t-1} - d_t
$$

- $r_t^a$ is the total return on its portfolio and $d_t$ is the dividend paid to households
- Dividends are determined by the following rule:

$$
d_t = d + \chi\left[(1+r_t^a)A_{t-1} - (1+r^a)A\right]
$$

- The parameter $\chi$ governs how fast consumption responds to changes in financial wealth

Page/slide number shown: 7

## Slide 8: Marginal propensities to consume

- Target an average MPC of $0.25$ and $r = 1\%$ p.a.
  - Requires $B = 70\%$ of annual GDP, $\beta = 0.992$
  - Results in an income-weighted MPC of $0.14$
- Calibrate $\chi$ to target annual MPCs out of capital gains
  - Chodorow-Reich, Nenov and Simsek (2021) find $0.032$
  - Our model gives $0.028$ and $0.042$ over the first two years
  - This requires $\chi = 0.035$ (for $\lambda = 0.92$)

Image note: Line chart titled “Marginal propensities to consume.” X-axis: “Quarters” from 1 to 8. Legend: Lump-sum, Income-weighted, Capital gains. Lump-sum and income-weighted MPCs fall sharply after quarter 1; capital-gains MPC is much smaller and rises gradually.

Page/slide number shown: 8

## Slide 9: Monetary shock IRFs

Image note: Six-panel IRF chart for a monetary shock. Panels: “Output (% s.s.),” “Price level (%),” “Nominal interest rate (p.p.),” “Consumption (% s.s.),” “Investment (% s.s.),” and “Nominal exchange rate (%).” All x-axes are “Quarters,” with ticks at 0, 4, 8, 12, and 16. Legend compares “HANK model” and “Empirical meta-analysis” in the first three panels, with a shaded empirical uncertainty band. Output, price level, consumption, and investment decline after the shock and then recover; the nominal interest rate jumps and decays; the nominal exchange rate initially drops sharply and then partially recovers.

Page/slide number shown: 9

## Slide 10: Applications

Applications

Page/slide number shown: none visible

## Slide 11: Application 1: household savings

- Household savings substantially higher than pre-pandemic levels
- Potential explanations (Bobasu, Gareis and Stoevsky, 2024):
  - Increased uncertainty
  - Tight labor markets and higher wages
  - Need to rebuild real wealth after the inflation spike
  - Higher interest rates

Image note: Line chart titled “Household savings rate (% disposable income).” X-axis shows years 2022, 2023, 2024, and 2025. Legend: Savings rate; Pre-COVID average. The savings rate falls early in 2022, then rises through 2023–2024 and remains above the dashed pre-COVID average.

Page/slide number shown: 10

## Slide 12: Substantial heterogeneity in perceived uncertainty

- ECB Consumer Expectations Survey results from Dimou, Dossche, Hütten and Kocharkoc (2026)
- Can uncertainty at the bottom of the income distribution be a risk to GDP growth?
  - More generally, can microdata be informative about macroeconomic risks?

Image note: Embedded stacked bar chart titled “Perceived uncertainty, by household type,” with subtitle “percentages of respondents, weighted.” Legend: “Easy to predict own financial situation (lower uncertainty)” and “Difficult to predict own financial situation (higher uncertainty).” Categories include liquidity-constrained households: Yes, No; and employment status: Unemployed, Employed high job-loss probability, Employed low job-loss probability. The chart shows substantially higher perceived uncertainty among liquidity-constrained and unemployed households.

Page/slide number shown: 11

## Slide 13: Can stronger saving at the bottom affect aggregate consumption?

- Response of consumption to a discount factor shock decomposed into income terciles
  - Not exactly the same as an uncertainty shock, but works as a proxy
- Stronger saving incentives at the bottom have limited effects on aggregate consumption
- The bottom of the income distribution accounts for a small share of consumption

Image note: Two stacked-area charts. Left panel: “Consumption (% s.s.).” Right panel: “Savings rate (% disposable income).” X-axes: “Quarters” from 0 to 20. Legend: Bottom, Middle, Top, Total. The consumption response is driven mainly by the top tercile; the total savings-rate response starts near 1% of disposable income and fades toward zero.

Page/slide number shown: 12

## Slide 14: But some shocks propagate strongly through the bottom of the distribution: energy price shock

- Response of consumption to an increase in imported energy prices
  - Higher energy prices $\rightarrow$ lower disposable income $\rightarrow$ operates via MPCs
- Strong contribution coming from the bottom tercile: low consumption share, but high MPCs
- Savings are still driven by the top
- More details in Battistini, Bobasu, Kase and Rigato (2026)

Image note: Two stacked-area charts for an imported energy price shock. Left panel: “Consumption (% s.s.).” Right panel: “Savings rate (% disposable income).” X-axes: “Quarters” from 0 to 20. Legend: Bottom, Middle, Top, Total. The total consumption response falls sharply, with a large contribution from the bottom tercile despite its lower consumption share; the savings-rate response is strongly negative initially and then moves back toward zero.

Page/slide number shown: 13

## Slide 15: Application 2: fiscal policy scenarios following an energy shock

- Large increase in oil and energy prices in the past few months
- In the last energy crisis, governments responded with a mix of fiscal instruments
- How effective are these instruments and how do they affect real GDP and inflation projections?
- Compare illustrative fiscal policy scenarios based on different instruments
  - Targeted transfers to households (transfer to the lower tercile)
  - Untargeted (lump-sum) transfers
  - Subsidies on imported energy

Page/slide number shown: 14

## Slide 16: Effects of fiscal policy on GDP and inflation

- Fiscal multipliers: targeted transfers $>$ energy subsidies $>$ untargeted transfers
  - Energy subsidies also stimulate investment
- Muted effects on inflation for transfers: flat Phillips curve
- Mechanical effect on energy subsidies, but also second-round effects

Image note: Three-panel chart. Left panel: “Fiscal stimulus (% of s.s. output),” showing stimulus around 0.5 for the first few quarters and then falling to zero. Middle panel: “Output (% s.s.).” Right panel: “Inflation (% y-o-y).” X-axes: “Quarters” from 0 to 12. Legend: Lump-sum transfers, Targeted transfers, Imported energy subsidy. Targeted transfers generate the largest output response; imported energy subsidies have a strong mechanical disinflationary effect initially, followed by positive second-round inflation effects.

Page/slide number shown: 15

## Slide 17: Different fiscal policy scenarios

Image note: Four-panel scenario chart with legend: March 2026 staff projections, Lump-sum transfers, Targeted transfers, Imported energy subsidy. Panels: “Fiscal stimulus (as % of 2026Q1 GDP),” “HICP inflation (% y-o-y),” “Real GDP (2026Q1 = 100),” and “Real GDP (% y-o-y growth).” X-axis labels run from Q1 2026 through Q4 2028. The fiscal stimulus path rises to about 0.5% of 2026Q1 GDP, stays there through early 2027, and then returns to zero; the policy scenarios differ mainly in inflation timing and year-over-year GDP growth, while real GDP levels converge by 2028.

Page/slide number shown: 16

## Slide 18: Takeaways

- Substantial progress in HANK modelling at FPM over the past few years
- What this framework lets us do:
  - Identify macroeconomic risks using microdata
  - Assess the effectiveness of different policy instruments
  - Different transmission channels relative to other models
  - Inequality matters in its own right
- We welcome your comments and suggestions!
- Feel free to reach out at rodolfo.dinis_rigato@ecb.europa.eu

Page/slide number shown: 17
