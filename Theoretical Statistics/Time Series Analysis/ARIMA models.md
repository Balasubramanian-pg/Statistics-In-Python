---
Due Date: 2025-07-03
Urgency: Good To Have
---
ARIMA stands for **AutoRegressive Integrated Moving Average**. It's a time series forecasting model used when your data shows trends over time.

Here's the breakdown:

- **AR (AutoRegressive)**: The model uses past values to predict the current one. Think: “What happened last month affects this month.”
- **I (Integrated)**: It makes the data _stationary_ (i.e., removes trends or seasonality) by differencing. Like taking change instead of actual value.
- **MA (Moving Average)**: It uses past forecast errors to improve predictions. So, if it messed up earlier, it learns from that.
    

Notation: **ARIMA(p, d, q)**

- `p` = number of AR terms
- `d` = number of differences
- `q` = number of MA terms

It's good for non-stationary data with trends but not seasonality (that’s where SARIMA comes in). 

Cool, let’s build a basic ARIMA model step by step. I’ll assume you're using Python with `pandas` and `statsmodels`. You can replace the dataset with yours.

---

### **Step 0: Install dependencies (if not done)**

```bash
pip install pandas matplotlib statsmodels
```

---

### **Step 1: Import and visualize the data**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load a time series dataset (e.g., monthly airline passengers)
df = pd.read_csv('AirPassengers.csv', index_col='Month', parse_dates=True)
df.plot(title='Original Data')
plt.show()
```

---

### **Step 2: Make the data stationary**

```python
# Check for stationarity visually and with .diff()
df_diff = df.diff().dropna()
df_diff.plot(title='After Differencing')
plt.show()
```

---

### **Step 3: Use ACF and PACF to find p and q**

```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(df_diff)
plot_pacf(df_diff)
plt.show()
```

Look at how long the bars stay above the threshold — that gives you `q` (from ACF) and `p` (from PACF).

---

### **Step 4: Fit the ARIMA model**

```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(df, order=(p, d, q))  # Replace p,d,q with your values
model_fit = model.fit()
print(model_fit.summary())
```

---

### **Step 5: Forecast**

```python
forecast = model_fit.forecast(steps=12)
df.plot()
forecast.plot(title='Forecast')
plt.show()
```

---

### TL;DR

1. Clean the data
2. Difference to remove trend
3. Use ACF/PACF to get p, d, q
4. Fit ARIMA
5. Forecast and profit


Yep. Let's walk through a **real ARIMA example** using the classic **AirPassengers** dataset (monthly airline passengers from 1949 to 1960). This is time series gold for demos.

---

### **Step 1: Load and plot data**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
df = pd.read_csv(url, index_col='Month', parse_dates=True)

df.columns = ['Passengers']
df.plot(title='Monthly Airline Passengers')
plt.show()
```

You’ll see a clear upward **trend** and possible **seasonality**.

---

### **Step 2: Check stationarity**

```python
from statsmodels.tsa.stattools import adfuller

result = adfuller(df['Passengers'])
print(f'p-value: {result[1]}')
```

If `p-value > 0.05`, the data is **non-stationary** — we need to difference it.

---

### **Step 3: Make it stationary**

```python
df_diff = df.diff().dropna()
df_diff.plot(title='Differenced Data')
plt.show()

# Recheck stationarity
result = adfuller(df_diff['Passengers'])
print(f'New p-value: {result[1]}')
```

Now, `d = 1`.

---

### **Step 4: Determine p and q with ACF/PACF**

```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(df_diff)
plot_pacf(df_diff)
plt.show()
```

Let’s say:

- PACF cuts off at lag 2 ⇒ `p = 2`
    
- ACF cuts off at lag 2 ⇒ `q = 2`
    

---

### **Step 5: Fit ARIMA**

```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(df, order=(2,1,2))
model_fit = model.fit()
print(model_fit.summary())
```

You’ll get coefficients, AIC/BIC, and p-values. Watch for low p-values (<0.05) — they’re significant.

---

### **Step 6: Forecast**

```python
forecast = model_fit.forecast(steps=12)
df['Passengers'].plot(label='Original', legend=True)
forecast.plot(label='Forecast', legend=True, title='Forecast for next 12 months')
plt.show()
```

---

That’s ARIMA in action. Want me to explain what AIC/BIC means or how to automate this with `pmdarima`?

Use **ARIMA** when:

1. **Your data is a time series**  
    One column is a time-based index (dates, months, etc.), and you want to forecast future values.
2. **There’s a clear trend**  
    ARIMA is built for handling trending data by differencing it.
3. **There’s **no strong seasonality**  
    If you see repeating yearly/monthly patterns, ARIMA alone might underperform. Use **SARIMA** or **Prophet** instead.
4. **The data is univariate**  
    ARIMA only handles _one variable_ — the one you're trying to predict.
5. **You want explainability**  
    ARIMA is simple and easy to interpret compared to black-box models like LSTMs.

If your data is seasonal, use **SARIMA**. If it's irregular and noisy, maybe try **Prophet** or machine learning models.

Here’s a no-BS cheat sheet for when to use which time series model:

|Model|Use When...|Handles Seasonality?|Multivariate?|Strengths|
|---|---|---|---|---|
|**ARIMA**|Trendy, non-seasonal, univariate time series|No|No|Interpretable, statistical grounding|
|**SARIMA**|Like ARIMA, but data has clear seasonal cycles|Yes|No|Good for seasonal forecasts|
|**Prophet**|Seasonality + holidays + weird events in messy data|Yes|No|Robust to missing data, intuitive|
|**Exponential Smoothing (ETS)**|Stable trend and seasonality|Yes|No|Simple, strong on smooth data|
|**VAR**|Multiple time series that affect each other|No|Yes|Good for interconnected metrics|
|**LSTM/RNN**|Huge data, long memory needed, non-linear patterns|Yes (kinda)|Yes|Can learn complex relationships|
|**XGBoost/ML models**|You have features beyond time|Indirectly|Yes|Flexible, powerful, black-boxy|

**TL;DR**

- Use **ARIMA** when you have clean, trending data.
- Switch to **SARIMA** or **Prophet** if seasonality is real.
- Use **ML/DL** if you want power, don’t care about explainability, or have rich features.

