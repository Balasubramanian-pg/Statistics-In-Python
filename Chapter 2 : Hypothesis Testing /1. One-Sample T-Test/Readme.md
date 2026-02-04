A **one-sample t-test** is a statistical test used to determine whether the mean of a single sample significantly differs from a known or hypothesized population mean. It’s commonly used when you want to compare your sample data to a standard or a theoretical value.
## When the One-Sample t-Test Is the Right Tool

Use it when:

- You have one group
- You are comparing against a fixed benchmark
- Variability must be estimated from the sample

Examples:

- Average delivery time vs SLA
- Average exam score vs passing cutoff
- Average sensor reading vs calibration value

Do not use it when comparing two groups. That is a different test with a different error structure.

## Common Misuses and Traps

- Testing after peeking at the data repeatedly
- Using one-sided tests without justification
- Ignoring effect size
- Treating non-significance as proof of equality

Absence of evidence is not evidence of absence.

## Summary Mental Model

The one-sample t-test is not a magical significance button.

It is a disciplined way to ask:

> “Given the noise I observe, is this difference too large to ignore?”

It forces you to confront uncertainty instead of hand-waving it away.

## Points That Require Care or Are Context-Dependent

- Normality requirements depend on sample size
- Effect size thresholds vary by domain
- One-sided tests require pre-registered logic

These are methodological choices, not universal constants.

## **Example**
Suppose you want to test if the average height of a sample of 25 students is different from the national average of 170 cm.

- Sample mean (\(\bar{X}\)) = 172 cm
- Sample standard deviation (\(s\)) = 5 cm
- Population mean (\(\mu_0\)) = 170 cm
- \(n = 25\)

\[
t = \frac{172 - 170}{5 / \sqrt{25}} = \frac{2}{1} = 2
\]

Compare this t-value to the critical value (for \(df = 24\) and \(\alpha = 0.05\), two-tailed) or find the p-value.

## **Interpretation**
- If the p-value is **less than 0.05**, you conclude that the sample mean is significantly different from the population mean.
- If the p-value is **greater than 0.05**, you do not have enough evidence to reject the null hypothesis.

## **Limitations**
- Sensitive to outliers.
- Assumes normality, especially for small samples.