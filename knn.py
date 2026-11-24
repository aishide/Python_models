from sklearn.neighbours import KNeighboursClassifier 

#Features [age , salary in thousands] , tager 0 = not buy and 1= buy 
x = [[22, 20], [25,25], [45, 80], [50,90]]
y = [0, 0, 1, 1]

knn = KNeighboursClassifier(n_neighbours = 3)
knn.fit(x, y)

print("The predicted value of [28,30] is : " , knn.predict([[28,30]]))
