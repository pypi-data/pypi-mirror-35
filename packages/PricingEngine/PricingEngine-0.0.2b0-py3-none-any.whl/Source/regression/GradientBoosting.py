# import pandas as pd
# from sklearn.metrics import mean_squared_error
# import numpy as np
from Logger.log_helper import LogHelper as lhelper
from sklearn.ensemble import GradientBoostingRegressor


# from sklearn.model_selection import cross_val_score
# import matplotlib as plt
# import seaborn as sns


class Gradient_Boosting_Regression:
    def gradient_boosting_regression(self, data):
        try:
            user_data = data['user_data']
            # user_data = user_data.drop(['AcquistionCost'], axis=1)
            X_train, X_test, Y_train, Y_test = data['X_train'], data['X_test'], data['Y_train'], data['Y_test']
            gbr = GradientBoostingRegressor(learning_rate=0.21)
            # gbr = GradientBoostingRegressor(loss='huber', max_depth=3, learning_rate=0.1, n_estimators=100,
            #                                             criterion='mae')
            gbr.fit(X_train, Y_train)
            predicted = gbr.predict(user_data)
            accuracy = gbr.score(X_test, Y_test)
            print("Gradient Boosting Algorithm")
            return accuracy, predicted
        except Exception as err:
            lhelper.getlogger().error(err)
