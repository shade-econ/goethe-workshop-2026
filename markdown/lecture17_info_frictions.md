## Slide 1: Information frictions

Information frictions

Ludwig Straub

Goethe Heterogeneous-Agent Workshop, 2026

## Slide 2: Information frictions

- So far, have assumed full information & rational expectations (“FIRE”)

- Next: Deviations from FIRE (“information frictions”)
  - incomplete information (e.g. noisy information, sticky information)
  - deviations from rational expectations (e.g. cognitive discounting, level $k$ thinking)

- Leading contender to explain key puzzles in macro & finance, e.g.
  - Why do $\{\pi_t, I_t, C_t\}$ respond so sluggishly to aggregate shocks?
    (but not to idiosyncratic shocks)
  - Why do asset prices overreact to shocks?

## Slide 3: A slight problem

- Deviations from FIRE already hard to simulate within simple RA models!
  - e.g. Mankiw Reis 2007, Mackowiak Wiederholt 2015

## Slide 4: A slight problem

- Deviations from FIRE already hard to simulate within simple RA models!
  - e.g. Mankiw Reis 2007, Mackowiak Wiederholt 2015

Image note: Screenshot of a paper overlaid on the slide. Visible text includes: “STICKY INFORMATION IN GENERAL EQUILIBRIUM”; “N. Gregory Mankiw, Harvard University”; “Ricardo Reis, Princeton University”; “3. Solving for the Economy’s Dynamics.” The highlighted excerpt says that the model involves both an infinite number of past expectations of the present through sticky information and present expectations of variables at an infinite number of future dates through intertemporal smoothing, implying an infinite-dimensional state space that current algorithms cannot handle.

## Slide 5: A slight problem

- Deviations from FIRE already hard to simulate within simple RA models!
  - e.g. Mankiw Reis 2007, Mackowiak Wiederholt 2015

- Goal: Coherent framework to model and simulate deviations from FIRE
  - … not just RA, but also HA! (or any other block …)

- Materials here mostly a version of the approach we have developed for “Micro Jumps, Macro Humps…”

## Slide 6: Introductory example

Introductory example

## Slide 7: Monetary policy with myopic agents

- IKC equation for monetary policy

$$
dY = M^r dr - M dT + M dY
$$

- Imagine households are myopic:
  - only start responding to $dr_t$ at date $t$
  - only start responding to $dT_t$ at date $t$
  - only start responding to $dY_t$ at date $t$

- What is $dY$ in this case?

Image note: Arrow annotation points to the $dT$ term and says: $dT =$ endogenous tax adjustment to $dr$.

## Slide 8: Manipulating Jacobians

- Take the intertemporal MPC matrix … Is it still correct with myopia?

Response to income increase at $s = 0$

$$
M =
\begin{pmatrix}
M_{00} & M_{01} & M_{02} & M_{03} & \cdots \\
M_{10} & M_{11} & M_{12} & M_{13} & \cdots \\
M_{20} & M_{21} & M_{22} & M_{23} & \cdots \\
M_{30} & M_{31} & M_{32} & M_{33} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

Still correct with myopia? ✓

Image note: The first column of the matrix is highlighted, with a check mark indicating the $s=0$ response remains correct.

## Slide 9: Manipulating Jacobians

- Take the intertemporal MPC matrix … Is it still correct with myopia?

Response to income increase at $s = 1$

$$
M =
\begin{pmatrix}
M_{00} & M_{01} & M_{02} & M_{03} & \cdots \\
M_{10} & M_{11} & M_{12} & M_{13} & \cdots \\
M_{20} & M_{21} & M_{22} & M_{23} & \cdots \\
M_{30} & M_{31} & M_{32} & M_{33} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

Still correct with myopia? ✓ ×

Image note: The second column is highlighted. A red × marks $M_{01}$, indicating that entry is not correct with myopia.

## Slide 10: Manipulating Jacobians

- Take the intertemporal MPC matrix … Is it still correct with myopia?

Response to income increase at $s = 2$

$$
M =
\begin{pmatrix}
M_{00} & M_{01} & M_{02} & M_{03} & \cdots \\
M_{10} & M_{11} & M_{12} & M_{13} & \cdots \\
M_{20} & M_{21} & M_{22} & M_{23} & \cdots \\
M_{30} & M_{31} & M_{32} & M_{33} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

