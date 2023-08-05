from sklearn.tree import DecisionTreeClassifier


class DecisionTreeRegressor:

    def Decision_tree_regression(self, data):
        try:
            user_data = data['user_data']
            # user_data = user_data.drop(['AcquistionCost'], axis=1)
            X_train, X_test, Y_train, Y_test = data['X_train'], data['X_test'], data['Y_train'], data['Y_test']

            # Fitting the decision tree regression
            # regressor = DecisionTreeRegressor()
            classifier = DecisionTreeClassifier()
            classifier.fit(X_train, Y_train)

            # predict new acv
            prediction = classifier.predict(user_data)
            # accuracy or score
            accuracy = classifier.score(X_test, Y_test)
            print("Decision Tree")
            return accuracy, prediction

        except Exception as err:
            print(err)
