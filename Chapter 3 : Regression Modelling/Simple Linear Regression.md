### **Simple Linear Regression**

**Simple Linear Regression** is a statistical method used to model the relationship between a **single independent variable (X)** and a **dependent variable (Y)**. It helps you understand how changes in \( X \) are associated with changes in \( Y \), and it allows you to predict \( Y \) for new values of \( X \).


### **When to Use Simple Linear Regression**
- You want to **explore the relationship** between two continuous variables.
- You want to **predict** the value of \( Y \) based on \( X \).
- You suspect a **linear relationship** between \( X \) and \( Y \).


### **Key Concepts**
#### **Regression Equation**
\[
Y = \beta_0 + \beta_1 X + \epsilon
\]
- \( Y \): Dependent variable.
- \( X \): Independent variable.
- \( \beta_0 \): Intercept (value of \( Y \) when \( X = 0 \)).
- \( \beta_1 \): Slope (change in \( Y \) for a one-unit change in \( X \)).
- \( \epsilon \): Error term (residuals, representing unexplained variation).


### **Assumptions**
1. **Linearity**: The relationship between \( X \) and \( Y \) is linear.
2. **Independence**: Observations are independent of each other.
3. **Homoscedasticity**: The variance of residuals is constant across all values of \( X \).
4. **Normality**: Residuals are normally distributed.
5. **No Outliers**: Outliers can disproportionately influence the regression line.


### **Steps to Perform Simple Linear Regression**
1. **Define the Model**: Specify \( Y \) (dependent variable) and \( X \) (independent variable).
2. **Estimate Coefficients**: Use the **least squares method** to find \( \beta_0 \) and \( \beta_1 \):
   \[
   \beta_1 = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2}
   \]
   \[
   \beta_0 = \bar{Y} - \beta_1 \bar{X}
   \]
3. **Evaluate the Model**:
   - **Coefficient of Determination (\( R^2 \))**: Measures the proportion of variance in \( Y \) explained by \( X \) (ranges from 0 to 1).
   - **t-test for Slope**: Tests if \( \beta_1 \) is significantly different from zero.
   - **F-test**: Tests the overall significance of the model.
4. **Check Assumptions**: Use residual analysis to validate linearity, homoscedasticity, and normality.
5. **Interpret Coefficients**:
   - \( \beta_1 \): A one-unit increase in \( X \) is associated with a \( \beta_1 \)-unit change in \( Y \).
   - \( \beta_0 \): The expected value of \( Y \) when \( X = 0 \).


### **Example**
Suppose you want to predict **house prices (Y)** based on **house size (X)**. You collect the following data:

| Size (sq. ft) | Price ($1000s) |
|---------------|----------------|
| 1500          | 200            |
| 2000          | 250            |
| 2500          | 300            |
| 3000          | 350            |

- **Regression Equation**:
  \[
  \text{Price} = \beta_0 + \beta_1 \times \text{Size}
  \]
- Suppose the model outputs:
  \[
  \text{Price} = 50 + 0.1 \times \text{Size}
  \]
  - **Interpretation**: For every additional square foot, the price increases by **$100** (holding other factors constant).
  - **Intercept**: A house with 0 sq. ft would cost **$50,000** (often not meaningful in practice).


### **Model Evaluation Metrics**
1. **\( R^2 \)**: Explains the proportion of variance in \( Y \) accounted for by \( X \).
   - \( R^2 = 0.8 \) means 80% of the variability in \( Y \) is explained by \( X \).
2. **Standard Error of the Estimate (SEE)**: Measures the accuracy of predictions.
3. **p-value for Slope**: If \( p < 0.05 \), the slope is statistically significant.


### **Limitations**
- **Assumes Linearity**: If the relationship is non-linear, the model may not fit well.
- **Sensitive to Outliers**: Outliers can distort the regression line.
- **Only One Predictor**: Cannot account for the influence of other variables (use **multiple regression** for multiple predictors).


### **Extensions**
- **Polynomial Regression**: For non-linear relationships.
- **Multiple Linear Regression**: For multiple predictors.
- **Residual Analysis**: To validate model assumptions.