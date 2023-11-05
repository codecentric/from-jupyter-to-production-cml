import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay

# read in data
X_train = np.genfromtxt("data/train_features.csv")
y_train = np.genfromtxt("data/train_labels.csv")
X_test = np.genfromtxt("data/test_features.csv")
y_test = np.genfromtxt("data/test_labels.csv")


# fit a model
depth = 2
clf = RandomForestClassifier(max_depth=depth)
clf.fit(X_train, y_train)

acc = clf.score(X_test, y_test)
print(acc)
with open("metrics.txt", "w") as outfile:
    outfile.write(f"Accuracy: {acc}")

y_pred = clf.predict(X_test)
# plot it
display = ConfusionMatrixDisplay.from_predictions(y_test,y_pred)
display.plot()
plt.savefig("confusion_matrix.png")
