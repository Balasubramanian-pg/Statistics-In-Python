### **Logistic Regression**

**Logistic Regression** is a statistical method used to model the relationship between a **binary or categorical dependent variable** and one or more **independent variables** (predictors). It estimates the probability of an outcome occurring (e.g., yes/no, success/failure) based on the predictors.


### **When to Use Logistic Regression**
- Your **dependent variable is binary** (e.g., "disease present" or "disease absent").
- You want to **predict probabilities** or classify observations into categories.
- You have **one or more independent variables** (continuous or categorical).


### **Key Concepts**
- **Odds**: The ratio of the probability of an event occurring to it not occurring.
  \[
  \text{Odds} = \frac{P(Y=1)}{1 - P(Y=1)}
  \]
- **Logit**: The natural logarithm of the odds.
  \[
  \text{Logit}(p) = \ln\left(\frac{p}{1-p}\right)
  \]
- **Logistic Regression Model**:
  \[
  \ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k
  \]
  where:
  - \( p \): Probability of the outcome.
  - \( \beta_0 \): Intercept.
  - \( \beta_1, \beta_2, \dots, \beta_k \): Coefficients for predictors \( X_1, X_2, \dots, X_k \).


### **Assumptions**
1. **Binary Outcome**: The dependent variable must be binary (or ordinal for ordinal logistic regression).
2. **No Multicollinearity**: Independent variables should not be highly correlated.
3. **Large Sample Size**: Generally, at least 10-20 observations per predictor.
4. **Linearity of Logit**: The relationship between predictors and the logit of the outcome should be linear.
5. **Independence of Observations**: No repeated measurements or clustered data.


### **Steps to Perform Logistic Regression**
1. **Define the Model**: Specify the dependent and independent variables.
2. **Estimate Coefficients**: Use maximum likelihood estimation (MLE) to fit the model.
3. **Evaluate the Model**:
   - **Likelihood Ratio Test**: Compares the model with and without predictors.
   - **Wald Test**: Tests the significance of individual coefficients.
   - **Hosmer-Lemeshow Test**: Assesses goodness-of-fit.
4. **Interpret Coefficients**:
   - **Odds Ratio (OR)**: \( e^{\beta} \). An OR > 1 increases the odds of the outcome; OR < 1 decreases it.
5. **Predict Probabilities**: Use the model to predict the probability of the outcome for new data.


### **Example**
Suppose you want to predict the probability of a customer **buying a product (Yes/No)** based on their **age** and **income**.

- **Dependent Variable (Y)**: Buy (1 = Yes, 0 = No).
- **Independent Variables (X)**: Age, Income.

The logistic regression equation:
\[
\ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 \text{Age} + \beta_2 \text{Income}
\]

If the model outputs:
- \( \beta_1 = 0.05 \) (Age)
- \( \beta_2 = 0.01 \) (Income)

The **odds ratio** for Age is \( e^{0.05} \approx 1.05 \), meaning a one-unit increase in age increases the odds of buying by 5%.


### **Interpretation**
- **Significant Coefficients**: If the p-value for a coefficient is < 0.05, the predictor is statistically significant.
- **Odds Ratios**:
  - OR = 1: No effect.
  - OR > 1: Increases the odds of the outcome.
  - OR < 1: Decreases the odds of the outcome.


### **Model Evaluation Metrics**
1. **AIC/BIC**: Lower values indicate better model fit.
2. **R-squared (Pseudo R²)**: McFadden’s, Cox & Snell, or Nagelkerke R² (values closer to 1 indicate better fit).
3. **Confusion Matrix**: Accuracy, sensitivity, specificity, precision, and recall.
4. **ROC Curve and AUC**: AUC = 1 indicates perfect classification; AUC = 0.5 indicates no discrimination.


### **Limitations**
- Assumes a **linear relationship** between predictors and the logit of the outcome.
- Can be **sensitive to outliers**.
- Requires **sufficient sample size** for reliable estimates.


### **Extensions**
- **Multinomial Logistic Regression**: For dependent variables with **more than two categories**.
- **Ordinal Logistic Regression**: For **ordered categorical outcomes**.
- **Mixed-Effects Logistic Regression**: For **hierarchical or clustered data**.