A **one-sample t-test** is a statistical test used to determine whether the mean of a single sample significantly differs from a known or hypothesized population mean. It’s commonly used when you want to compare your sample data to a standard or a theoretical value.

---

## **When to Use a One-Sample T-Test**
- You have **one continuous variable** (e.g., test scores, reaction times, weights).
- You want to compare the **sample mean** to a **known or hypothesized population mean** (e.g., comparing the average score of a class to a national average).
- Your data is **normally distributed** or your sample size is large enough (typically n > 30) for the Central Limit Theorem to apply.

---

## **Key Assumptions**
1. **Normality**: The data should be approximately normally distributed. For small samples (n < 30), check normality using a Shapiro-Wilk test or Q-Q plots.
2. **Independence**: Observations should be independent of each other.
3. **Continuous Data**: The variable should be measured on an interval or ratio scale.

---

## **Hypotheses**
- **Null Hypothesis (H₀)**: The sample mean is equal to the population mean.
  \( H_0: \mu = \mu_0 \)
- **Alternative Hypothesis (H₁)**: The sample mean is not equal to (or greater/less than) the population mean.
  \( H_1: \mu \neq \mu_0 \) (two-tailed)
  \( H_1: \mu > \mu_0 \) (one-tailed, right)
  \( H_1: \mu < \mu_0 \) (one-tailed, left)

---

## **Steps to Perform a One-Sample T-Test**
1. **State your hypotheses** (null and alternative).
2. **Set the significance level (α)**, usually 0.05.
3. **Calculate the t-statistic**:
   \[
   t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}
   \]
   - \(\bar{X}\): Sample mean
   - \(\mu_0\): Population mean
   - \(s\): Sample standard deviation
   - \(n\): Sample size
4. **Determine the critical t-value** from the t-distribution table (based on degrees of freedom: \(df = n - 1\)).
5. **Compare the t-statistic to the critical value** or calculate the p-value.
6. **Make a decision**:
   - If \(p \leq \alpha\), reject the null hypothesis.
   - If \(p > \alpha\), fail to reject the null hypothesis.

---

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

---

## **Interpretation**
- If the p-value is **less than 0.05**, you conclude that the sample mean is significantly different from the population mean.
- If the p-value is **greater than 0.05**, you do not have enough evidence to reject the null hypothesis.

---

## **Limitations**
- Sensitive to outliers.
- Assumes normality, especially for small samples.

---

Would you like help with a specific dataset or calculating a one-sample t-test? Or do you want to explore how to do this in software like Python, R, or SPSS?
