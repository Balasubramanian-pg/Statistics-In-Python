The expected value and variance are fundamental concepts in probability theory and statistics that help us understand the central tendency and spread of a random variable.


#### Expected Value

The expected value, also known as the mean or expectation, provides a measure of the central tendency of a random variable. For both discrete and continuous random variables, the expected value gives us an idea of what value we would expect to see on average if we were to repeat an experiment many times.

**For a Discrete Random Variable:** If X is a discrete random variable with possible values x1​,x2​,…,xn​ and corresponding probabilities P(X=x1​),P(X=x2​),…,P(X=xn​), the expected value E(X) is calculated as:

E(X)=i=1∑n​xi​⋅P(X=xi​)

In other words, you multiply each possible value by its probability and then sum all these products.

**For a Continuous Random Variable:** If X is a continuous random variable with a probability density function (PDF) f(x), the expected value is given by the integral over all possible values of X:

E(X)=∫−∞∞​x⋅f(x)dx

**Properties of Expected Value:**

1. **Linearity:** For any two random variables X and Y and constants a and b:
    
    - E(aX+bY)=aE(X)+bE(Y)
        
    - E(aX+b)=aE(X)+b
        


#### Variance
Variance measures how spread out the values of a random variable are. A **high variance** indicates that the values are spread out over a wider range, while a **low variance** indicates that the values are clustered more closely around the mean. The variance of a random variable X is denoted by Var(X) or σ2, and it is defined as the expected value of the squared deviation from the mean:

Var(X)=E[(X−μ)2]

where μ=E(X) is the expected value of X.

For a discrete random variable, the variance is calculated as:

Var(X)=i=1∑n​(xi​−μ)2⋅P(X=xi​)

For a continuous random variable, the variance is given by the integral:

Var(X)=∫−∞∞​(x−μ)2⋅f(x)dx

The variance can also be computed using the following alternative formula, which is often easier to work with:

Var(X)=E(X2)−[E(X)]2

where E(X2) is the expected value of the squared random variable.

**Properties of Variance:**

1. For any constant a and b:
    
    - Var(aX+b)=a2Var(X)
        
2. For independent random variables X and Y:
    
    - Var(X+Y)=Var(X)+Var(Y)
        


#### Examples

**Example 1: Discrete Random Variable**

Consider a random variable X representing the outcome of a roll of a fair six-sided die. The possible outcomes and their probabilities are:

- xi​: 1, 2, 3, 4, 5, 6
    
- P(X=xi​): 61​ for each outcome
    

The expected value E(X) is calculated as:

E(X)=1⋅61​+2⋅61​+3⋅61​+4⋅61​+5⋅61​+6⋅61​

E(X)=61+2+3+4+5+6​=621​=3.5

So, the expected value is **3.5**.

Now, let's calculate the variance. First, we need to find E(X2):

E(X2)=12⋅61​+22⋅61​+32⋅61​+42⋅61​+52⋅61​+62⋅61​

E(X2)=61+4+9+16+25+36​=691​≈15.1667

Now, using the alternative formula for variance:

$$\text{Var}(X) = E(X^2) - [E(X)]^2$$$$\text{Var}(X) = 15.1667 - (3.5)^2$$$$\text{Var}(X) = 15.1667 - 12.25$$

Var(X)≈2.9167

So, the variance is approximately **2.9167**.


**Example 2: Continuous Random Variable**

Consider a continuous random variable X with a uniform distribution over the interval [0,1]. The probability density function (PDF) is:

f(x)=1for0≤x≤1

The expected value E(X) is calculated as:

E(X)=∫01​x⋅f(x)dx=∫01​x⋅1dx

E(X)=2x2​![](data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="0.333em" height="2.400em" viewBox="0 0 333 2400"><path d="M145 15 v585 v1200 v585 c2.667,10,9.667,15,21,15
c10,0,16.667,-5,20,-15 v-585 v-1200 v-585 c-2.667,-10,-9.667,-15,-21,-15
c-10,0,-16.667,5,-20,15z M188 15 H145 v585 v1200 v585 h43z"></path></svg>)​01​=21​

So, the expected value is **0.5**.

Now, let's find the variance. First, we need to find E(X2):

E(X2)=∫01​x2⋅f(x)dx=∫01​x2⋅1dx

E(X2)=3x3​![](data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="0.333em" height="2.400em" viewBox="0 0 333 2400"><path d="M145 15 v585 v1200 v585 c2.667,10,9.667,15,21,15
c10,0,16.667,-5,20,-15 v-585 v-1200 v-585 c-2.667,-10,-9.667,-15,-21,-15
c-10,0,-16.667,5,-20,15z M188 15 H145 v585 v1200 v585 h43z"></path></svg>)​01​=31​

Now, using the alternative formula for variance:

$$\text{Var}(X) = E(X^2) - [E(X)]^2$$$$\text{Var}(X) = \frac{1}{3} - \left( \frac{1}{2} \right)^2$$$$\text{Var}(X) = \frac{1}{3} - \frac{1}{4}$$$$\text{Var}(X) = \frac{4}{12} - \frac{3}{12}$$$$\text{Var}(X) = \frac{1}{12}$$

So, the variance is **121​**.


These examples should help illustrate how to calculate the expected value and variance for both discrete and continuous random variables.

In summary, the **expected value** gives us the central tendency of a random variable, while the **variance** gives us a measure of the spread of the values around the mean. These two concepts are fundamental in probability theory and are widely used in various fields such as statistics, finance, and engineering.