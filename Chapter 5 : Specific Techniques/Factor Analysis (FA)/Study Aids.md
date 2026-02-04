## Factor Analysis (FA) - Extended Notes and Study Aids

These notes are meant to sit next to your original explanation as a deeper, more operational layer. Think of this as the stuff you wish textbooks said out loud instead of hiding in footnotes.

## 1. The Statistical Model Behind Factor Analysis

At its core, factor analysis assumes a **generative model**.

Each observed variable is produced by a combination of:

• One or more latent factors
• Variable specific noise or uniqueness

Formally, the model is:

Observed Variable = (Factor Loadings × Factors) + Error

Key implications:

• Correlation exists because variables share common factors
• Not all variance is useful. Some variance is just noise
• FA explicitly separates shared variance from unique variance

This is the philosophical difference from PCA, which never asks *why* variables move together.

## 2. Variance Decomposition

Every observed variable’s variance is split into two parts.

### Communality

• Portion of variance explained by the common factors
• High communality means the variable fits the factor model well
• Low communality suggests the variable may not belong in the analysis

Rule of thumb:
• Communality < 0.3 is often considered weak

### Uniqueness

• Variance specific to that variable
• Includes measurement error and variable specific effects

FA assumes uniqueness exists. PCA assumes it does not.

## 3. Factor Loadings: How to Read Them Properly

Factor loadings are correlations between observed variables and factors.

Interpretation guidelines:

• Absolute value matters more than sign
• Loadings ≥ 0.7 are strong
• Loadings between 0.4 and 0.6 are moderate
• Loadings < 0.3 are often ignored

Cross loadings matter:

• If a variable loads strongly on multiple factors, interpretation becomes muddy
• Clean factors have variables that load strongly on one factor and weakly on others

Rotation exists almost entirely to improve this clarity.

## 4. Extraction Methods and What They Assume

Different extraction methods answer slightly different questions.

### Principal Axis Factoring

• Focuses on shared variance only
• Most common for psychological and social science data
• Robust when data is not perfectly normal

### Maximum Likelihood

• Assumes multivariate normality
• Allows statistical tests of model fit
• Preferred when doing confirmatory work

### Principal Components (misused as FA)

• Extracts total variance
• Often incorrectly labeled as factor analysis
• Useful descriptively, misleading inferentially

## 5. Rotation Is Not Optional, It Is Interpretive

Unrotated factors are mathematically correct but psychologically useless.

### Orthogonal Rotation

• Factors are forced to be uncorrelated
• Simpler math
• Often unrealistic for human data

### Oblique Rotation

• Factors are allowed to correlate
• Produces two matrices:
• Pattern matrix showing unique factor contributions
• Structure matrix showing correlations

Most real world constructs are correlated. Oblique rotation reflects reality better.

## 6. Deciding the Number of Factors

This is where many analyses quietly fail.

Common techniques:

• Eigenvalues greater than 1 rule
• Scree plot elbow inspection
• Parallel analysis comparing against random data

Best practice:

• Do not rely on a single method
• Combine statistical evidence with domain knowledge

Factor analysis is not purely mechanical. Judgment matters.

## 7. Assumptions You Should Explicitly Check

Factor analysis quietly assumes:

• Linear relationships between variables
• Sufficient correlations among variables
• Reasonable sample size

Rules of thumb for sample size:

• Minimum of 5 to 10 observations per variable
• Absolute minimum often cited as 100 observations

Violating these does not always break FA, but it weakens conclusions.

## 8. Common Failure Modes

Things that go wrong in practice:

• Too many variables with low communalities
• Over interpreting weak loadings
• Naming factors based on one variable
• Treating exploratory results as confirmed truth

FA is hypothesis generating unless explicitly confirmatory.

## 9. When to Stop and Use CFA Instead

Move to confirmatory factor analysis when:

• You have a clear theoretical structure
• You want to test model fit explicitly
• You care about goodness of fit metrics

CFA asks:
“Does this model explain the data well enough?”

EFA asks:
“What model might explain this data?”

Confusing these two leads to false confidence.

## 10. Mental Model to Keep You Honest

A useful way to think about FA:

• Factors are not real objects
• They are compressed explanations
• They exist only insofar as they predict correlations

If a factor stops predicting correlations, it stops existing.

That mindset keeps interpretation sharp and prevents mystical thinking about latent variables.

## Points That Require Care or Verification

• Exact cutoff thresholds for loadings vary by field
• Sample size rules are heuristics, not laws
• Rotation choice depends on domain assumptions

These are methodological conventions, not physical constants.

If you want, the next natural layer is walking through a real factor loading matrix and practicing how to name factors without lying to yourself.