Still correct with myopia? ✓ × ×

Image note: The third column is highlighted. Red × marks appear on the entries above the diagonal in earlier/future-response columns, showing which entries fail under myopia.

## Slide 11: Manipulating Jacobians

- Take the intertemporal MPC matrix … Is it still correct with myopia?

Response to income increase at $s = 3$

$$
M =
\begin{pmatrix}
M_{00} & M_{01} & M_{02} & M_{03} & \cdots \\
M_{10} & M_{11} & M_{12} & M_{13} & \cdots \\
M_{20} & M_{21} & M_{22} & M_{23} & \cdots \\
M_{30} & M_{31} & M_{32} & M_{33} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

Still correct with myopia? ✓ × × ×

Do we need to modify the other entries in each column?

Image note: The fourth column is highlighted. Red × marks indicate entries above the diagonal that are incorrect under myopia; a callout asks whether other entries in each column must also be modified.

## Slide 12: Manipulating Jacobians

- Take the intertemporal MPC matrix … Is it still correct with myopia?

$$
M =
\begin{pmatrix}
M_{00} & 0      & M_{02} & M_{03} & \cdots \\
M_{10} & M_{00} & M_{12} & M_{13} & \cdots \\
M_{20} & M_{10} & M_{22} & M_{23} & \cdots \\
M_{30} & M_{20} & M_{32} & M_{33} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

Image note: Red arrows show the first-column unanticipated-shock responses being shifted into the second column, with the top entry set to zero.

## Slide 13: Manipulating Jacobians

- Take the intertemporal MPC matrix … Is it still correct with myopia?

$$
M =
\begin{pmatrix}
M_{00} & 0      & 0      & M_{03} & \cdots \\
M_{10} & M_{00} & 0      & M_{13} & \cdots \\
M_{20} & M_{10} & M_{00} & M_{23} & \cdots \\
M_{30} & M_{20} & M_{10} & M_{33} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

Image note: The diagram continues the same replacement logic, shifting the unanticipated-shock response pattern into later columns and setting entries above the diagonal to zero.

## Slide 14: Manipulating Jacobians

- Take the intertemporal MPC matrix … Is it still correct with myopia?

$$
M =
\begin{pmatrix}
M_{00} & 0      & 0      & 0      & \cdots \\
M_{10} & M_{00} & 0      & 0      & \cdots \\
M_{20} & M_{10} & M_{00} & 0      & \cdots \\
M_{30} & M_{20} & M_{10} & M_{00} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

After date $s$, $M_{t,s}$ is just like the date $t-s$ response to an unanticipated shock!

Image note: The final modified matrix is lower-triangular Toeplitz: entries above the diagonal are zero and each column repeats the unanticipated-shock response shifted downward.

## Slide 15: Expectations matrix

- Another way to look at this: What are expectations about a date-$s$ shock?

- Define matrix $E$ that in column $s$ has the expectations about date-$s$ shock of 1

$$
E =
\begin{pmatrix}
1 & 1 & 1 & 1 & \cdots \\
1 & 1 & 1 & 1 & \cdots \\
1 & 1 & 1 & 1 & \cdots \\
1 & 1 & 1 & 1 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
\quad \rightsquigarrow \quad
E =
\begin{pmatrix}
1 & 0 & 0 & 0 & \cdots \\
1 & 1 & 0 & 0 & \cdots \\
1 & 1 & 1 & 0 & \cdots \\
1 & 1 & 1 & 1 & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

- $E_{t,s} dY_s$ is then the expected value of $dY_s$ at date $t$.

## Slide 16: Solving the myopic IKC

- How can we solve for the GE response of $dY$ then?

$$
dY = M^r dr - M dT + M dY
$$

- With zero new computational burden, we can solve our myopic economy!

Image note: Two line charts compare responses. Left chart: “Response to $t=0$ rate cut,” x-axis “Quarter,” y-axis “% of output.” Right chart: “Response to $t=40$ rate cut,” x-axis “Quarter.” Legend: FIRE; myopic $M$; myopic $M$ and $M^r$. The myopic responses are smaller and more hump-shaped, and the $t=40$ response is delayed until the future rate cut date. Generated by `notebooks/lecture17_info_frictions.ipynb`; figure `lecture17_full_sticky_exp.pdf`.

