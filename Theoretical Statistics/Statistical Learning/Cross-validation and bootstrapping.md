Cross-validation and bootstrapping are both techniques often used in machine learning and statistics to estimate model performance and uncertainty.

### Cross-Validation

Cross-validation involves partitioning the dataset into subsets, training the model on some subsets (training data), and validating it on the remaining subsets (validation or test data). The most common form is k-fold cross-validation, where the dataset is divided into k equal parts, and the model is trained and validated k times, using each of the k parts as the validation set exactly once.

#### Advantages of Cross-Validation:

- More reliable than a single train-test split as it uses most of the data for training and validation.
- Reduces variance and helps in detecting overfitting.

#### Types of Cross-Validation:

- k-Fold Cross-Validation (most common)
- Stratified k-Fold (preserves class distribution in each fold)
- Leave-One-Out Cross-Validation (LOOCV) (where k equals the number of observations)

### Bootstrapping

Bootstrapping involves repeatedly sampling from the dataset with replacement and refitting the model each time. This allows for an estimation of the distribution of a statistic (e.g., mean, variance) or model performance metric.

#### Advantages of Bootstrapping:

- Can be used to estimate the distribution of almost any statistic.
- Helps in understanding the variability of the statistic.
- Useful when sample sizes are small.

#### Types of Bootstrapping:

- Basic Bootstrap
- Percentile Bootstrap
- Bootstrap Confidence Intervals (BCa, etc.)

### When to Use Each Technique

- **Cross-Validation**: When you need an estimate of model performance (e.g., prediction error).
- **Bootstrapping**: When you need to estimate the uncertainty or distribution of a statistic.

Both techniques are useful in their own right and are often used complementarily in practice. For instance, bootstrapping can be used to estimate confidence intervals for the performance metrics obtained through cross-validation.