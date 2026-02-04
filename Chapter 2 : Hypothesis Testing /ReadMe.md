This content summarizes common statistical hypothesis tests.

### One-Sample T-Test

This test determines if the mean of a single **sample** is different from a specific **hypothesized value** or a known population mean.

* **Goal:** Compare one group mean to a standard.
* **Data Type:** The variable must be **continuous** (interval or ratio).
* **Use Case:** Assessing if a new production batch's average weight meets the 100-gram target.

### Independent Samples T-Test

Also known as the Two-Sample T-Test, this procedure compares the means of two **unrelated** groups to see if a significant difference exists between their population means.

* **Goal:** Compare means of two distinct groups.
* **Key Feature:** Groups are separate; the data from one group does not influence the other (e.g., Men vs. Women).
* **Use Case:** Testing if two different teaching methods result in different average test scores.

### Paired Samples T-Test

This test compares the means of two sets of observations that are **related** or dependent. It often involves measuring the same subjects under two different conditions or at two time points.

* **Goal:** Compare the mean **difference** between paired observations (e.g., before and after).
* **Key Feature:** Each data point in one set is directly linked to a data point in the second set.
* **Use Case:** Evaluating a drug's effectiveness by comparing patient blood pressure before treatment and after treatment.

### Analysis of Variance (ANOVA)

ANOVA is a test used to compare the means of **three or more** independent groups. It determines if at least one group mean is different from the others.

* **Goal:** Check if means from multiple groups are equal.
* **Output:** Provides an overall **F-statistic** to show if any difference exists. It does not indicate which specific pairs differ.
* **Use Case:** Comparing the average crop yield resulting from three distinct fertilizer types.

### Post-Hoc Tests (e.g., Tukey's HSD)

These tests are typically run **after** a significant ANOVA result. Their **purpose** is to conduct pairwise comparisons among all groups while controlling the **Type I error rate** (false positive).

* **Tukey's HSD (Honest Significant Difference):** A common post-hoc test.
* **Goal:** Identify **which specific pairs** of group means are significantly different from each other.
* **Process:** Compares all possible mean pairs based on the overall ANOVA result.

### Chi-Squared Test for Independence

This is a **nonparametric** test used to determine if there is a relationship (association) between **two categorical variables**.

* **Goal:** Check if two categorical variables are independent.
* **Data Type:** Uses **counts** or frequencies in a contingency table.
* **Use Case:** Testing if there is a relationship between a person's preferred soft drink (Coke, Pepsi, Sprite) and their geographic region (North, South, West).

### Proportion Z-Test (One and Two Sample)

This test assesses hypotheses about population **proportions** (percentages) rather than means.

* **One Sample:** Compares a sample proportion to a single hypothesized population proportion.
    * **Goal:** Determine if the proportion of successes in a sample differs from a target percentage.
    * **Use Case:** Testing if the 80% success rate claimed by a company is accurate based on a sample.
* **Two Sample:** Compares the proportions of two independent groups.
    * **Goal:** Determine if the proportions of successes in two different populations are equal.
    * **Use Case:** Testing if the defect rate of assembly line A is the same as the defect rate of assembly line B.