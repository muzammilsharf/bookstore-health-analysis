# Bookstore Health Analysis: Findings

Prepared for the owner of a three-store Calgary bookstore. The data covers
2019 to 2024 and is a synthetic dataset (see the README).

## Summary

- Revenue recovered after COVID to its pre-pandemic level, but not beyond it.
  After inflation it is likely still below.
- YYC-DT is the strongest store by a wide margin. All three stores sell about
  20% online, so the gap between stores comes from the physical locations.
- The checking account lost money every quarter, but it only sees a fraction
  of sales and payroll, so it cannot show whether the business is unprofitable.
- Debt taken on in 2020 was never paid down and peaked at about $132K. That is
  small next to the checking deficit, so it is not what keeps the account running.

## 1. Did revenue recover after COVID?

Average quarterly revenue was about $571K before COVID, $452K during it, and
$611K after. A Kruskal-Wallis test shows the periods differ (p = 0.017). A
post-hoc Dunn test (Bonferroni-corrected) shows the rise from during-COVID to
post-COVID is real (p = 0.013), but post-COVID is not distinguishable from
pre-COVID (p = 1.00).

The recovery is real, but it is a return to baseline, not growth past it. All
figures are nominal. The dataset applies an inflation factor from 1.00 in 2019
to 1.18 in 2024, so 2024 revenue is about 5% above 2019 nominally and roughly
11% below it in real terms.

## 2. Which stores and channels drive revenue?

Median monthly revenue is roughly $85K at YYC-DT, $60K at YYC-NW and $51K at
YYC-SE. The stores differ significantly (Kruskal-Wallis p < 0.001), and every
pair differs in the post-hoc test, including NW vs SE (p = 0.0007).

Online sales are 20.5% of revenue at DT, 20.4% at NW and 20.2% at SE. The mix
is essentially identical, so DT's lead comes from its location doing more
business, not from online. For an expansion decision, a new store's results
will likely depend more on the location than on its online presence.

## 3. Is cash flow healthy, or propped up by debt?

The checking account went from a $75K opening balance to about -$1.94M, losing
roughly $84K a quarter, with no visible COVID effect. Deposits covered about
61% of withdrawals.

This does not mean the business lost $2M. The account sees only about 23% of
sales (sales sweeps) and pays about 29% of the payroll file's totals, so it
looks like a partial view on its own scale. I did not treat it as proof that
the business is unprofitable.

Loans were near zero in 2019, jumped to about $55K in 2020Q1, and never came
back down, peaking at about $132K in 2024Q3. Interest grew to about $2K a
quarter. Peak debt is about 15 times smaller than the account's deficit and no
loan proceeds appear in checking deposits, so debt is not what keeps the
account running. What is worth flagging is that the 2020 borrowing was never
paid down.

## 4. Payroll vs revenue

[FILL IN two sentences from your payroll notebook, or delete this section and
list it under "Not covered".]

## Limitations

- Checking could not be reconciled with sales or payroll, and the inventory
  file was not used.
- All figures are nominal dollars.
- The dataset is synthetic, so patterns reflect how it was generated.

## Not covered

Customer ratings vs spend and the cleaning of the raw customer file.