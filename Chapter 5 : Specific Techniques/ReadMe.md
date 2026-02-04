## Overview

**Advanced statistics techniques** are methods used to analyze complex datasets, model relationships between multiple variables, and draw more nuanced inferences than basic descriptive or inferential tests allow. They move beyond simple comparisons (like t-tests) and are essential for **prediction**, **classification**, and understanding **causality** in large or high-dimensional data.

The purpose of this documentation is to outline techniques used when data is **non-linear**, has a **complex structure**, or involves **many independent variables**.

## Table of Contents

* **Modeling Relationships and Prediction**
    * **Multiple Regression Analysis**
    * **Logistic Regression**
* **Dimensionality Reduction and Data Structure**
    * **Principal Component Analysis (PCA)**
    * **Factor Analysis (FA)**
* **Modeling Complex Causality**
    * **Structural Equation Modeling (SEM)**
    * **Time Series Analysis (ARIMA)**
* **Application Summary**

## Modeling Relationships and Prediction

These techniques are used when the goal is to predict an outcome or explain a relationship involving multiple predictor variables.

### Multiple Regression Analysis

This is an extension of simple linear regression. It is used to determine the relationship between **one dependent variable** and **two or more independent variables**.

* **Simple Definition:** It finds the best-fitting line or hyperplane that minimizes the sum of squared errors between the predicted and actual values.
* **Real Life Example:** Predicting a house's **sale price** (dependent variable) based on its **square footage**, the **number of bedrooms**, and its **distance to the city center** (independent variables).
* **What You Must Understand:** Each independent variable gets a unique **coefficient**, which represents the change in the dependent variable for a one-unit change in that predictor, *while holding all other predictors constant*. This allows you to assess the unique contribution of each factor.

### Logistic Regression

This technique is used when the dependent variable is **binary** (dichotomous), meaning it has only two outcomes (e.g., Yes/No, Pass/Fail, 0/1). 

[Image of Logistic Regression Sigmoid Curve]


* **Simple Definition:** It models the probability of a certain event occurring by fitting data to a **sigmoid (S-shaped) curve**, transforming the linear relationship into a probability.
* **Real Life Example:** Predicting whether a customer will **click** (1) or **not click** (0) on an advertisement based on their age and income.
* **What You Must Understand:** Instead of predicting the actual outcome (like price), it predicts the **log odds** of the outcome. The result is then converted into a probability between 0 and 1.

[!INFO]
Logistic Regression is core for all basic **classification** problems, especially in machine learning. It is an extension of the **Generalized Linear Model (GLM)** family.

## Dimensionality Reduction and Data Structure

These methods are used to simplify complex datasets by finding underlying structures or reducing the number of variables while preserving most of the original information.

### Principal Component Analysis (PCA)

PCA is a technique used to reduce the **dimensionality** of a dataset with many variables while retaining as much variance as possible.

* **Simple Definition:** It transforms the original set of variables into a smaller set of **uncorrelated variables** called **Principal Components (PCs)**.
* **Real Life Example:** A large survey has 50 questions asking about consumer satisfaction. PCA can combine the variance across those 50 questions into perhaps 3 or 4 **underlying factors** (e.g., "Product Quality," "Customer Service," "Value") that explain most of the variation.
* **Application:** The first principal component (PC1) captures the most variance in the data, PC2 captures the next most, and so on. You select only the top PCs to use in further analysis.

[!TIP]
PCA is often used as a **preprocessing step** before running a regression or clustering model to improve performance and reduce noise.

### Factor Analysis (FA)

FA is used to identify the **unobserved variables** (factors) that explain the pattern of correlations among a set of observed variables.

* **Simple Definition:** It is a method for grouping together measured variables that are highly correlated with each other, suggesting they all measure the same underlying construct.
* **Real Life Example:** In psychology, different test questions (observed variables) on an IQ test are used to measure an underlying **Intelligence** (the unobserved factor).
* **Application:** Unlike PCA which focuses on maximizing variance, FA focuses on explaining the correlation structure. It is heavily used in developing reliable surveys and scales.

## Modeling Complex Causality

These techniques are necessary for time-dependent data or models that attempt to show complex, directed relationships between latent and observed variables.

### Structural Equation Modeling (SEM)

SEM is a powerful multivariate technique that allows researchers to test complex theoretical models by examining relationships between observed (measured) variables and latent (unobserved) variables.

* **Simple Definition:** It combines **Factor Analysis** and **Multiple Regression** into one comprehensive framework, allowing you to test entire systems of hypotheses simultaneously.
* **Real Life Example:** Modeling how **Job Satisfaction** (a latent variable measured by several survey questions) affects **Organizational Commitment** (another latent variable), which in turn predicts **Employee Turnover** (an observed variable).
* **Application:** SEM provides various **fit indices** to determine how well the proposed theoretical model matches the actual sample data.

### Time Series Analysis (ARIMA)

**Time Series Analysis** is a specialized area for analyzing data points collected over a period of time. **ARIMA** (AutoRegressive Integrated Moving Average) is a common model within this domain.

* **Simple Definition:** ARIMA models use past observations to predict future values. It handles trends, seasonality, and irregular fluctuations in sequential data.
* **Real Life Example:** Forecasting the stock price of a company, the monthly electricity consumption of a city, or the weekly sales of a product.
* **Sub-parts of ARIMA:**
    * **AR (AutoRegressive):** Uses the relationship between the current observation and a number of lagged (past) observations.
    * **I (Integrated):** Uses differencing of the raw observations to make the time series stationary (meaning its statistical properties don't change over time).
    * **MA (Moving Average):** Uses the dependency between an observation and a residual error from a moving average model applied to lagged observations.

[!DANGER]
In Time Series Analysis, assuming independence is a major mistake. The observations are inherently dependent on previous values.


## Application Summary

To choose the correct advanced technique, assess your data and goal:

1.  **Prediction Goal:** If you are predicting a **continuous outcome** with multiple variables, use **Multiple Regression**. If you are predicting a **binary outcome**, use **Logistic Regression**.
2.  **Simplification Goal:** If you have too many variables and need to reduce them to underlying, uncorrelated components, use **PCA** or **Factor Analysis**.
3.  **Complex Modeling Goal:** If you are testing a complex theory with latent variables and directed paths, use **SEM**. If your data is sequential and you need to forecast, use **Time Series Analysis (ARIMA)**.

**Simple Real World Use Scenario (PCA in Python):**

A bank has 20 financial metrics for each loan applicant. They need a simpler risk score.

**Action Plan:**

1.  Standardize the 20 variables.
2.  Run a **PCA** on the standardized data.
3.  Examine the output to see that the first **three principal components** explain 85% of the total variance.
4.  **Conclusion:** Use these three principal components, which now act as a composite "risk score," instead of all 20 original metrics for the downstream loan default prediction model.