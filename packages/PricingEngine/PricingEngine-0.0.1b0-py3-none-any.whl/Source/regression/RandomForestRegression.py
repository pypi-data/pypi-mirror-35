from abc import abstractmethod

import pandas as pd
import numpy as np
from sklearn import cross_validation
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


class RandomForestRegression:
    @abstractmethod
    def random_forest_regression(self, data):
        user_data = data['user_data']
        # user_data = user_data.drop(['AcquistionCost'], axis=1)
        X_train, X_test, Y_train, Y_test = data['X_train'], data['X_test'], data['Y_train'], data['Y_test']
        # Fitting the random forest regression
        from sklearn.ensemble import RandomForestRegressor
        regressor = RandomForestRegressor(n_estimators=500, random_state=42)
        regressor.fit(X_train, Y_train)
        accuracy = regressor.score(X_test, Y_test)
        # predict new acv
        prediction = regressor.predict(user_data)
        # errors = abs(prediction - Y_test)
        # print('Errors :', errors)
        print("random Forest Regression")
        return accuracy, prediction

        # # visualising the random forest regression
        # plt.scatter(X_train, Y_train, color='red')
        # plt.plot(X_test, regressor.predict(X_test), color='blue')
        # plt.title('Random Forest Regression')
        # plt.xlabel('Millage')
        # plt.ylabel('ACV')
        # plt.show()
