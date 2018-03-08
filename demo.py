from sklearn import tree

X = [[181,80,44], [142, 40, 40]]

Y = ['male', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[160, 70, 43]])

print(prediction)