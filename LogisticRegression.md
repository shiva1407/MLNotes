# Logistic Regression

Logistic regression is a supervised learning algorithm used for binary classification tasks, where the target variable has two possible outcomes (e.g., spam/not spam, fraud/not fraud, etc.). Despite its name, logistic regression is a classification algorithm, not a regression algorithm. It's called "regression" because it uses a linear regression model to estimate the probability that a given input belongs to a particular class.

## How Logistic Regression Works

1. **Sigmoid Function**: Logistic regression uses the sigmoid function (also known as the logistic function) to transform the output of a linear regression model into a probability value between 0 and 1. The sigmoid function is defined as:

   <img width="564" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/59d78120-bbc6-42ae-8720-92a12680da3f">


2. **Decision Boundary**: Logistic regression predicts the class label based on whether the probability output by the sigmoid function is greater than a threshold (usually 0.5). If the probability is greater than 0.5, the input is classified as belonging to the positive class; otherwise, it's classified as belonging to the negative class.

## Loss Function: Binary Cross-Entropy Loss

Logistic regression uses the binary cross-entropy loss (also known as log loss) as its loss function. The binary cross-entropy loss measures the difference between the predicted probabilities and the true class labels.

   ![Binary Cross-Entropy Loss](https://latex.codecogs.com/svg.latex?J(\theta)%20=%20-\frac{1}{m}%20\sum_{i=1}^{m}%20[y^{(i)}\log(\hat{y}^{(i)})%20+%20(1%20-%20y^{(i)})\log(1%20-%20\hat{y}^{(i)})])

   where:
   <img width="508" alt="image" src="https://github.com/shiva1407/MLNotes/assets/31319750/f92008c6-4729-4b93-be37-0237ccf3ba0e">


## Example: Spam Email Classification

Suppose you're building a spam email classifier using logistic regression. You have a dataset containing features extracted from emails (e.g., word frequency, presence of certain keywords) and corresponding labels indicating whether each email is spam (1) or not spam (0).

1. **Data Preparation**: You preprocess the data, splitting it into training and test sets, and scaling or normalizing the features if necessary.

2. **Model Training**: You train a logistic regression model on the training data. The model learns the optimal coefficients (weights) to minimize the binary cross-entropy loss function.

3. **Model Evaluation**: You evaluate the trained model on the test data to assess its performance. You calculate metrics such as accuracy, precision, recall, and F1-score to measure how well the model classifies spam and non-spam emails.

4. **Prediction**: You use the trained model to predict the class labels (spam or not spam) for new, unseen emails.

Logistic regression is widely used in various applications such as email spam detection, credit risk assessment, medical diagnosis, and many others, where binary classification is required. Despite its simplicity, logistic regression can be quite effective, especially when the relationship between the features and the target variable is approximately linear and the classes are separable.