## Slide 17: Solving myopic IKC for fiscal policy

- Another application: Imagine we want to solve for fiscal multipliers but agents expect neither future taxes nor future income.

- What’s the right IKC?

$$
dY = dG - M dT + M dY
$$

- Next: Generalize this to more general models of belief formation!

## Slide 18: Two general assumptions we make

- We make two implicit assumptions

- Agents are only “behavioral” about future changes in aggregate variables
  - steady state unaffected
  - not behavioral w.r.t. idiosyncratic income process

- Deviations from FIRE are orthogonal to idiosyncratic state
  - can relax, but too much today. See Guerreiro (2022).

## Slide 19: General Expectations matrices

General Expectations matrices

## Slide 20: Typical example

$$
E =
\begin{pmatrix}
1 & \ast & \ast & \ast & \cdots \\
1 & 1    & \ast & \ast & \cdots \\
1 & 1    & 1    & \ast & \cdots \\
1 & 1    & 1    & 1    & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

## Slide 21: Typical example

Like a news shock at date 1, that one period later $dY$ goes up by 0.3

$$
E =
\begin{pmatrix}
1 & 0.4 & 0.3 & 0.2 & \cdots \\
1 & 1   & 0.6 & 0.4 & \cdots \\
1 & 1   & 1   & 0.8 & \cdots \\
1 & 1   & 1   & 1   & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

Image note: Orange highlight emphasizes the entries $0.3$ and $0.6$ in the same expectations column.

## Slide 22: Typical example

Like a news shock at date 1, that two periods later $dY$ goes up by 0.2

$$
E =
\begin{pmatrix}
1 & 0.4 & 0.3 & 0.2 & \cdots \\
1 & 1   & 0.6 & 0.4 & \cdots \\
1 & 1   & 1   & 0.8 & \cdots \\
1 & 1   & 1   & 1   & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

$$
M_{t,s}
=
\sum_{\tau=0}^{\min\{t,s\}}
\left(E_{\tau,s} - E_{\tau-1,s}\right)
\cdot M_{t-\tau,s-\tau}
$$

Image note: Orange highlights emphasize the relevant expectations entries in the fourth column, with an arrow pointing to the term $\left(E_{\tau,s} - E_{\tau-1,s}\right)$ in the formula.

## Slide 23: Richer Examples

Richer Examples

## Slide 24: (1) Sticky expectations

- Mankiw Reis (2002), Carroll et al. (2020)

- Each period, households update info with prob. $1-\theta$

$$
E =
\begin{pmatrix}
1 & 1-\theta & 1-\theta & \cdots \\
1 & 1        & 1-\theta^2 & \cdots \\
1 & 1        & 1        & \cdots \\
\vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

$$
M =
\begin{pmatrix}
M_{00} & (1-\theta)M_{01} & (1-\theta)M_{02} & \cdots \\
M_{10} & (1-\theta)M_{11} + \theta M_{00} &
(1-\theta)M_{12} + \theta(1-\theta)M_{01} & \cdots \\
M_{20} & (1-\theta)M_{21} + \theta M_{10} & \vdots & \cdots \\
\vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

## Slide 25: (1) HANK with sticky expectations

- Intermediate $\theta$ generates strong hump shape

- Nice way to replace habit and other slow-adjustment frictions in DSGE models

Image note: Two line charts: “Response to $t=0$ rate cut” and “Response to $t=40$ rate cut.” Axes include “Quarter” and “% of output.” Legend: $\theta=0$, $\theta=0.5$, $\theta=0.8$, $\theta=1$. Intermediate values of $\theta$ generate more hump-shaped responses. Generated by `notebooks/lecture17_info_frictions.ipynb`; figure `lecture17_sticky_exp.pdf`.

## Slide 26: (2) Cognitive discounting

- Gabaix (2020) introduces cognitive discounting

- Idea: Agents respond to shock in $h$ periods as if shock size is dampened by $\theta^h$
  - this is as if agents expect shock size $\theta^h$, instead of 1

$$
E =
\begin{pmatrix}
1 & \theta & \theta^2 & \theta^3 & \cdots \\
1 & 1      & \theta   & \theta^2 & \cdots \\
1 & 1      & 1        & \theta   & \cdots \\
1 & 1      & 1        & 1        & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

