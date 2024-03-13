# Math Behind Logistic Regression

Logistic regression is a fundamental statistical method used for binary classification problems. It models the probability that a given input belongs to a particular class. Despite its name, logistic regression is actually a classification algorithm rather than a regression algorithm.

Here's a brief overview of the math behind logistic regression:

## Linear Combination

Similar to linear regression, logistic regression starts with a linear combination of the input features weighted by coefficients:

<img width="458" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/91941dba-9d19-440c-89c6-3b4b798ff783">


## Sigmoid Function

The linear combination \( z \) is then passed through the sigmoid function to produce the probability of belonging to a particular class. The sigmoid function "squashes" the output of the linear combination to the range [0, 1]:

<img width="445" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/f2e9c143-ff47-461b-9e35-de61456558f9">


The sigmoid function ensures that the output is always between 0 and 1, which can be interpreted as the probability of belonging to the positive class.

## Decision Boundary

In binary classification, a decision boundary is used to separate the classes. This decision boundary is typically set at \( p = 0.5 \). If \( p \) is greater than 0.5, the input is classified as belonging to the positive class; otherwise, it's classified as belonging to the negative class.

## Cost Function

The cost function used in logistic regression is the log loss (or cross-entropy) function, which measures the difference between the predicted probabilities and the actual class labels:

<img width="407" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/c80d59e3-e54c-4e0b-93ce-e062c9623bce">


## Optimization

The goal of logistic regression is to minimize the cost function \( J(b) \) with respect to the coefficients \( b \). This is typically done using optimization algorithms such as gradient descent.

By adjusting the coefficients \( b \) through the optimization process, logistic regression learns to make predictions about the probability of belonging to a particular class based on the input features.

### Sigmoid Function and Log Odds

The sigmoid function, also known as the logistic function, is a mathematical function that maps any real-valued number to the range [0, 1]. It has an S-shaped curve and is defined as:

<img width="161" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/b65a85d4-9dda-443b-8ee2-ba0d95edd5ca">


Where:
- \( z \) is any real number.

The key property of the sigmoid function is that it outputs values between 0 and 1 for any input value of \( z \). This property makes it suitable for modeling probabilities in logistic regression.

To understand how the sigmoid function accomplishes this, let's analyze its behavior:
<img width="426" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/1446dd4e-afe4-4e60-9347-b5269090c964">


Therefore, regardless of the input value of \( z \), the sigmoid function ensures that the output is bounded between 0 and 1.

The log odds, also known as the logit function, represents the logarithm of the odds of a binary event. For a binary classification problem where the event of interest is labeled as 1 (positive class) and the other outcome is labeled as 0 (negative class), the log odds of an event happening can be expressed as:

<img width="310" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/b47f9cf9-46a2-42ad-a6cf-d962834a9963">


Where:
- \( p \) is the probability of the event occurring.

The log odds can take any real value from \(-\infty\) to \(+\infty\). When \( p = 0.5 \), the log odds are 0, indicating that the event is equally likely to occur or not occur. Positive log odds imply a higher probability of the event occurring, while negative log odds imply a lower probability.

In logistic regression, the linear combination of input features is transformed into log odds through the logistic function (sigmoid function), and then the log odds are used to predict the probability of the positive class.
