Before we get to the formulas, let's understand the core concept.

Imagine the true population parameter (the real average height of all men in a country, or the real click-through rate of a webpage) is a single, stationary fish in a lake. You don't know exactly where it is.

*   You take a sample (you get some data).
*   Based on your sample, you calculate a **confidence interval**. Think of this as building a fishing net of a certain size.
*   You cast your net into the lake.

A **95% confidence interval** has a very specific, and somewhat counter-intuitive, meaning:

> "If we were to repeat our sampling process many times and create a net (an interval) each time, **95% of those nets would capture the true, unknown population parameter (the fish).**"

Notice that we don't say "there is a 95% chance the true value is in *our* interval." In this frequentist view, the true value is fixed. Our interval is what's random; we just happened to cast one net, and we're pretty confident it's one of the 95% that worked.

---

### The Universal Formula

All confidence intervals follow the same basic structure:

**Confidence Interval = (Point Estimate)  ±  (Margin of Error)**

Where:
*   **Point Estimate:** Your best single guess from the sample (e.g., the sample mean or sample proportion).
*   **Margin of Error:** How much you need to add and subtract to create your range of plausible values. It's calculated as: `(Critical Value) × (Standard Error)`

Now let's apply this to our two cases.

---

### Part 1: Confidence Interval for a Mean (μ)

Use this when you are working with continuous data like height, weight, temperature, time, or test scores. Your goal is to estimate the true population mean, **μ**.

**The Point Estimate:** The sample mean, **x̄** (pronounced "x-bar").

**The Formula:**
`CI = x̄  ±  (t* × SE)`
where `SE = s / √n`

**Breaking it down:**
*   **x̄:** The average of your sample.
*   **s:** The standard deviation of your sample. This measures the variability or spread of your data.
*   **n:** Your sample size.
*   **SE (Standard Error):** The standard deviation of the *sampling distribution of the mean*. It represents how much the sample mean would be expected to vary if you took many samples. Notice that as your sample size `n` gets bigger, the SE gets smaller (more data = less error).
*   **t\* (t-critical value):** This value comes from the **t-distribution**. It's determined by two things:
    1.  **Your confidence level** (e.g., 95%). Higher confidence requires a larger t-value (a wider net).
    2.  **Degrees of freedom (df)**, which is `n - 1`.

**Step-by-Step Example:**
You want to estimate the average height of all students at a university. You randomly sample **49 students (n=49)**.
*   The sample mean height **(x̄)** is **172 cm**.
*   The sample standard deviation **(s)** is **14 cm**.

Let's calculate a **95% confidence interval**.

1.  **Calculate the Standard Error (SE):**
    `SE = s / √n = 14 / √49 = 14 / 7 = 2`

2.  **Find the t-critical value (t\*):**
    *   Confidence Level = 95%
    *   Degrees of Freedom (df) = n - 1 = 49 - 1 = 48
    *   Using a t-table or software for df=48 and 95% confidence, we find **t\* ≈ 2.01**.

3.  **Calculate the Margin of Error (MoE):**
    `MoE = t* × SE = 2.01 × 2 = 4.02`

4.  **Construct the Confidence Interval:**
    `CI = x̄ ± MoE = 172 ± 4.02`
    `CI = (167.98, 176.02)`

**Interpretation:** "We are 95% confident that the true average height of all students at the university is between 167.98 cm and 176.02 cm."

---

### Part 2: Confidence Interval for a Proportion (p)

Use this when you are working with categorical, binary data (Yes/No, Success/Failure, Click/No-Click). Your goal is to estimate the true population proportion, **p**.

**The Point Estimate:** The sample proportion, **p̂** (pronounced "p-hat").

**The Formula:**
`CI = p̂  ±  (Z* × SE)`
where `SE = √[ p̂(1-p̂) / n ]`

**Breaking it down:**
*   **p̂:** The proportion of successes in your sample, calculated as `x/n` (number of successes / sample size).
*   **n:** Your sample size.
*   **SE (Standard Error):** The standard deviation of the sampling distribution of the proportion.
*   **Z\* (Z-critical value):** This value comes from the standard normal (Z) distribution. It only depends on the confidence level. For proportions, we generally use Z instead of t, assuming the sample size is large enough.
    *   For 95% confidence, **Z\* = 1.96** (This is a very common number to memorize).
    *   For 99% confidence, **Z\* = 2.576**.

**Step-by-Step Example:**
You run an A/B test on a new website button. You show it to **400 users (n=400)**, and **52 of them click it (x=52)**.

Let's calculate a **95% confidence interval** for the true click-through rate.

1.  **Calculate the Sample Proportion (p̂):**
    `p̂ = x / n = 52 / 400 = 0.13` (or 13%)

2.  **Calculate the Standard Error (SE):**
    `SE = √[ 0.13(1-0.13) / 400 ] = √[ 0.13(0.87) / 400 ] = √[ 0.1131 / 400 ] = √0.00028275 ≈ 0.0168`

3.  **Find the Z-critical value (Z\*):**
    *   For 95% confidence, **Z\* = 1.96**.

4.  **Calculate the Margin of Error (MoE):**
    `MoE = Z* × SE = 1.96 × 0.0168 ≈ 0.0329`

5.  **Construct the Confidence Interval:**
    `CI = p̂ ± MoE = 0.13 ± 0.0329`
    `CI = (0.0971, 0.1629)`

**Interpretation:** "We are 95% confident that the true click-through rate for the new button is between 9.71% and 16.29% for the entire user population."

### Key Factors That Affect the Width of a Confidence Interval

*   **Confidence Level:** Higher confidence (e.g., 99%) requires a larger critical value, resulting in a **wider** interval. (To be more sure, you need a bigger net).
*   **Sample Size (n):** A larger sample size makes the standard error smaller, resulting in a **narrower** interval. (More data gives you more precision).
*   **Data Variability (s or p̂):** Higher variability (a larger `s`) makes the standard error larger, resulting in a **wider** interval. For proportions, variability is highest when p̂ is near 0.5. (If the data points are all over the place, it's harder to pin down the true value).