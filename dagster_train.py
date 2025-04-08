from dagster import job, op
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

@op
def load_data():
    """
    Load the Iris dataset and split it into training and test sets.

    Returns:
        Tuple containing:
        - train_features (ndarray)
        - test_features (ndarray)
        - train_labels (ndarray)
        - test_labels (ndarray)
    """
    data = load_iris()
    # Split the dataset into train and test sets (80% train, 20% test)
    return train_test_split(data.data, data.target, test_size=0.2, random_state=42)

@op
def train_model(train_features, train_labels):
    """
    Train a Random Forest Classifier on the training data.

    Args:
        train_features (ndarray): Features for training.
        train_labels (ndarray): Labels for training.

    Returns:
        RandomForestClassifier: Trained model.
    """
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(train_features, train_labels)
    return model

@op
def evaluate_model(model, test_features, test_labels):
    """
    Evaluate the trained model on the test data.

    Args:
        model (RandomForestClassifier): Trained classifier.
        test_features (ndarray): Features for testing.
        test_labels (ndarray): Labels for testing.

    Returns:
        float: Accuracy score of the model on the test set.
    """
    predictions = model.predict(test_features)
    acc = accuracy_score(test_labels, predictions)
    return acc

@job
def rf_training_pipeline():
    """
    Dagster job to orchestrate the loading of data, training of the model,
    and evaluation of the model's performance.
    """
    # Unpack the split data
    train_features, test_features, train_labels, test_labels = load_data()

    # Train the model
    model = train_model(train_features, train_labels)

    # Evaluate the model's accuracy
    accuracy = evaluate_model(model, test_features, test_labels)
    with open('metrics.txt', 'w') as f:
        f.write(f'Accuracy: {accuracy}\n')
