import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from matplotlib import pyplot as plt

'''
X = pd.read_csv('1.csv')

kmeans = KMeans(n_clusters = 2, random_state = 0).fit(X)

plt.figure(figsize=(10,10))
plt.scatter(X.a0, X.a1, c = X["class"])

plt.figure(figsize = (10,10))
plt.scatter(X.a0, X.a1, c = kmeans.labels_)
plt.show()
'''

'''
X = pd.read_csv('2.csv', index_col = None)

kmeans = KMeans(n_clusters = 4, random_state = 0).fit(X)

plt.figure(figsize=(10,10))
plt.scatter(X.x, X.y, c = X["class"])

plt.figure(figsize = (10,10))
plt.scatter(X.x, X.y, c = kmeans.labels_)
plt.show()
'''

'''
X = pd.read_csv('3.csv', index_col = None)

kmeans = KMeans(n_clusters = 3, random_state = 0).fit(X)

plt.figure(figsize=(10,10))
plt.scatter(X.x, X.y, c = X["class"])

plt.figure(figsize = (10,10))
plt.scatter(X.x, X.y, c = kmeans.labels_)
plt.show()
'''

'''
X = pd.read_csv('4.csv', index_col = None)

kmeans = KMeans(n_clusters = 3, random_state = 0).fit(X)

plt.figure(figsize=(10,10))
plt.scatter(X.x, X.y, c = X["class"])

plt.figure(figsize = (10,10))
plt.scatter(X.x, X.y, c = kmeans.labels_)
plt.show()
'''

'''
X = pd.read_csv('5.csv', index_col = None)

kmeans = KMeans(n_clusters = 4, random_state = 0).fit(X)

plt.figure(figsize=(10,10))
plt.scatter(X.a0, X.a1, c = X["class"])

plt.figure(figsize = (10,10))
plt.scatter(X.a0, X.a1, c = kmeans.labels_)
plt.show()
'''


X = pd.read_csv('6.csv', index_col = None)

kmeans = KMeans(n_clusters = 3, random_state = 0).fit(X)

plt.figure(figsize=(10,10))
plt.scatter(X.iloc[:, [1]], X.iloc[:, [2]], c = X.iloc[:, [3]])

plt.figure(figsize = (10,10))
plt.scatter(X.iloc[:, [1]], X.iloc[:, [2]], c = kmeans.labels_)
plt.show()

