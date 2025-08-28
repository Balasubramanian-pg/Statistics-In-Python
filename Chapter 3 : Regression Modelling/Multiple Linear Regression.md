### **Multiple Linear Regression**

**Multiple Linear Regression** is a statistical technique used to model the relationship between a **dependent variable (Y)** and **two or more independent variables (X₁, X₂, ..., Xₖ)**. It extends simple linear regression by incorporating multiple predictors to explain the variability in the dependent variable.

---

### **When to Use Multiple Linear Regression**
- You want to **predict or explain** a continuous dependent variable using multiple predictors.
- You suspect that **multiple factors** influence the outcome (e.g., predicting house prices based on size, location, and age).
- You want to **quantify the relationship** between each predictor and the dependent variable while controlling for other predictors.

---

### **Key Concepts**
#### **Regression Equation**
\[
Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k + \epsilon
\]
- \( Y \): Dependent variable.
- \( X_1, X_2, \dots, X_k \): Independent variables.
- \( \beta_0 \): Intercept (value of \( Y \) when all \( X \) are zero).
- \( \beta_1, \beta_2, \dots, \beta_k \): Coefficients (change in \( Y \) per unit change in \( X \)).
- \( \epsilon \): Error term (residuals).

---

### **Assumptions**
1. **Linearity**: The relationship between predictors and the dependent variable is linear.
2. **Independence**: Observations are independent (no autocorrelation).
3. **Homoscedasticity**: Residuals have constant variance across all levels of predictors.
4. **Normality**: Residuals are normally distributed.
5. **No Multicollinearity**: Predictors are not highly correlated with each other.

---

### **Steps to Perform Multiple Linear Regression**
1. **Define the Model**: Specify the dependent and independent variables.
2. **Estimate Coefficients**: Use the **least squares method** to minimize the sum of squared residuals.
3. **Evaluate the Model**:
   - **Coefficient of Determination (\( R^2 \))**: Proportion of variance in \( Y \) explained by the predictors (0 to 1).
   - **Adjusted \( R^2 \)**: Adjusts \( R^2 \) for the number of predictors.
   - **F-test**: Tests if the model is significant (null hypothesis: all coefficients are zero).
   - **t-tests**: Tests the significance of individual coefficients.
4. **Check Assumptions**:
   - Plot residuals to check for linearity, homoscedasticity, and normality.
   - Use **Variance Inflation Factor (VIF)** to check for multicollinearity (VIF > 10 indicates multicollinearity).
5. **Interpret Coefficients**:
   - A coefficient \( \beta_i \) represents the change in \( Y \) for a one-unit change in \( X_i \), holding other predictors constant.

---

### **Example**
Suppose you want to predict **house prices (Y)** based on:
- **Size (X₁)** in square feet.
- **Number of bedrooms (X₂)**.
- **Age of the house (X₃)** in years.

The regression equation might look like:
\[
\text{Price} = 50000 + 150 \times \text{Size} + 10000 \times \text{Bedrooms} - 2000 \times \text{Age}
\]
- **Interpretation**:
  - For every additional square foot, the price increases by **$150**, holding bedrooms and age constant.
  - Each additional bedroom increases the price by **$10,000**, holding size and age constant.
  - For every additional year of age, the price decreases by **$2,000**, holding size and bedrooms constant.

---

### **Model Evaluation Metrics**
1. **\( R^2 \)**: Explains the proportion of variance in \( Y \) accounted for by the model.
2. **Adjusted \( R^2 \)**: Penalizes adding non-contributing predictors.
3. **F-statistic**: Tests the overall significance of the model.
4. **p-values for Coefficients**: Indicate if individual predictors are significant.
5. **Residual Analysis**: Check for patterns in residuals to validate assumptions.

---

### **Limitations**
- **Overfitting**: Including too many predictors can lead to a model that fits the training data well but generalizes poorly.
- **Multicollinearity**: Highly correlated predictors can inflate the variance of coefficient estimates.
- **Outliers**: Can disproportionately influence the regression line.

---

### **Extensions**
- **Polynomial Regression**: For non-linear relationships.
- **Interaction Terms**: To model the effect of one predictor depending on the value of another.
- **Stepwise Regression**: Automatically selects predictors based on statistical criteria.
