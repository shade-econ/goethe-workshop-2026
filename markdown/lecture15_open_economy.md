## Slide 1: Open economy HANK

Open economy HANK

Ludwig Straub

Goethe Heterogeneous-Agent Workshop, 2026


## Slide 2: Open economy HANK

- So far, focus on *closed* economy models of fiscal & monetary policy

- **Next:** *Open* economy. What changes?
  - Exports & imports are new **source** and **destination** for demand
  - Extent to which is controlled by the **exchange rate**

- Material here based on Gali Monacelli (2005) and Auclert, Rognlie, Souchier, Straub (2024)

Exciting other work in this area: de Ferra et al (2020), Cugat (2019), Giagheddu (2020), Zhou (2022), Kekre Lenel (2020), Guo Ottonello Perez (2021), Aggarwal et al (2022), Sundry (2024), Bellifemine Couturier Jamilov (2025, R&R REStud)


## Slide 3: Proceed in three steps

1. Introduce model that nests RA & HA
   - RA model almost literally = Gali Monacelli (2005)
   - HA model: no bonds, but capitalized profits
   - Key parameter: **trade elasticity** $\chi$

2. Effects of **exchange rate shocks** (e.g. due to capital flows or UIP shocks)

3. Paper: Effects of **monetary policy**


## Slide 4: HANK meets Gali-Monacelli

HANK meets Gali-Monacelli


## Slide 5: Model overview

- Small open economy (SOE) model

- Two goods
  - “Home”: $H$, produced at home, $P_{Ht}$ at home, $P^*_{Ht}$ abroad
  - “Foreign”: $F$, produced abroad, $P_{Ft}$ at home, $P^*_{Ft} \equiv 1$ abroad
  - Consumed in bundles. CPI $P_t$ at home, $P^*_t$ abroad

- Two kinds of agents:
  - Large mass of foreign households
  - mass 1 of **HA domestic households**


## Slide 6: Households’ consumption behavior

- Foreigners consume fixed real $C^*$. Home HA solve **intertemporal problem**:

$$
\max_{\{c_{it}\}} \mathbb{E}_0 \sum_{t=0}^{\infty} \beta_{it}
\left(u(c_{it}) - v(N_t)\right)
$$

subject to

$$
c_{it} + a_{it} \leq (1+r^p_t)a_{it-1} + Z_t e_{it},
\qquad
a_{it} \geq 0
$$

where $Z_t e_{it}$ is real labor income.

- Domestic & foreign consume CES bundle, solve **intratemporal problem**:

$$
C_{Ht} = (1-\alpha)\left(\frac{P_{Ht}}{P_t}\right)^{-\eta} C_t
$$

$$
C^*_{Ht} = \alpha\left(\frac{P^*_{Ht}}{P^*}\right)^{-\gamma} C^*
$$

- Domestic production and market clearing:

$$
Y_t = N_t = C_{Ht} + C^*_{Ht}
$$


## Slide 7: Prices and nominal rigidities

- Exchange rates: nominal $\mathcal{E}_t$, real $Q_t \equiv \mathcal{E}_t/P_t$, $\uparrow$ is depreciation

- Same wage rigidity as before

$$
\pi_{wt}
=
\kappa_w
\left(
v'(N_t)
-
\frac{\epsilon - 1}{\epsilon}
\frac{W_t}{P_t}
u'(C_t)
\right)
+
\beta \pi_{w,t+1}
$$

- Flexible prices everywhere else:

$$
P_{Ft} = \mathcal{E}_t
$$

$$
P_{Ht} = W_t
$$

$$
P^*_{Ht} = \frac{P_{Ht}}{\mathcal{E}_t}
$$

“Producer currency pricing”


## Slide 8: Monetary policy and assets

Initial positions:

- **Home equity:** 100%
  - Capitalize profits $\left(1-\mu^{-1}\right)Y_t$ with realized return $r^p_t$

- **Home bonds:** 0%
  - Nominal return $i_t$
  - Set by monetary policy to ensure exogenous path of
    $$
    r_t = i_t - \pi_{t+1}
    $$

- **ROW bonds:** 0%
  - Nominal (= real) return $i^*_t$
  - Shocks = shocks to foreign discount factor
  - Set by monetary policy

Arbitrage pins down $r^p_t$.

UIP condition pins down exchange rate:

$$
1+r_t = (1+i^*_t)\frac{Q_{t+1}}{Q_t}
$$

Image note: Diagram shows three asset boxes — Home equity, Home bonds, ROW bonds — with double arrows between them. Downward “Arbitrage” arrows connect home equity/home bonds to $r^p_t$ and home bonds/ROW bonds to the UIP exchange-rate condition.


## Slide 9: Baseline calibration

- Calibrate openness $\alpha = 0.40$ & balanced trade in steady state

- Same HA block as before

- Normalize all prices to 1 in steady state.

- *Note:* HA model already stationary, no need for debt-elastic interest rate

- Next: $i^*_t$ shocks, then (briefly) $r_t$ shocks.


## Slide 10: Capital flows and exchange rates

