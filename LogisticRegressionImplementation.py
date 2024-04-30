import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None
    
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def initialize_parameters(self, num_features):
        self.weights = np.zeros((num_features, 1))
        self.bias = 0
    
    def hypothesis(self, X):
        return self.sigmoid(np.dot(X, self.weights) + self.bias)
    
    def compute_loss(self, y_true, y_pred):
        m = len(y_true)
        return -1/m * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    
    def gradient_descent(self, X, y_true, y_pred):
        m = len(y_true)
        dw = 1/m * np.dot(X.T, (y_pred - y_true))
        db = 1/m * np.sum(y_pred - y_true)
        self.weights -= self.learning_rate * dw
        self.bias -= self.learning_rate * db
    
    def train(self, X, y):
        self.initialize_parameters(X.shape[1])
        
        for i in range(self.num_iterations):
            y_pred = self.hypothesis(X)
            loss = self.compute_loss(y, y_pred)
            self.gradient_descent(X, y, y_pred)
            
            if i % 100 == 0:
                print(f"Iteration {i}, Loss: {loss}")
    
    def predict(self, X):
        y_pred = self.hypothesis(X)
        return (y_pred >= 0.5).astype(int)

# Example usage:
# Assuming X_train and y_train are your training data
# Initialize the model
model = LogisticRegression(learning_rate=0.1, num_iterations=1000)
# Train the model
model.train(X_train, y_train)
# Make predictions
predictions = model.predict(X_test)
