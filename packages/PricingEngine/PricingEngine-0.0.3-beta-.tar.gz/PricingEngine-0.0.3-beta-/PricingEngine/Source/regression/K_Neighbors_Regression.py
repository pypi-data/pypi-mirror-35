from sklearn import neighbors
from Logger.log_helper import LogHelper as lhelper
from sklearn.model_selection import train_test_split
import requests
import pandas as pd
import csv
# for data visualisation and statistical analysis
import numpy as np
import seaborn as sns
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from pylab import rcParams

sns.set_style("white")

class K_Neighbors_Regression:

    def k_neighbors_regressor(self, data):
        try:
            user_data = data['user_data']
            # user_data = user_data.drop(['AcquistionCost'], axis=1)
            X_train, X_test, Y_train, Y_test = data['X_train'], data['X_test'], data['Y_train'], data['Y_test']
            # the value of n_neighbors will be changed when we plot the histogram showing the lowest RMSE value
            knn = neighbors.KNeighborsRegressor(n_neighbors=20)
            knn.fit(X_train, Y_train)
            predicted = knn.predict(user_data)
            accuracy = knn.score(X_test, Y_test)
            print("K Neighbors Regression")
            # from sklearn.metrics import mean_squared_error
            # rmse = np.sqrt(mean_squared_error(Y_test, predicted))
            # print('RMSE:')
            # print(rmse)
            return accuracy, predicted
            #
            # fig = plt.figure(figsize=(30, 30))
            # ax1 = plt.subplot(211)
            # sns.distplot(residual, color='teal')
            # plt.tick_params(axis='both', which='major', labelsize=20)
            # plt.title('Residual counts', fontsize=35)
            # plt.xlabel('Residual', fontsize=25)
            # plt.ylabel('Count', fontsize=25)
            #
            # ax2 = plt.subplot(212)
            # plt.scatter(predicted, residual, color='teal')
            # plt.tick_params(axis='both', which='major', labelsize=20)
            # plt.xlabel('Predicted', fontsize=25)
            # plt.ylabel('Residual', fontsize=25)
            # plt.axhline(y=0)
            # plt.title('Residual vs. Predicted', fontsize=35)
            #
            # plt.show()

            from sklearn.metrics import mean_squared_error
            rmse = np.sqrt(mean_squared_error(Y_test, predicted))
            print('RMSE:')
            print(rmse)
            return 0, 0

        except Exception as err:
            lhelper.getlogger().error(err)
