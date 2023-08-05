from Source.PricingEngineDataPreprocessing import PricingEngineDataPreProcessing
from Source.pricing_data_reader import PricingDataReader
import pandas as pd
from Source.SplittingTrainingSet import SplittingTrainingSet
from Source.AlgoList import AlgoList
from Logger.log_helper import LogHelper as lhelper
from sklearn.preprocessing import normalize
from Utilities.sqlQuery import sqlQuery
import warnings

try:
    # remove warning
    warnings.filterwarnings("ignore")

    pricingEngine = PricingEngineDataPreProcessing()
    pricereader = PricingDataReader()
    # geting data from database using class pricereder
    data = pricereader.readRawdata(sqlQuery.sql_query.get('sql_query'))
    data = pricingEngine.datamaniputation(data)
    # split data in train and test it will return x1,y1,x2,y2
    train_data_ = SplittingTrainingSet()
    X_train, X_test, Y_train, Y_test = train_data_.train_data(data)
    user_data = {
        'Mileage': [49355],
        # 'AcquistionCost': [13500],
        'Color': ['White'],
        'Year': [2013],
        'MakeName': ['Mercedes-Benz'],
        'ModelName': ['C-Class'],
        'StyleName': ['C 250 Sport 4dr Sedan'],
        'AddrZip': ['90015']}

    user_data1 = {
        'Mileage': [64918],
        # 'AcquistionCost': [6000],
        'Color': ['Champagne'],
        'Year': [2010],
        'MakeName': ['Volkswagen'],
        'ModelName': ['Eos'],
        'StyleName': ['Komfort 2dr Convertible 6A'],
        'AddrZip': ['92806']}
    user_data2 = {
        'Mileage': [40742],
        # 'AcquistionCost': [12076],
        'Color': ['Silver'],
        'Year': [2016],
        'MakeName': ['Hyundai'],
        'ModelName': ['Veloster'],
        'StyleName': ['3dr Cpe Auto'],
        'AddrZip': ['92806']}

    def run_test(user_data):
        user_data = pd.DataFrame(data=user_data)
        user_data = pricingEngine.user_data_label_encode(user_data)
        user_data = normalize(user_data, norm='max')
        # user_data1 = pd.DataFrame(data=self.user_data1)
        # user_data1 = pricingEngine.user_data_label_encode(user_data1)
        # user_data1 = normalize(user_data1, norm='max')
        for i in range(7):
            pricingEngine.PricingEngine(X_train, X_test, Y_train, Y_test, user_data, AlgoList.algo_list.get(i+1))
            # pricingEngine.PricingEngine(X_train, X_test, Y_train, Y_test, user_data1, AlgoList.algo_list.get(i+1))

    run_test(user_data)

    # user_data = pd.DataFrame(data=user_data2)
    # user_data = pricingEngine.user_data_label_encode(user_data)
    # user_data = normalize(user_data, norm='max')
    # pricingEngine.PricingEngine(X_train, X_test, Y_train, Y_test, user_data, AlgoList.algo_list.get(6))
except Exception as err:
    lhelper.getlogger().error(err)