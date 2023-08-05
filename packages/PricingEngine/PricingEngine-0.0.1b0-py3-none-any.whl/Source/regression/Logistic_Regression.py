import pandas as pd
from sklearn.metrics import accuracy_score

from Logger.log_helper import LogHelper as lhelper
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split


class Logistic_Regression:
    def logistic_regression(self, data):
        try:
            user_data = data['user_data']
            # user_data = user_data.drop(['AcquistionCost'], axis=1)
            X_train, X_test, Y_train, Y_test = data['X_train'], data['X_test'], data['Y_train'], data['Y_test']
            classifier = LogisticRegression(n_jobs=1)
            classifier.fit(X_train, Y_train)
            prediction = classifier.predict(user_data)
            accuracy = classifier.score(X_test, Y_test)
            # print(accuracy_score(Y_test, prediction))
            print("Logistic regression")
            return accuracy, prediction
        except Exception as err:
            lhelper.getlogger().error(err)
