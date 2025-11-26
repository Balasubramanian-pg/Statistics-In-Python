## Overview

**Non-parametric tests** are statistical methods that do not rely on assumptions about the underlying **distribution** of the data. They are often used when data is **not normally distributed** or when working with **ordinal** (ranked) or **nominal** (categorical) data. These tests help determine if there is a significant difference or relationship between groups or variables without assuming a specific shape for the population. They are a practical alternative to **parametric tests** like the t-test or ANOVA when those tests' assumptions are violated.

The main problem they solve is providing a **valid statistical conclusion** even when the requirements for traditional tests, such as a normal distribution, cannot be met.

---

## Table of Contents

* **Understanding Parametric vs. Non-parametric Tests**
* **Key Non-parametric Tests**
    * **Mann-Whitney U Test (Two Independent Samples)**
    * **Kruskal-Wallis H Test (Three or More Independent Samples)**
    * **Wilcoxon Signed-Rank Test (Two Dependent/Paired Samples)**
    * **Friedman Test (Three or More Dependent/Paired Samples)**
* **The Python Ecosystem (SciPy)**
* **Application Summary**

---

## Understanding Parametric vs. Non-parametric Tests

A **parametric test** requires your data to meet certain conditions, primarily that the data comes from a specific distribution (like the **normal distribution**) and that the variances of the groups are roughly equal. A **non-parametric test** makes few or no assumptions about the data's distribution.

[!INFO]
This distinction is core. If your data fails a normality test (like Shapiro-Wilk) and you cannot transform it, you **must** use a non-parametric test to ensure valid results.

**Real Life Example:**
Imagine you are comparing the income of two groups. If the income data has a few extremely high earners (skewing the data), the distribution will not be normal. A parametric t-test would be inaccurate. A **non-parametric test** would be appropriate because it works with the **ranks** of the data points, not the raw values, making it less sensitive to outliers.

**What You Must Understand:**
The core idea is **robustness**. Non-parametric tests are more robust against violations of distributional assumptions. Their primary mechanism is often using **ranks** instead of the original raw scores.

---

## Key Non-parametric Tests

This section covers the essential tests, focusing on their purpose and equivalent parametric test.

### Mann-Whitney U Test (Two Independent Samples)

This test assesses whether two **independent samples** come from the same distribution. It is the non-parametric equivalent of the **Independent Samples t-test**.

* **Simple Definition:** It checks if the values in one group are significantly higher (or lower) than the values in another group.
* **Real Life Example:** Comparing the test scores of students from **Class A** and **Class B** after an intervention, where the scores are heavily skewed and not normally distributed.
* **Application:** You calculate a **U statistic** based on how the data points from one group rank relative to the data points in the other group.

### Kruskal-Wallis H Test (Three or More Independent Samples)

This test checks if there are statistically significant differences between three or more **independent groups**. It is the non-parametric equivalent of the **One-Way ANOVA**.

* **Simple Definition:** It tests the null hypothesis that all groups have the same median.
* **Real Life Example:** Comparing the customer satisfaction ratings (on a scale of 1 to 10) of three different coffee shops, where the distribution of ratings is non-normal.
* **Application:** If the test is significant, you must then perform **post-hoc tests** (like Dunn's test) to find out *which specific pairs* of groups are different.

### Wilcoxon Signed-Rank Test (Two Dependent/Paired Samples)

This test compares two related or paired samples. It is the non-parametric equivalent of the **Paired Samples t-test**.

* **Simple Definition:** It assesses if the differences between paired observations (before and after) are centered around zero.
* **Real Life Example:** Measuring the anxiety score of a group of patients **before** and **after** a new therapy, where the score change is not normally distributed.
* **Application:** It works by calculating the differences between the pairs, ranking the absolute differences, and then summing the ranks based on the sign of the difference.

### Friedman Test (Three or More Dependent/Paired Samples)

This test is used to detect differences in treatments across multiple test occasions or conditions when the same subjects are used in each condition. It is the non-parametric equivalent of the **Repeated Measures ANOVA**.

* **Simple Definition:** It compares the values of three or more conditions for the same group of subjects.
* **Real Life Example:** Having a group of ten users rate three different website layouts (Layout A, B, and C) on a non-normal usability score.
* **Application:** The test ranks the data for each subject separately across the different conditions, then analyzes the sum of the ranks for each condition.

---

## The Python Ecosystem (SciPy)

In Python, the **SciPy** library's `scipy.stats` module is the primary tool for performing non-parametric tests.

[!NOTE]
The functions are usually named after the test, making them easy to find. You will primarily use the function to get a **test statistic** and a **p-value**.

**Key Functions in `scipy.stats`:**

* **`mannwhitneyu(x, y)`:** For the Mann-Whitney U Test.
* **`kruskal(group1, group2, group3, ...)`:** For the Kruskal-Wallis H Test.
* **`wilcoxon(x, y)`:** For the Wilcoxon Signed-Rank Test.
* **`friedmanchisquare(condition1, condition2, condition3, ...)`:** For the Friedman Test.

[!TIP]
For the Kruskal-Wallis and Friedman tests, SciPy gives you the overall test result. You will often need to use a separate library (like `scikit-posthocs`) for the **post-hoc analysis** to pinpoint where the differences lie.

---

## Application Summary

To use non-parametric tests effectively, remember these three points:

1.  **Check Assumptions First:** Always test for **normality** (e.g., Shapiro-Wilk) before deciding on a test. If it fails, go non-parametric.
2.  **Know Your Data Structure:**
    * **Independent Groups:** Use **Mann-Whitney U** (2 groups) or **Kruskal-Wallis H** (3+ groups).
    * **Paired/Dependent Groups:** Use **Wilcoxon Signed-Rank** (2 conditions) or **Friedman** (3+ conditions).
3.  **Interpret the P-value:** If the calculated **p-value** is less than your significance level (usually $0.05$), you **reject the null hypothesis**, meaning there is a statistically significant difference between the groups.

**Simple Real World Use Scenario (Mann-Whitney U in Python):**

A hospital wants to see if a new drug (Group B) causes a lower white blood cell count than the old drug (Group A). The cell count data is highly skewed.

**Action Plan:**

1.  Gather data for **Group A** and **Group B** (the two independent samples).
2.  Import `mannwhitneyu` from `scipy.stats`.
3.  Run the test: `statistic, p_value = mannwhitneyu(group_A_data, group_B_data)`.
4.  **Conclusion:** If $p\_value < 0.05$, the ranks of the white blood cell counts are significantly different between the two drug groups.
