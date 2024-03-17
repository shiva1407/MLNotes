# Understanding Assumptions in Linear Regression

When working with linear regression, it's essential to understand the underlying assumptions behind the model. These assumptions help ensure the reliability and validity of the regression analysis. Let's explore these assumptions in detail.

## Trivial Assumptions:

### 1. Linearity between Features and Target Variable:

The expression 

![image](https://github.com/shiva1407/MLNotes/assets/31319750/c6c658af-329c-492f-a256-918aadb064d8)

Here, if both m1 and m2 are real numbers then we can say that x1 and x2 are linearly related to target variable(y). If m1 and m2 are not real numbers then we can say that x1 and x2 aren’t linearly related to target variable y.

### 2. Homoscedasticity Assumption in Linear Regression


Homoscedasticity means that variance of samples taken from the data should remain constant i.e., we need our data points(observations) to be closer to the plane that we have predicted if drawn spatially.

Homoscedasticity, also known as homogeneity of variance, is a fundamental assumption in linear regression analysis. It refers to the condition where the variance of the errors (residuals) is constant across all levels of the independent variables. This assumption is crucial for ensuring the reliability of the model's predictions and the validity of statistical inferences.

In the below figure, you can see that variance remains constant in the first case (Homoscedastic behaviour) and not in the second case(Heteroscedastic behaviour).

![image](https://github.com/shiva1407/MLNotes/assets/31319750/74ed6682-3df4-4356-98d7-4eb69608172d)

![image](https://github.com/shiva1407/MLNotes/assets/31319750/1ffda722-3ed6-47d4-ba52-69b198de7572)



## Importance of Homoscedasticity Assumption

Homoscedasticity, or homogeneity of variance, is a critical assumption in linear regression for several reasons:

1. **Model Reliability:**
   - Homoscedasticity ensures that the errors (residuals) have a consistent spread across all levels of the independent variables. This consistency indicates that the model's predictions are equally reliable across the range of predicted values.
   -  Homoscedasticity ensures that the errors have a consistent spread, which is essential for the reliability of the model's predictions. If the variance of errors varies significantly across the range of predicted values, it indicates potential issues with the model's explanatory power.

2. **Statistical Inference:**
   - Violations of the homoscedasticity assumption can lead to biased estimates of the model parameters. It can distort the estimated coefficients and affect the validity of statistical tests, confidence intervals, and hypothesis testing conducted on the regression coefficients.
   - It can affect the validity of statistical tests, confidence intervals, and hypothesis testing conducted on the regression coefficients.

3. **Interpretability:**
   - Homoscedasticity simplifies the interpretation of the regression coefficients. It makes it easier to assess the impact of each independent variable on the dependent variable, enhancing the interpretability of the model.

4. **Assumption of Constant Error Variance:**
   - Linear regression assumes that the errors have constant variance across all levels of the independent variables. Homoscedasticity ensures the validity of the least squares estimation method used in linear regression.

In summary, homoscedasticity is essential in linear regression to ensure the reliability of the model's predictions, the validity of statistical inferences, and the interpretability of the regression coefficients. Detecting and addressing violations of the homoscedasticity assumption is crucial for building accurate and reliable regression models.

In mathematical terms, the homoscedasticity assumption can be expressed as:

<img width="505" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/1bf2873f-2d15-4ea8-9656-35ae1cad6677">

## Diagnostic Techniques

Several diagnostic techniques can be employed to check for homoscedasticity in a linear regression model:

1. **Residual Plot:** Plot the residuals against the predicted values. A constant spread of residuals across all predicted values suggests homoscedasticity.

2. **Goldfeld-Quandt Test:** This statistical test divides the dataset into two subsets based on the values of an independent variable and compares the variances of the residuals in the two subsets.

3. **Breusch-Pagan Test:** This test examines whether the variance of the residuals is related to the values of the independent variables.

## Addressing Violations

If the assumption of homoscedasticity is violated, several strategies can be employed:

- Transforming the dependent or independent variables to stabilize the variance.
- Using weighted least squares regression, where observations with higher variance are given lower weights.
- Employing robust regression techniques that are less sensitive to violations of homoscedasticity.

In summary, homoscedasticity is a critical assumption in linear regression analysis, ensuring the reliability of the model's predictions and the validity of statistical inferences. Understanding and diagnosing homoscedasticity are essential steps in building accurate and interpretable regression models.





### 3. No Outliers:

Outliers can significantly impact the predicted regression plane and the overall performance of the model. Hence, it's essential to detect and remove outliers before applying linear regression.

## Non-trivial Assumptions:


To understand the rationale behind other assumptions in linear regression, let's delve into the mathematical derivations involved in linear regression optimization.

## Choosing the Cost Function:

### 1. Normality of Residuals:
   - **Definition:** Residuals  follow a Gaussian distribution with mean zero and constant variance.
   - **Mathematical Assumption:**
                <img width="118" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/971a3d51-0b40-49ca-a922-b10a2c12208f">

   - **Rationale:** Normality of residuals ensures random distribution around zero with a constant spread, facilitating valid statistical inferences.

### 2. Independence of Residuals:
   - **Definition:** Residuals are independent and identically distributed (i.i.d), implying no autocorrelation.
   - **Mathematical Assumption:**
            <img width="192" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/870013a4-4e7f-4986-9d76-d93397d7f8cf">

   - **Rationale:** Independence ensures errors from one observation do not influence errors of another, crucial for statistical tests and predictions.

## Minimizing Cost Function:

### 1. Linear Independence of Columns:
   - **Definition:** Design matrix  has linearly independent columns.
   - **Mathematical Assumption:** No column of X can be expressed as a linear combination of others.
   - **Rationale:** Ensures  XTX is invertible, crucial for finding the unique solution to the least squares problem.

### 2. No Multicollinearity:
   - **Definition:** Absence of high correlation between independent variables.
   - **Mathematical Assumption:** Correlation matrix of X does not have high correlations (\( \rho > 0.8 \)).
   - **Rationale:** Prevents inflated standard errors of coefficients and difficulty in interpreting individual variable effects.

These assumptions form the mathematical foundation for performing linear regression analysis and interpreting results accurately.
