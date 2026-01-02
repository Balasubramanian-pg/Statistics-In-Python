**Factor Analysis (FA)** is a statistical method used to describe variability among observed, correlated variables in terms of a potentially lower number of unobserved variables called **factors**.

Think of it as a way to find "hidden" patterns. For instance, if a student gets high scores in algebra, geometry, and calculus, factor analysis might suggest these are all driven by a single underlying factor: "Mathematical Ability."

## 1. Core Concepts

Factor analysis operates on the assumption that your data contains "latent" constructs that cannot be measured directly but influence the things you *can* measure.

* **Latent Variables (Factors):** The hidden variables that cause the patterns in your data (e.g., Intelligence, Happiness, Brand Loyalty).
* **Observed Variables:** The actual data you collected (e.g., test scores, survey responses).
* **Factor Loadings:** Coefficients that represent the strength of the relationship between an observed variable and the underlying factor. A loading of 0.7 or higher usually indicates a strong link.
* **Communality:** The proportion of a variable's variance that is explained by the factors.

## 2. Types of Factor Analysis

There are two primary ways researchers use this tool depending on whether they are exploring a new dataset or testing an existing theory:

| Feature | Exploratory Factor Analysis (EFA) | Confirmatory Factor Analysis (CFA) |
| --- | --- | --- |
| **Goal** | To identify the underlying structure of data. | To test if the data fits a specific model/theory. |
| **When to use** | Early stages of research; "I don't know what the factors are yet." | Late stages; "I think these 3 factors exist, let me prove it." |
| **Flexibility** | High—allows variables to load on any factor. | Low—variables are "assigned" to specific factors. |

## 3. Factor Analysis vs. PCA

People often confuse Factor Analysis with **Principal Component Analysis (PCA)**. While both reduce data dimensions, they have different philosophies:

* **PCA** is a mathematical "summary." It squashes variables together to retain as much information (variance) as possible. It assumes there is no "error" in the measurements.
* **Factor Analysis** is a "model." It assumes that your observed variables are imperfect reflections of a deeper reality and accounts for "error" or unique variance in each variable.

## 4. How the Process Works

1. **Check for Suitability:** Use tests like **KMO (Kaiser-Meyer-Olkin)** and **Bartlett’s Test** to see if your variables are correlated enough to justify an analysis.
2. **Extraction:** Choose a method (like Principal Axis Factoring) to pull the factors out of the data.
3. **Rotation:** This is a mathematical trick to make the output easier to read.
* **Varimax (Orthogonal):** Used if you think your factors are independent.
* **Promax/Oblimin (Oblique):** Used if you think your factors might be related (most common in psychology).


4. **Interpretation:** Look at which variables "load" onto which factors and give the factors a name.

## 5. Common Applications

* **Psychology:** Identifying personality traits (e.g., "The Big Five").
* **Marketing:** Grouping customer survey responses into "Price Sensitivity" or "Brand Trust."
* **Health:** Grouping symptoms to identify underlying syndromes or diseases.
