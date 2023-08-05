from sklearn.preprocessing import normalize
# import numpy as np
# import pandas as pd
# from Source.regression.LinearRegressionClass import LinearRegressionClass
from sklearn.model_selection import train_test_split
from Logger.log_helper import LogHelper as lhelper


# split data in to part train have 80% data and test have 20% of whole data
class SplittingTrainingSet:
    def train_data(self, data):
        try:
            # n = int(len(data) * 0.2)
            # train = data.iloc[n:, :]
            # test = data.iloc[:n, :]
            # y_train = train.loc[:, 'AcquistionCost']
            # x_train = train.drop(['AcquistionCost'], axis=1)
            # y_test = test.loc[:, 'AcquistionCost']
            # x_test = test.drop(['AcquistionCost'], axis=1)
            x_train, x_test, y_train, y_test = train_test_split(data.drop(['AcquistionCost'], axis=1),
                                                data.loc[:, 'AcquistionCost'], test_size=0.1, random_state=42)
            # normalize data train and test
            x_train = normalize(x_train, norm='max')
            x_test = normalize(x_test, norm='max')
            return x_train, x_test, y_train, y_test
        except Exception as err:
            lhelper.getlogger().error(err)