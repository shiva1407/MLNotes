# Feature Selection Techniques in Machine Learning

Feature selection is a crucial step in machine learning model building, aiming to identify the most relevant features that contribute the most to the predictive power of the model. There are various techniques for feature selection, which can be broadly classified into different categories.

## Supervised Techniques

These techniques are used for labeled data to identify relevant features for improving the efficiency of supervised models like classification and regression.


From a taxonomic point of view, feature selection techniques can be classified into filter, wrapper, embedded, and hybrid methods. Let's discuss some popular machine learning feature selection methods in detail.

## Filter Methods

Filter methods pick up the intrinsic properties of the features measured via univariate statistics instead of cross-validation performance. These methods are faster and less computationally expensive than wrapper methods. When dealing with high-dimensional data, it is computationally cheaper to use filter methods.

### Information Gain

Information gain calculates the reduction in entropy from the transformation of a dataset. It can be used for feature selection by evaluating the Information gain of each variable in the context of the target variable.

```python
from sklearn.feature_selection import mutual_info_classif

# Calculate mutual information for feature selection
information_gain = mutual_info_classif(X, y)

```
### Chi-square Test

The Chi-square test is used for categorical features in a dataset. We calculate Chi-square between each feature and the target and select the desired number of features with the best Chi-square scores.


```python
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Select features based on Chi-square test
selector = SelectKBest(score_func=chi2, k=5)
X_selected = selector.fit_transform(X, y)

```
### Fisher’s Score

Fisher score is one of the most widely used supervised feature selection methods. The algorithm returns the ranks of the variables based on the Fisher’s score in descending order.

```python
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import fisher_score

# Select features based on Fisher's score
selector = SelectKBest(score_func=fisher_score, k=5)
X_selected = selector.fit_transform(X, y)

```
### Correlation Coefficient

Correlation coefficient measures the linear relationship between two or more variables. It can be used for feature selection by selecting variables highly correlated with the target.

```python
# Calculate Pearson correlation coefficient
correlation_matrix = df.corr()

```

### Variance Threshold

Variance threshold is a simple baseline approach to feature selection. It removes all features whose variance doesn’t meet some threshold.

```python
from sklearn.feature_selection import VarianceThreshold

# Remove features with low variance
selector = VarianceThreshold(threshold=0.2)
X_selected = selector.fit_transform(X)
```

## Wrapper Methods

Wrappers require some method to search the space of all possible subsets of features, assessing their quality by learning and evaluating a classifier with that feature subset. The feature selection process is based on a specific machine learning algorithm we are trying to fit on a given dataset. Wrapper methods usually result in better predictive accuracy than filter methods.

### Forward Feature Selection

Forward feature selection is an iterative method wherein we start with the performing features against the target features. Next, we select another variable that gives the best performance in combination with the first selected variable. This process continues until the preset criterion is achieved.

```python
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.ensemble import RandomForestClassifier

# Perform forward feature selection with Random Forest
selector = SequentialFeatureSelector(RandomForestClassifier(), n_features_to_select=5, direction='forward')
X_selected = selector.fit_transform(X, y)

```
### Backward Feature Elimination

This method works exactly opposite to the Forward Feature Selection method. Here, we start with all the features available and build a model. Next, we remove the variable from the model, which gives the best evaluation measure value. This process is continued until the preset criterion is achieved.

```python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

# Perform backward feature elimination with Linear Regression
selector = RFE(LinearRegression(), n_features_to_select=5, step=1)
X_selected = selector.fit_transform(X, y)

```
### Exhaustive Feature Selection

This is the most robust feature selection method covered so far. This is a brute-force evaluation of each feature subset. This means it tries every possible combination of the variables and returns the best-performing subset.

```python 
### Recursive Feature Elimination
```
Given an external estimator that assigns weights to features (e.g., the coefficients of a linear model), the goal of recursive feature elimination (RFE) is to select features by recursively considering smaller and smaller sets of features. First, the estimator is trained on the initial set of features, and each feature’s importance is obtained either through a coef_ attribute or a feature_importances_ attribute. Then, the least important features are pruned from the current set of features. That procedure is recursively repeated on the pruned set until the desired number of features to select is eventually reached.

```python
from sklearn.feature_selection import RFECV
from sklearn.svm import SVC

# Perform recursive feature elimination with cross-validation
selector = RFECV(estimator=SVC(), step=1, cv=5)
X_selected = selector.fit_transform(X, y)

```
## Embedded Methods

Embedded methods encompass the benefits of both the wrapper and filter methods by including interactions of features but also maintaining reasonable computational costs. Embedded methods are iterative in the sense that they take care of each iteration of the model training process and carefully extract those features which contribute the most to the training for a particular iteration.

### LASSO Regularization (L1)

Regularization consists of adding a penalty to the different parameters of the machine learning model to reduce the freedom of the model, i.e., to avoid over-fitting. Lasso or L1 has the property that can shrink some of the coefficients to zero, thereby removing the corresponding features from the model.

```python
from sklearn.linear_model import LassoCV

# Perform feature selection with LASSO regularization
selector = LassoCV()
selector.fit(X, y)
```

### Random Forest Importance

Random Forests aggregate decision trees and naturally rank features based on how well they improve the purity of the node. By pruning trees below a particular node, we can create a subset of the most important features.

```python
from sklearn.ensemble import RandomForestClassifier

# Perform feature selection based on Random Forest importance
model = RandomForestClassifier()
model.fit(X, y)
importances = model.feature_importances_
```
These are some of the popular feature selection techniques in machine learning, each with its own strengths and weaknesses. The choice of technique depends on the specific requirements of the problem and the characteristics of the dataset.