Capital flows and exchange rates


## Slide 11: Shock

- Temporary shock $i^*_t \uparrow$

  - Real depreciation! Iterate UIP forward:

$$
dQ_t = \frac{1}{1+r}\sum_{s \geq 0} d i^*_{t+s}
$$

- $Q_t \uparrow$, $\frac{P_{Ht}}{P_t} \downarrow$, $\frac{P_{Ht}}{\mathcal{E}_t} \downarrow$

- Demand for home goods?

- First **RA**, then **HA**


## Slide 12: What happens to aggregate demand?

$$
Y_t
=
(1-\alpha)
\left(\frac{P_{Ht}}{P_t}\right)^{-\eta}
C_t
+
\alpha
\left(\frac{P_{Ht}}{\mathcal{E}_t}\right)^{-\gamma}
C^*
$$

**RA:** $C_t = C = \text{const}!$

“Expenditure switching”

The highlighted first term increases with elasticity:

$$
\eta\frac{\alpha}{1-\alpha}
$$

The highlighted second term increases with elasticity:

$$
\gamma\frac{1}{1-\alpha}
$$

Therefore:

$$
dY = \frac{\alpha}{1-\alpha}\chi dQ
$$

Trade elasticity:

$$
\chi \equiv \eta(1-\alpha) + \gamma
$$

Image note: Equation diagram highlights the two price-ratio terms in red boxes and points with a large arrow to the aggregate-demand response formula.


## Slide 13: Representative agent: Exchange rate shock

Image note: Two line charts compare RA responses after an exchange-rate shock. Left chart is “Output, RA” with y-axis “% of GDP” and x-axis “Quarter” from 0 to 30; output rises initially and decays toward zero. Right chart is “Consumption, RA” with flat lines at zero. Legends in both charts: $\chi=1$, $\chi=0.5$, $\chi=0.05$. Generated by `notebooks/lecture15_open_economy.ipynb`; figure `lecture15_output_ra_y_and_c.pdf`.


## Slide 14: DAG

Image note: DAG with a box labeled “shocks $r^*$ / unknowns $Y$.” A horizontal arrow labeled $i^*$ points to “UIP.” From UIP, red arrows labeled $Q$ point to “dom. demand” and “foreign demand.” Domestic demand sends $C_H$ to “Goods market clearing”; foreign demand sends $C^*_H$ to goods market clearing. A dotted arrow labeled $Y$ loops from goods market clearing back to the shocks/unknowns box.


## Slide 15: DAG

Image note: Same DAG as Slide 14, overlaid with three code screenshots for `UIP`, `dom_demand`, and `for_demand`. The right code screenshot is visibly cut off at the slide edge after `# PF_`; clipped code comments below are repaired from `notebooks/lecture15_open_economy.ipynb`. 

Visible code screenshot: `UIP`

```python
@sj.solved(unknowns={'Q': (0.01, 300.)}, targets=['uip'])
def UIP(Q, r, rstar, eta, alpha, gamma):
    # recursive equation for UIP to pin down RER Q
    uip = 1 + r - (1 + rstar) * Q(1) / Q

    # price of H goods abroad in terms of Q
    PHstar = ((Q ** (eta - 1) - alpha) / (1 - alpha)) ** (1 / (1 - eta))

    # price of H goods at home in terms of Q
    PH_P = ((1 - alpha * Q ** (1 - eta)) / (1 - alpha)) ** (1 / (1 - eta))

    # price of F goods at home in terms of Q
    PF_P = Q  # LOOP

    # let's also compute chi, as an important object in the theory
    chi = eta * (1-alpha) + gamma
    return uip, PHstar, PH_P, PF_P, chi
```

Visible code screenshot: `dom_demand`

```python
@sj.simple
def dom_demand(C, PF_P, PH_P, eta, alpha):
    cH = (1 - alpha) * PH_P ** (-eta) * C  # PH_P is the real (in domestic cons. good units) price of the home good consumed domestically
    cF = alpha * PF_P ** (-eta) * C  # PF_P is the real (in domestic cons. good units) price of the foreign good consumed domestically
    return cH, cF
```

Visible code screenshot: `for_demand`

```python
@sj.simple
def for_demand(PHstar, alphastar, gamma, Cstar):
    cHstar = alphastar * PHstar ** (-gamma) * Cstar  # PHstar is the real (in domestic cons. good units) price of the home good consumed abroad
    return cHstar
```


## Slide 16: What changes with heterogeneous agents?

**HA:**

$$
C_t = \mathcal{C}_t\left(r^p_0, \{Z_s\}\right)!
$$

Therefore:

$$
dC
=
\frac{\mathbb{M}}{\mu}
d\left(\frac{P_{Ht}}{P_t}Y_t\right)
+
\mathbf{m}_{A_{ss}}dr^p_0
=
\overline{\mathbb{M}}
d\left(\frac{P_{Ht}}{P_t}Y_t\right)
=
-\frac{\alpha}{1-\alpha}\overline{\mathbb{M}}dQ
+
\overline{\mathbb{M}}dY
$$

Intertemporal MPCs out of total income:

