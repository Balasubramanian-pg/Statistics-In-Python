## Simple Linear Regression

Simple Linear Regression (SLR) is a statistical method used to model the linear relationship between two continuous variables.

* **Goal:** Predict a **continuous dependent variable** ($Y$) using a single **continuous independent variable** ($X$).
* **Model:** Finds the "line of best fit" that minimizes the sum of squared errors between the observed data and the line.
* **Output:** Provides a linear equation ($Y = \beta_0 + \beta_1X$) that describes the relationship's direction and strength.
* **Use Case:** Predicting a student's final exam score based on their hours spent studying.

## Multiple Linear Regression

Multiple Linear Regression (MLR) extends SLR by incorporating two or more independent variables to predict a single continuous dependent variable.

* **Goal:** Predict a **continuous dependent variable** ($Y$) using **two or more independent variables** ($X_1, X_2, ...$).
* **Key Feature:** Allows for controlling the influence of multiple factors simultaneously to isolate the effect of each predictor.
* **Assumptions:** Requires the relationship to be linear, residuals to be normally distributed and exhibit homoscedasticity (constant variance), and low multicollinearity among predictors.
* **Use Case:** Predicting house price based on square footage, number of bedrooms, and distance to the city center.

## Logistic Regression

Logistic Regression is a regression technique used for classification problems where the outcome variable is categorical.

* **Goal:** Predict the **probability** of a categorical outcome, typically a **binary outcome** (e.g., 0 or 1, Yes or No).
* **Method:** Uses the **logistic function** (or sigmoid function) to transform the linear combination of predictors into a probability value between 0 and 1.
* **Output:** The result is an estimated probability of the event occurring, which is then classified into one of the categories.
* **Use Case:** Predicting whether a loan applicant will default (Yes/No) based on credit score, income, and debt history.

## Residual Analysis for Regression

Residual analysis is a diagnostic technique essential for validating the assumptions of a linear regression model.

* **Definition of Residuals:** The **residual** is the difference between the **observed value** and the value **predicted by the model** ($Observed - Predicted$).
* **Goal:** Check if the model's core assumptions are satisfied. 
* **Key Checks:**
    * **Linearity:** The residual plot should show a **random scatter** around the horizontal axis, indicating the linear model is appropriate.
    * **Homoscedasticity (Constant Variance):** The spread of the residuals should be uniform across all predicted values, avoiding a funnel or cone shape.
    * **Normality:** The residuals should be approximately normally distributed.
    * **Outliers:** Helps identify data points that do not follow the general pattern and may disproportionately affect the model.

***

To learn how to diagnose potential problems with your regression model, you can review this video on [Residual Analysis](https://www.youtube.com/watch?v=_IlAuhLPi30).


http://googleusercontent.com/youtube_content/0
