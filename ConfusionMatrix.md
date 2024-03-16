# What Is a Confusion Matrix?

A confusion matrix is a performance evaluation tool in machine learning, representing the accuracy of a classification model. It displays the number of true positives, true negatives, false positives, and false negatives. This matrix aids in analyzing model performance, identifying mis-classifications, and improving predictive accuracy.

## Definition

A confusion matrix is an N x N matrix used for evaluating the performance of a classification model, where N is the total number of target classes. The matrix compares the actual target values with those predicted by the machine learning model. This gives us a holistic view of how well our classification model is performing and what kinds of errors it is making.

### Example

Imagine a binary classification problem where we predict whether a person has a disease or not. Here's a simplified confusion matrix for this scenario:

|               | Predicted Negative | Predicted Positive |
|---------------|--------------------|--------------------|
| Actual Negative | True Negative (TN) | False Positive (FP) |
| Actual Positive | False Negative (FN) | True Positive (TP) |

## Important Terms in a Confusion Matrix

### True Positive (TP)

- The predicted value matches the actual value, or the predicted class matches the actual class.
- The actual value was positive, and the model predicted a positive value.

### True Negative (TN)

- The predicted value matches the actual value, or the predicted class matches the actual class.
- The actual value was negative, and the model predicted a negative value.

### False Positive (FP) – Type I Error

- The predicted value was falsely predicted.
- The actual value was negative, but the model predicted a positive value.
- Also known as the type I error.

### False Negative (FN) – Type II Error

- The predicted value was falsely predicted.
- The actual value was positive, but the model predicted a negative value.
- Also known as the type II error.

## Why Do We Need a Confusion Matrix?

A confusion matrix helps us understand how well our model is performing, especially in scenarios where accuracy alone may be misleading due to class imbalance or differing importance of errors. It provides insights into the types of errors our model is making and guides us in improving its performance.

## How to Calculate Confusion Matrix for a 2-class Classification Problem?

To calculate the confusion matrix for a 2-class classification problem, you will need to know the following:

- True positives (TP): The number of samples that were correctly predicted as positive.
- True negatives (TN): The number of samples that were correctly predicted as negative.
- False positives (FP): The number of samples that were incorrectly predicted as positive.
- False negatives (FN): The number of samples that were incorrectly predicted as negative.

Once you have these values, you can calculate the confusion matrix using the following table:

|              | Predicted Negative | Predicted Positive |
|--------------|---------------------|---------------------|
| Actual Negative | True Negatives (TN) | False Positives (FP) |
| Actual Positive | False Negatives (FN) | True Positives (TP) |

## Precision vs. Recall

Precision tells us how many of the correctly predicted cases actually turned out to be positive, while recall tells us how many of the actual positive cases we were able to predict correctly with our model.

- **Precision**: TP / (TP + FP)
- **Recall**: TP / (TP + FN)

## What Is F1-Score?

In practice, when we try to increase precision, recall may decrease and vice versa. The F1-score, which is the harmonic mean of precision and recall, captures both trends in a single value. It is maximum when precision is equal to recall.

F1-Score = 2 * (Precision * Recall) / (Precision + Recall)

However, the interpretability of the F1-score is poor, so it is often used in combination with other evaluation metrics.