- Here, dampening relative to diagonal

- $\neq$ sticky info, where dampening relative to initial period

## Slide 27: (2) HANK with cognitive discounting

- Doesn’t generate humps so well, but dampens forward guidance!

Image note: Two line charts: “Response to $t=0$ rate cut” and “Response to $t=40$ rate cut.” Axes include “Quarter” and “% of output.” Legend: $\theta=1$, $\theta=0.98$, $\theta=0.85$, $\theta=0$. Lower $\theta$ dampens the forward-guidance response. Generated by `notebooks/lecture17_info_frictions.ipynb`; figure `lecture17_cog_disc.pdf`.

## Slide 28: (3) HANK with level $k$

Image note: Two line charts: “Response to $t=0$ rate cut” and “Response to $t=40$ rate cut.” Axes include “Quarter” and “% of output.” Legend: FIRE; $k=4$; $k=3$; $k=2$; $k=1$. Lower levels of $k$ produce weaker and more delayed responses. Generated by `notebooks/lecture17_info_frictions.ipynb`; figure `lecture17_level_k.pdf`.

## Slide 29: (4) HANK with dispersed information

Image note: Two line charts: “Response to $t=0$ rate cut” and “Response to $t=40$ rate cut.” Axes include “Quarter” and “% of output.” Legend: $\tau/\tau_\epsilon=\infty$; $\tau/\tau_\epsilon=5$; $\tau/\tau_\epsilon=0.2$; $\tau/\tau_\epsilon=0$. The curves vary in the degree and timing of response depending on information dispersion. Generated by `notebooks/lecture17_info_frictions.ipynb`; figure `lecture17_dispersed_info.pdf`.

## Slide 30: Takeaway

Takeaway

## Slide 31: Conclusion

- Information rigidities can be nested quite nicely in the sequence space

- Not only gives us a straightforward way of simulating them for RA models,
  - but allows us to apply it to HA models equally well!

## Slide 32: More on level-$k$

More on level-$k$

## Slide 33: (4) Level-$k$ thinking

- Farhi Werning (2019) is first paper to combine HANK with deviations from FIRE

- They use level-$k$ thinking:
  - $k=1$: all agents believe output is at steady state
  - $k=2$: all agents believe all other agents are at level $k=1$
  - $k=3$: all agents believe all other agents are at level $k=2$, … etc

## Slide 34: (4) Level-1 thinking

- Level $k=1$ very close to our myopic example:

$$
M^{(1)} =
\begin{pmatrix}
M_{00} & 0      & 0      & 0      & \cdots \\
M_{10} & M_{00} & 0      & 0      & \cdots \\
M_{20} & M_{10} & M_{00} & 0      & \cdots \\
M_{30} & M_{20} & M_{10} & M_{00} & \cdots \\
\vdots & \vdots & \vdots & \vdots & \ddots
\end{pmatrix}
$$

$$
dY^{(1)} = M^r dr + M^{(1)} \cdot dY^{(1)}
$$

## Slide 35: (4) Level-2 thinking

- What about level-2?

$$
dY^{(2)}
=
M^r dr
+
M \cdot dY^{(1)}
+
M^{(1)} \cdot \left(dY^{(2)} - dY^{(1)}\right)
$$

Everybody expects everyone else to spend money according to level-1!

Hence everyone expects income $= dY^{(1)}$.

… but actual income is $dY^{(2)}$!

Agents are constantly surprised when actual income $dY^{(2)}$ differs from $dY^{(1)}$.

General recursion:

$$
dY^{(k+1)}
=
M^r dr
+
M \cdot dY^{(k)}
+
M^{(1)} \cdot \left(dY^{(k+1)} - dY^{(k)}\right)
$$

## Slide 36: (4) HANK with level $k$

Image note: Two line charts: “Response to $t=0$ rate cut” and “Response to $t=25$ rate cut.” The x-axis is “Quarters.” Legend: FIRE; $k=4$; $k=3$; $k=2$; $k=1$. Lower $k$ values produce smaller responses, especially for the future rate cut. Related to `notebooks/lecture17_info_frictions.ipynb`; closest saved figure is `lecture17_level_k.pdf`, which uses $t=40$ rather than $t=25$.
