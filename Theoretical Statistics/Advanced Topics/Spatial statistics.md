## Spatial Statistics

### 1. Clear Overview

**Spatial Statistics** is a field of statistics that deals with data associated with geographic locations. It focuses on the analysis of phenomena where the location of the observation is a critical piece of information. The purpose is to model and understand patterns, distributions, and relationships in data that are influenced by their spatial position. It helps solve problems where the assumption of independent and identically distributed (i.I.d.) data is violated due to **spatial dependence** (nearby things are more related than distant things).

### 2. Structured Table of Contents

* Key Concepts (Foundational)
* Types of Spatial Data (Core)
* Core Methods (Essential Application)
* Application Summary

### 3. Create Sections for Each Main Component

#### Key Concepts

**Definition:** Spatial statistics recognizes that observations close to one another tend to be correlated. This is formally known as **spatial autocorrelation** or Tobler's First Law of Geography: "Everything is related to everything else, but near things are more related than distant things."

>[!INFO]
>Ignoring spatial autocorrelation leads to incorrect standard errors and unreliable significance tests in traditional statistical models.

**Real Life Example:** If you measure the **air pollution level** at several spots in a city, the pollution reading at one monitor will be very similar to the reading at a monitor 100 meters away, but much less similar to a reading 10 kilometers away.

**What to Apply:** To analyze spatial data, you must incorporate measures of distance and connectivity into your model.

* **Spatial Autocorrelation:** The degree to which a set of features and their corresponding values are similar in location.
    * **Positive Autocorrelation:** Clustering of similar values (e.g., high crime areas clustered together).
    * **Negative Autocorrelation:** Checkerboard pattern; high values are next to low values.
* **Stationarity:** The statistical properties of the data (like mean and variance) do not change across the study area. Many spatial methods assume some form of stationarity.
* **The Variogram/Semivariogram:** A function used to model the spatial dependence structure. 

#### Types of Spatial Data

**Definition:** Spatial data is generally categorized based on how the observations are collected and represented across space.

>[!NOTE]
>The choice of statistical method depends heavily on the type of spatial data you are working with.

**Real Life Example:** Analyzing different types of health data:
* **Point Pattern Data:** The location of every single registered **disease case** (a specific $x, y$ coordinate).
* **Areal Data:** The **average infection rate** summarized for each county or census tract (polygons).
* **Geostatistical Data:** **Soil salinity** measurements taken at irregularly spaced sample locations (a continuous field).

**Data Types and Characteristics:**

* **Geostatistical Data (Continuous Field):**
    * Data is continuous in space (e.g., elevation, temperature).
    * Measurements are taken at fixed locations, but we want to predict values at unmeasured locations.
* **Areal Data (Lattice/Polygons):**
    * Data is aggregated over defined spatial units (e.g., districts, zones).
    * Often called **Lattice Data**. The primary tool is Spatial Econometrics or Spatial Regression.
* **Point Pattern Data (Locations):**
    * The location itself is the focus (e.g., tree locations, accident spots).
    * The question is whether the pattern is random, clustered, or dispersed.

#### Core Methods

**Definition:** The core methods are the statistical techniques used to analyze each specific data type, all built on the principle of accounting for spatial relationships.

>[!CAUTION]
>Do not apply Geostatistical methods to Areal Data, or vice versa, without proper transformation, as the assumptions will be violated.

**What to Apply:**

* **Geostatistics $\rightarrow$ Kriging:**
    * This is an **optimal prediction method** used to interpolate values for locations that were not sampled, based on the spatial relationship modeled by the variogram.
    * It produces not only a prediction map but also a map of the prediction uncertainty (variance).
* **Areal Data $\rightarrow$ Spatial Regression:**
    * Used when the dependent variable and/or the error terms in a regression model are spatially correlated.
    * **Spatial Lag Model (SAR):** Assumes the dependent variable in one area is influenced by the dependent variable in neighboring areas.
    * **Spatial Error Model (SEM):** Assumes the correlation is in the error term, meaning the model's unobserved factors are spatially correlated.
* **Point Pattern Data $\rightarrow$ Density Estimation & Ripley's K:**
    * Methods used to test if points are randomly distributed, or if they exhibit clustering or dispersion.

### 4. Mark Essential vs Optional Sections

>[!INFO]
>Understanding **Spatial Autocorrelation** and the distinction between **Geostatistical, Areal, and Point Pattern data** are the **core essentials** of the field.

>[!TIP]
>Learning **Kriging** and **Spatial Regression (SAR/SEM)** are the most practical skills for applying spatial statistics in real-world scenarios like environmental modeling or urban planning.

### 5. Close With an Application Summary

**What to Remember:**

* Spatial statistics handles data where **location matters**.
* The central problem is **spatial autocorrelation** (dependence among neighbors).
* **Geostatistical data** leads to **Kriging** (prediction/interpolation).
* **Areal data** leads to **Spatial Regression** (modeling drivers/relationships).
* You must correctly model the spatial dependency to get reliable standard errors.

**Simple Real World Use Scenario:**

A city health department is mapping flu cases reported over the last month (Point Pattern Data) across all zip codes (Areal Data).

1.  **Analyze Clustering:** They use a method like Ripley's K to confirm if the **individual flu cases** are clustered in certain areas.
2.  **Run Spatial Regression:** They then link the **flu rate per zip code** (Areal Data) to variables like average income and population density.
3.  **Refinement:** They use a **Spatial Error Model (SEM)** to account for the fact that unmeasured environmental factors (like proximity to a specific school) might make neighboring zip codes similar in flu rate.
4.  **Action:** The analysis identifies both the socioeconomic drivers of the flu and the specific geographic areas needing immediate intervention.