import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


class PolynomialRegression:

    def polynomial_regression(self, dataset):
        try:
            X = dataset.iloc[:, :-1].values
            y = dataset.iloc[:, -1].values
            X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            regressor = LinearRegression(n_jobs=1)
            regressor.fit(X_train, Y_train)
            accuracy = regressor.score(X_train, Y_train)
            print("Accuracy: ", accuracy)
            # millage = X_train[:, 4:5]
            # mileage_test = X_test[:, 4:5]

            # Fitting Polynomial Regression
            from sklearn.preprocessing import PolynomialFeatures
            poly_reg = PolynomialFeatures(degree=2)
            x_poly = poly_reg.fit_transform(X_train)
            lin_reg_2 = LinearRegression()
            lin_reg_2.fit(x_poly, Y_train)
            plt.scatter(X_train[:, 4: 5], Y_train, color='red')
            plt.title('Polynomial Regression')
            plt.ylabel('ACV')
            plt.xlabel('Millage')
            plt.plot(X_train, lin_reg_2.predict(poly_reg.fit_transform(X_train)), color='blue')
            plt.show()

            plt.scatter(X_train[:, 5: 6], Y_train, color='green')
            plt.title('Polynomial Regression')
            plt.ylabel('ACV')
            plt.xlabel('Millage')
            plt.plot(X_train, lin_reg_2.predict(poly_reg.fit_transform(X_train)), color='blue')
            plt.show()

            plt.scatter(X_train[:, 6: 7], Y_train, color='black')
            plt.title('Polynomial Regression')
            plt.ylabel('ACV')
            plt.xlabel('Millage')
            plt.plot(X_train, lin_reg_2.predict(poly_reg.fit_transform(X_train)), color='blue')
            plt.show()

            print(lin_reg_2.predict(poly_reg.fit_transform(X_test)))
        except Exception as err:
            print(err)