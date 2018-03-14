import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.neighbors import NearestCentroid

n_neighbors = 5

naranja = [[5,5.5],[4.5,5],[5.2,4.9]]
toronja = [[6.5,6.8],[5.9,6],[5.7,5.5]]
data = np.array([[6.5,6.8],[5.9,6],[5.7,5.5],[5,5.5],[4.5,5],[5.2,4.9]])
dataType = np.array([0,0,0,1,1,1])

predict = np.array([[5.3,4],[6.8,5.9]])
#predict = np.array(arrayNaraja)
# import some data to play with
iris = datasets.load_iris()


# we only take the first two features. We could avoid this ugly
# slicing by using a two-dim dataset
X = data[:]

y = dataType[:]

h = .01  # step size in the mesh

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00'])

for shrinkage in [None, .2]:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = NearestCentroid(shrink_threshold=shrinkage)
    clf.fit(X, y)
    y_pred = clf.predict(predict)
    print(shrinkage, np.mean(y == y_pred))
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    x1_min, x1_max = predict[:, 0].min() - 1, predict[:, 0].max() + 1
    y1_min, y1_max = predict[:, 1].min() - 1, predict[:, 1].max() + 1

    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    xx1, yy1 = np.meshgrid(np.arange(x1_min, x1_max, h),
                         np.arange(y1_min, y1_max, h))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z1 = clf.predict(np.c_[xx1.ravel(), yy1.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    Z1 = Z1.reshape(xx1.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
    plt.pcolormesh(xx1, yy1, Z1, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold,
                edgecolor='b', s=20)
    plt.scatter(predict[:, 0], predict[:, 1], c=y_pred, cmap=cmap_bold,
                edgecolor='b', s=20)
    plt.title("3-Class classification (shrink_threshold=%r)"
              % shrinkage)
    plt.axis('tight')

plt.show()
