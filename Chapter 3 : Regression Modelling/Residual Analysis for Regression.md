### **Residual Analysis for Regression**

**Residual analysis** is a diagnostic tool used to validate the assumptions of regression models, such as linear regression or logistic regression. Residuals are the differences between the **observed values** and the **predicted values** from the model. Analyzing residuals helps you assess whether the model is appropriate and if its assumptions are met.


### **Why Perform Residual Analysis?**
1. **Check Linearity**: Ensure the relationship between predictors and the dependent variable is linear.
2. **Check Homoscedasticity**: Verify that the variance of residuals is constant across all levels of predictors.
3. **Check Normality**: Confirm that residuals are normally distributed.
4. **Detect Outliers**: Identify observations that deviate significantly from the model.
5. **Detect Influential Points**: Find observations that disproportionately influence the model.


### **Types of Residuals**
1. **Raw Residuals**:
   \[
   e_i = Y_i - \hat{Y}_i
   \]
   - \( Y_i \): Observed value.
   - \( \hat{Y}_i \): Predicted value.

2. **Standardized Residuals**:
   \[
   \text{Standardized Residual} = \frac{e_i}{s}
   \]
   - \( s \): Standard deviation of residuals.

3. **Studentized Residuals**:
   - Residuals divided by their standard error, accounting for leverage (useful for detecting outliers).


### **Key Plots for Residual Analysis**

#### **1. Residuals vs. Fitted Values Plot**
- **Purpose**: Check for **linearity** and **homoscedasticity**.
- **What to Look For**:
  - Residuals should be **randomly scattered** around zero.
  - No clear patterns (e.g., curves or funnels).
  - If residuals form a **funnel shape**, heteroscedasticity is present.
  - If residuals show a **curved pattern**, the relationship may be non-linear.

#### **2. Normal Q-Q Plot of Residuals**
- **Purpose**: Check for **normality** of residuals.
- **What to Look For**:
  - Points should lie **close to the 45-degree line**.
  - Deviations at the tails indicate **non-normality**.

#### **3. Histogram of Residuals**
- **Purpose**: Visual check for **normality**.
- **What to Look For**:
  - Residuals should be **symmetrically distributed** around zero.
  - A bell-shaped curve suggests normality.

#### **4. Residuals vs. Predictor Plots**
- **Purpose**: Check for **non-linearity** or **unequal variance** for individual predictors.
- **What to Look For**:
  - Residuals should be **randomly distributed** across all values of the predictor.
  - Patterns suggest the need for **transformation** or **polynomial terms**.

#### **5. Leverage vs. Residuals Plot**
- **Purpose**: Detect **influential points** and **outliers**.
- **What to Look For**:
  - Points with **high leverage** (extreme predictor values) and **large residuals** are influential.
  - Use **Cook’s Distance** to quantify influence.


### **Common Issues and Solutions**

| **Issue**               | **Indication**                          | **Solution**                                  |
|-------------------------|-----------------------------------------|-----------------------------------------------|
| **Non-linearity**       | Residuals form a curved pattern.        | Add polynomial terms or use non-linear models.|
| **Heteroscedasticity**  | Residuals form a funnel shape.          | Transform the dependent variable (e.g., log).|
| **Non-normality**       | Q-Q plot deviates from the line.        | Transform the dependent variable.            |
| **Outliers**            | Points far from zero in residual plots.  | Investigate outliers; consider robust regression.|
| **Influential Points**  | High leverage and large residuals.       | Use Cook’s Distance; consider removing points.|


### **Example: Residual Analysis in Linear Regression**
Suppose you fit a linear regression model to predict **house prices** based on **size** and **age**. After fitting the model, you perform residual analysis:

1. **Residuals vs. Fitted Plot**:
   - Residuals are randomly scattered, but a slight funnel shape suggests **heteroscedasticity**.

2. **Normal Q-Q Plot**:
   - Points lie close to the line, indicating **normality**.

3. **Residuals vs. Size Plot**:
   - Residuals show a curved pattern, suggesting a **non-linear relationship** with size.

**Solution**: Transform the dependent variable (e.g., log(price)) or add a polynomial term for size.


### **Statistical Tests for Residual Analysis**
1. **Shapiro-Wilk Test**: Tests for normality of residuals.
2. **Breusch-Pagan Test**: Tests for heteroscedasticity.
3. **Durbin-Watson Test**: Tests for autocorrelation in residuals (important for time-series data).


### **Tools for Residual Analysis**
- **Python**: Use `statsmodels` or `scikit-learn` to plot residuals.
- **R**: Use `plot(lm_model)` for built-in residual plots.
- **SPSS**: Use the "Save" option to generate residuals and create plots.