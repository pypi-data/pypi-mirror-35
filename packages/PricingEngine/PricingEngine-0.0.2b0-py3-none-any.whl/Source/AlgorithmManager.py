from Logger.log_helper import LogHelper as lhelper
from Source.AlgoList import AlgoList
from Source.regression.LinearRegressionClass import LinearRegressionClass
from Source.regression.DecisionTreeRegressor import DecisionTreeRegressor
from Source.regression.RandomForestRegression import RandomForestRegression
from Source.regression.Logistic_Regression import Logistic_Regression
from Source.regression.GradientBoosting import Gradient_Boosting_Regression
from Source.regression.K_Neighbors_Regression import K_Neighbors_Regression


class AlgorithmManager:
    try:
        def __init__(self, data):
            self.data = data
            super(AlgorithmManager, self).__init__()
            self.algo_name.get(data['algo'])(self)

        def linear_regression(self):
            linear_reg = LinearRegressionClass()
            accuracy, prediction = linear_reg.linear_regression(self.data)
            print('Accuracy :', accuracy, 'prediction :', prediction)

        def random_forest_regression(self):
            random_forest_regr = RandomForestRegression()
            accuracy, prediction = random_forest_regr.random_forest_regression(self.data)
            print('Accuracy :', accuracy, 'prediction :', prediction)

        def decision_tree_regression(self):
            decision_tree = DecisionTreeRegressor()
            accuracy, prediction = decision_tree.Decision_tree_regression(self.data)
            print('Accuracy :', accuracy, 'prediction :', prediction)

        def logistic_regression(self):
            logistic_regression = Logistic_Regression()
            accuracy, prediction = logistic_regression.logistic_regression(self.data)
            print('Accuracy :', accuracy, 'prediction :', prediction)

        def gradient_boosting_regression(self):
            gradient_boosting = Gradient_Boosting_Regression()
            accuracy, prediction = gradient_boosting.gradient_boosting_regression(self.data)
            print('Accuracy :', accuracy, 'prediction :', prediction)

        def k_neighbors(self):
            k_neighbors_reg = K_Neighbors_Regression()
            accuracy, prediction = k_neighbors_reg.k_neighbors_regressor(self.data)
            print('Accuracy :', accuracy, 'prediction :', prediction)

        algo_name = {
            # if you will do any changes in there then you need to change in AlgoList.py also
            'linear_regression': linear_regression,
            'random_forest_regression': random_forest_regression,
            'decision_tree_regression': decision_tree_regression,
            'logistic_regression': logistic_regression,
            'gradient_boosting_regression': gradient_boosting_regression,
            'k_neighbors': k_neighbors
        }

    except Exception as err:
        lhelper.getlogger().error(err)