$$
\overline{\mathbb{M}}
\equiv
\frac{1}{\mu}\mathbb{M}
+
\left(1-\frac{1}{\mu}\right)\mathbf{m}q'
$$

Aggregate demand:

$$
Y_t
=
(1-\alpha)
\left(\frac{P_{Ht}}{P_t}\right)^{-\eta}
C_t
+
\alpha
\left(\frac{P_{Ht}}{\mathcal{E}_t}\right)^{-\gamma}
C^*
$$

First highlighted term increases with elasticity:

$$
\eta(1-\alpha)
$$

Second highlighted term increases with elasticity:

$$
\gamma
$$

Result:

$$
dY
=
\frac{\alpha}{1-\alpha}\chi dQ
-
\alpha\overline{\mathbb{M}}dQ
+
(1-\alpha)\overline{\mathbb{M}}dY
$$

- Expenditure switching
- Real income channel
- Multiplier

Image note: Equation diagram highlights the two price-ratio terms in red boxes and labels the final decomposition: red “Expenditure switching,” green “Real income channel,” blue “Multiplier.”


## Slide 17: DAG

Image note: DAG expands Slide 14 by adding household and real-income channels. Box: “shocks $i^*$ / unknowns $Y$.” Nodes: UIP, real income, household, dom. demand, foreign demand, Goods market clearing. Arrows include $i^*$ to UIP; $Q$ from UIP to domestic demand, foreign demand, and real income; $Y$ to real income and back through the goods-market feedback loop; $Z$ from real income to household; $C$ from household to domestic demand; $C_H$ and $C^*_H$ into goods market clearing.


## Slide 18: DAG

Image note: Same HA DAG as Slide 17, overlaid with an income/asset-valuation code screenshot. Some comments in the code screenshot are visibly truncated at the right edge; clipped comments below are repaired from `notebooks/lecture15_open_economy.ipynb`. 

Visible code screenshot:

```python
@sj.solved(unknowns={'J': (0.001, 100.)}, targets=['valuation_cond'])
def income(Y, PH_P, J, r, markup_ss):
    # real labor income
    Z = 1 / markup_ss * PH_P * Y

    # real dividend
    div = (1 - 1 / markup_ss) * PH_P * Y

    # nominal PPP adjusted GDP
    gdp = PH_P * Y

    # valuation condition to price the asset
    valuation_cond = div + J(1) / (1 + r) - J  # J = beginning of period valuation
    j = J(1) / (1 + r)  # j = end of period valuation

    # ex post interest rate incl revaluation
    rp = J / j(-1) - 1

    # get assets to labor income ratio (will need this to calibrate to the household block)
    j_to_Z = j / Z
    return j, valuation_cond, gdp, div, Z, rp, j_to_Z
```


## Slide 19: How do RA and HA compare?

- Assume $\chi = 1$. Then:

$$
dY^{HA} = dY^{RA} = \frac{\alpha}{1-\alpha}dQ
$$

- HA and RA are identical in this case! What about the two new terms? **Cancel!**

$$
\alpha M dQ = (1-\alpha)M dY
$$

- **Intuition:** Depreciation causes just enough of a boom that the loss in real income due to depreciation is offset.

[geeky comment: this is a little like the balanced budget multiplier]

- What if $\chi \neq 1$?


## Slide 20: Contractionary depreciations for low $\chi$

Image note: Two charts compare “Output, RA” and “Output, HA.” Both have x-axis “Quarter” from 0 to 30; left y-axis is “% of GDP.” Legends: $\chi=1$, $\chi=0.5$, $\chi=0.05$. The RA chart shows positive output responses that decay to zero. The HA chart shows equivalence for $\chi=1$, but for low $\chi$ the output response is negative; an orange circle highlights the negative region and text reads “Contractionary depreciation!” Another annotation reads “Equivalence result.” Generated by `notebooks/lecture15_open_economy.ipynb`; figure `lecture15_output_ra_ha.pdf`.

- This is more likely when substitution away from imports is hard (e.g. energy, food)


## Slide 21: What about monetary policy?

Image note: DAG for monetary policy. Box: “shocks $i^*, r$ / unknowns $Y$.” Nodes: household, real income, UIP, dom. demand, foreign demand, Goods market clearing. Purple arrow $r$ goes directly to household. Arrow from shocks to UIP is labeled $r$ and $r^*$. Other arrows show $Y$ to real income, $Q$ from UIP to real income/domestic demand/foreign demand, $Z$ to household, $C$ to domestic demand, $C_H$ and $C^*_H$ into goods market clearing, and dotted feedback $Y$ from goods market clearing back to the shock/unknowns block.


## Slide 22: Summary

- Merged HANK with Gali-Monacelli.
  - Maybe the most natural way to apply HANK to open economies?

- Learned:
  - New channels: **Real income**, **Keynesian Multiplier**
  - Can generate contractionary depreciations for low trade elasticities

- Lots more in paper: Taylor rules, non-trivial gross positions, slow trade adjustments (J curve), non-homothetic demand, DCP, slow pass-through, …
