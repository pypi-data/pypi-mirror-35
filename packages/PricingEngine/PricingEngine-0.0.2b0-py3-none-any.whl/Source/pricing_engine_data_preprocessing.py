# Import the libraries

from Logger.log_helper import LogHelper as lhelper
from Source.pricing_data_reader import PricingDataReader
from sklearn import cross_validation
# # Import the dataset

class PricingEngineDataPreProcessing:

    def PricingEngine(self):
        pricereader = PricingDataReader()
        pricing_data = self.datamaniputation(pricereader.readRawdata())
        from Source.regression.DecisionTreeRegressor import DecisionTreeRegressor
        poly_reg = DecisionTreeRegressor()
        poly_reg.Decision_tree_regression(pricing_data)
        print("Total result in DB are:{}".format(len(pricing_data)))
        try:

            X = pricing_data.iloc[:, :-1].values
            y = pricing_data.iloc[:, -1].values
            X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)
            # regressor = LinearRegression(n_jobs=-1)
            # regressor.fit(X_train, Y_train)
            # accuracy = regressor.score(X_test, Y_test)
            # print("Accuracy: ", accuracy)


            # drawgraph = DrawGraph()
            # splittingTrainingSet = SplittingTrainingSet()
            #
            # drawgraph.acv_with_mileage(acv, mileage)
            # splittingTrainingSet.splite_data_mileage_acv(acv, mileage, pricing_data)
            #
            # drawgraph.acv_with_addrzip(acv, addrzip)
            # splittingTrainingSet.splite_data_Addrzip_acv(acv, addrzip, pricing_data)
            #
            # drawgraph.acv_with_color(acv, color ,r_color)
            # splittingTrainingSet.splite_data_acv_color(acv, color, r_color, pricing_data)
            #
            # drawgraph.acv_with_year(acv, year)
            # splittingTrainingSet.splite_data_acv_year(acv, year, pricing_data)
            #
            # drawgraph.acv_with_make_name(acv, make_name)
            # splittingTrainingSet.splite_acv_with_make_name(acv, make_name, r_make_name,pricing_data)
            #
            # drawgraph.acv_with_model_name(acv, model_name)
            # drawgraph.makename(make_name)
            # Splitting the dataset into the training set and test set
        except Exception as err:
            lhelper.getlogger().error(err)


        #
        # zipcode = np.asarray(pricing_data.iloc[:, -1].values)
        # # acvzip = {}
        # # k=0
        # # for i in range(len(acv)):
        # #     acvzip[k]=[acv[i],int(zipcode[i])]
        # #     k=k+1
        # # sorted(acvzip)
        # # print(acvzip)
        # # zipcode = np.asarray(zipcode.astype(str).astype(int))
        # # zipcode = np.log10(np.abs(zipcode))
        #

        #
        # plt.rcdefaults()
        # objects = mileage
        # y_pos = np.arange(len(objects))
        # performance = acv
        # plt.bar(y_pos, performance, align='center', alpha=0.5)
        # plt.xticks(y_pos, objects)
        # plt.ylabel('Usage')
        # plt.title('Programming language usage')
        # plt.show()

        # rng = np.random.RandomState(mileage)  # deterministic random data
        # a = np.hstack((rng.normal(size=1000), rng.normal(acv)))
        # plt.hist(a, bins='auto')  # arguments are passed to np.histogram
        # plt.title("Histogram with 'auto' bins")
        # plt.show()
        # print(acv, mileage, year)
        # print(np.unique(X), np.unique(mileage))
        # plt.hist(X, np.unique(mileage))
        #

        # imputer = Imputer(missing_values="NaN", strategy='mean', axis=0)
        # imputer = imputer.fit(mileage[:, 0:1])
        # mileage[:, 0:1] = imputer.transform(mileage[:, 0:1])
        # print(mileage[:, 0:1])
        # color = pricing_data.iloc[:, 5:6].values
        #
        # # plt.hist(np.unique(acv[:, :]), (addrZip[:, :]))
        # # plt.show()
        # # print(acv.min(), acv.max(), mileage.min(), mileage.max())
        # xMin = acv.min()
        # xMax = acv.max()
        # yMin = mileage.min()
        # yMax = mileage.max()

        # Taking care of missing data
        # imputer = Imputer(missing_values=0, strategy='mean', axis=0)
        # imputer = imputer.fit(X[:, 0:1])
        # X[:, 0:1] = imputer.transform(X[:, 0:1])
        # print(X,y)
        # # Encoding categorical data
        # labelencoder_X = LabelEncoder()
        # X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
        # onehotencoder = OneHotEncoder(categorical_features=[0])
        # X = onehotencoder.fit_transform(X).toarray()
        # labelencoder_y = LabelEncoder()
        # y = labelencoder_y.fit_transform(y)
        #
        # # Splitting the dataset into the training set and test set
        #
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        #
        # # Feature scaling
        #
        # sc_X = StandardScaler()
        # X_train = sc_X.fit_transform(X_train)
        # X_test = sc_X.transform(X_test)
        # # print(X_train , X_test)

    def datamaniputation(self,pricing_data):
        try:
            pricing_data.dropna(inplace=True)
            from sklearn.preprocessing import LabelEncoder, OneHotEncoder
            label_encoder = LabelEncoder()
            pricing_data = pricing_data[pricing_data['Mileage'] > 10000]
            pricing_data = pricing_data[pricing_data['AcquistionCost'] > 300]
            pricing_data['VIN'] = label_encoder.fit_transform(pricing_data['VIN'])
            pricing_data['Color'] = label_encoder.fit_transform(pricing_data['Color'])
            pricing_data['ModelName'] = label_encoder.fit_transform(pricing_data['ModelName'])
            pricing_data['MakeName'] = label_encoder.fit_transform(pricing_data['MakeName'])
            pricing_data['Mileage'] = label_encoder.fit_transform(pricing_data['Mileage'])
            pricing_data['StyleName'] = label_encoder.fit_transform(pricing_data['StyleName'])
            pricing_data['GroupName'] = label_encoder.fit_transform(pricing_data['GroupName'])
            pricing_data['CustomerDisplayName'] = label_encoder.fit_transform(pricing_data['CustomerDisplayName'])
            pricing_data['AcquiredOn'] = label_encoder.fit_transform(pricing_data['AcquiredOn'])
            pricing_data['AddrZip'] = label_encoder.fit_transform(pricing_data['AddrZip'])
            return pricing_data

        except Exception as err:
              lhelper.getlogger().error(err)

