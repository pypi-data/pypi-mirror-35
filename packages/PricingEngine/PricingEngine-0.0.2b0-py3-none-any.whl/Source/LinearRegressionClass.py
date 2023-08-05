from sklearn.model_selection import train_test_split
import numpy as np
import sys
import pandas as pd
from sklearn.metrics import accuracy_score
from Logger.log_helper import LogHelper as lhelper
from sklearn import linear_model
import seaborn as sns
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

class LinearRegressionClass:
    def regression_acv_mileage(self, train_X, train_y, test_X, test_y, pricing_data, acv, mileage):
        try:
            sns.jointplot(x=acv, y=mileage, data=pricing_data, kind='reg')
            cls = linear_model.LinearRegression()
            cls.fit(train_X, train_y)
            prediction = cls.predict(test_X)
            cls.get_params()
            print('Co-efficient of linear regression', cls.coef_)
            print('Intercept of linear regression model', cls.intercept_)
            print('Mean Square Error', metrics.mean_squared_error(test_y, prediction))
            print('Model R^2 Square value', metrics.r2_score(test_y, prediction))
            plt.scatter(test_X, test_y)
            plt.plot(test_X, prediction, color='red', linewidth=3)
            plt.xlabel('acv')
            plt.ylabel('mileage')
            plt.title('Linear Regression acv & mileage')
            plt.show()

            # fit a model
            lm = linear_model.LinearRegression()
            model = lm.fit(train_X, train_y)
            predictions = lm.predict(train_X)
            plt.scatter(train_y, predictions)
            plt.xlabel("True Values")
            plt.ylabel("Predictions")
            plt.title('acv & mileage')
            plt.show()

            print("Score :", model.score(train_X, train_y))

        except Exception as err:
            lhelper.getlogger().error(err)

    def regression_Addrzip_acv(self, train_X, train_y, test_X, test_y, pricing_data, acv, Addrzip):
        try:
            sns.jointplot(x=acv, y=Addrzip, data=pricing_data,  kind='reg')
            cls = linear_model.LinearRegression()
            cls.fit(train_X, train_y)
            prediction = cls.predict(test_X)
            cls.get_params()
            print('Co-efficient of linear regression', cls.coef_)
            print('Intercept of linear regression model', cls.intercept_)
            print('Mean Square Error', metrics.mean_squared_error(test_y, prediction))
            print('Model R^2 Square value', metrics.r2_score(test_y, prediction))
            plt.scatter(test_X, test_y)
            plt.plot(test_X, prediction, color='red', linewidth=3)
            plt.xlabel('acv')
            plt.ylabel('Zip code')
            plt.title('Linear Regression ACV & Zip Code')
            plt.show()

            # fit a model
            lm = linear_model.LinearRegression()
            model = lm.fit(train_X, train_y)
            predictions = lm.predict(train_X)
            plt.scatter(train_y, predictions)
            plt.xlabel("True Values")
            plt.ylabel("Predictions")
            plt.title('ACV & Zip Code')
            plt.show()
            print("Score :", model.score(train_X, train_y))

        except Exception as err:
            lhelper.getlogger().error(err)

    def regression_color_acv(self, train_X, train_y, test_X, test_y, pricing_data, acv, _color, r_color):

        try:
            sns.jointplot(x=acv, y=_color, data=pricing_data, kind='reg')
            cls = linear_model.LinearRegression()
            cls.fit(train_X, train_y)
            prediction = cls.predict(test_X)
            cls.get_params()
            print('Co-efficient of linear regression', cls.coef_)
            print('Intercept of linear regression model', cls.intercept_)
            print('Mean Square Error', metrics.mean_squared_error(test_y, prediction))
            print('Model R^2 Square value', metrics.r2_score(test_y, prediction))
            plt.scatter(test_X, test_y)
            plt.plot(test_X, prediction, color='red', linewidth=3)
            plt.xlabel('acv')
            plt.ylabel('Colour')
            plt.yticks(_color, r_color)
            plt.title('Linear Regression ACV & Color')
            plt.show()

            # fit a model
            lm = linear_model.LinearRegression()
            model = lm.fit(train_X, train_y)
            predictions = lm.predict(train_X)
            plt.scatter(train_y, predictions)
            plt.xlabel("True Values")
            plt.ylabel("Predictions")
            plt.title('ACV & Color')
            plt.show()
            print("Score :", model.score(train_X, train_y))

        except Exception as err:
            lhelper.getlogger().error(err)

    def regression_year_acv(self, train_X, train_y, test_X, test_y, pricing_data, acv, year):
        try:
            sns.jointplot(x=acv, y=year, data=pricing_data,  kind='reg')
            cls = linear_model.LinearRegression()
            cls.fit(train_X, train_y)
            prediction = cls.predict(test_X)
            cls.get_params()
            print('Co-efficient of linear regression', cls.coef_)
            print('Intercept of linear regression model', cls.intercept_)
            print('Mean Square Error', metrics.mean_squared_error(test_y, prediction))
            print('Model R^2 Square value', metrics.r2_score(test_y, prediction))
            plt.scatter(test_X, test_y)
            plt.plot(test_X, prediction, color='red', linewidth=3)
            plt.xlabel('acv')
            plt.ylabel('Year')
            plt.title('Linear Regression ACV & Year')
            plt.show()

            # fit a model
            lm = linear_model.LinearRegression()
            model = lm.fit(test_X, test_y)
            predictions = lm.predict(test_X)
            plt.scatter(test_y, predictions)
            plt.xlabel("True Values")
            plt.ylabel("Predictions")
            plt.title('ACV & Year')
            plt.show()

        except Exception as err:
            lhelper.getlogger().error(err)

    def regression_acv_with_make_name(self, train_X, train_y, test_X, test_y,
                                                                 pricing_data, acv, r_make_name ,make_name):
        try:
            sns.jointplot(x=acv, y=make_name, data=pricing_data,  kind='reg')
            cls = linear_model.LinearRegression()
            cls.fit(train_X, train_y)
            prediction = cls.predict(test_X)
            cls.get_params()
            print('Co-efficient of linear regression', cls.coef_)
            print('Intercept of linear regression model', cls.intercept_)
            print('Mean Square Error', metrics.mean_squared_error(test_y, prediction))
            print('Model R^2 Square value', metrics.r2_score(test_y, prediction))
            plt.scatter(test_X, test_y)
            plt.plot(test_X, prediction, color='red', linewidth=3)
            plt.xlabel('acv')
            plt.ylabel('Make Name')
            plt.title('Linear Regression ACV & Make name')
            plt.yticks(r_make_name, make_name)
            plt.show()

            # fit a model
            lm = linear_model.LinearRegression()
            model = lm.fit(test_X, test_y)
            predictions = lm.predict(test_X)
            plt.scatter(test_y, predictions)
            plt.xlabel("True Values")
            plt.ylabel("Predictions")
            plt.title('ACV & make name')
            plt.show()

        except Exception as err:
            lhelper.getlogger().error(err)