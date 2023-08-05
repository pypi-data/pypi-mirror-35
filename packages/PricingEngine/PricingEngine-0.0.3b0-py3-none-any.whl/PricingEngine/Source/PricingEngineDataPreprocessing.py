# Import the libraries
from difflib import get_close_matches
from Logger.log_helper import LogHelper as lhelper
from Source.get_prediction import get_prediction
# from Source.pricing_data_reader import PricingDataReader
# import numpy as np
import pandas as pd



# # Import the dataset


class PricingEngineDataPreProcessing:

    # In filter have parameters who user needs
    def PricingEngine(self, X_train, X_test, Y_train, Y_test, user_data, algo):
        try:

            # print(user_data)
            data = {'X_train': X_train, 'X_test': X_test, 'Y_train': Y_train, 'Y_test': Y_test,
                    'user_data': user_data, 'algo': algo}
            get_prediction_ = get_prediction(data)
            get_prediction_.algo()
        except Exception as err:
            lhelper.getlogger().error(err)

    # Data filtering
    def datamaniputation(self, pricing_data):
        try:
            pricing_data.dropna(inplace=True)
            pricing_data = pd.DataFrame(data=pricing_data)
            from sklearn.preprocessing import LabelEncoder, LabelBinarizer
            label_encoder = LabelEncoder()
            temp_col = pricing_data.loc[:, 'Color']
            pricing_data.loc[:, 'Color'] = label_encoder.fit_transform(pricing_data.loc[:, 'Color'])
            self.Color = dict(zip(temp_col, pricing_data.loc[:, 'Color']))

            temp_col = pricing_data.loc[:, 'ModelName']
            pricing_data.loc[:, 'ModelName'] = label_encoder.fit_transform(pricing_data.loc[:, 'ModelName'])
            self.ModelName = dict(zip(temp_col, pricing_data.loc[:, 'ModelName']))

            temp_col = pricing_data.loc[:, 'MakeName']
            pricing_data.loc[:, 'MakeName'] = label_encoder.fit_transform(pricing_data.loc[:, 'MakeName'])
            self.MakeName = dict(zip(temp_col, pricing_data.loc[:, 'MakeName']))

            temp_col = pricing_data.loc[:, 'AddrZip']
            pricing_data.loc[:, 'AddrZip'] = label_encoder.fit_transform(pricing_data.loc[:, 'AddrZip'])
            self.AddrZip = dict(zip(temp_col, pricing_data.loc[:, 'AddrZip']))

            temp_col = pricing_data.loc[:, 'StyleName']
            pricing_data.loc[:, 'StyleName'] = label_encoder.fit_transform(pricing_data.loc[:, 'StyleName'])
            self.StyleName = dict(zip(temp_col, pricing_data.loc[:, 'StyleName']))

            return pricing_data

        except Exception as err:
            lhelper.getlogger().error(err)

    # userdata encode respect to corresponding value
    def user_data_label_encode(self, data):
        try:

            if self.StyleName.get(data['StyleName'].values[0]) is None:
                closer_style = get_close_matches(data['StyleName'].values[0], self.StyleName)
                data['StyleName'] = self.StyleName.get(closer_style[0])
            else:
                data['StyleName'] = self.StyleName.get(data['StyleName'].values[0])

            if self.Color.get(data['Color'].values[0]) is None:
                closer_style = get_close_matches(data['Color'].values[0], self.Color)
                data['Color'] = self.Color.get(closer_style[0])
            else:
                data['Color'] = self.Color.get(data['Color'].values[0])

            if self.ModelName.get(data['ModelName'].values[0]) is None:
                closer_style = get_close_matches(data['ModelName'].values[0], self.ModelName)
                data['ModelName'] = self.ModelName.get(closer_style[0])
            else:
                data['ModelName'] = self.ModelName.get(data['ModelName'].values[0])

            if self.MakeName.get(data['MakeName'].values[0]) is None:
                closer_style = get_close_matches(data['MakeName'].values[0], self.MakeName)
                data['MakeName'] = self.MakeName.get(closer_style[0])
            else:
                data['MakeName'] = self.MakeName.get(data['MakeName'].values[0])

            if self.AddrZip.get(data['AddrZip'].values[0]) is None:
                closer_style = get_close_matches(data['AddrZip'].values[0], self.AddrZip)
                data['AddrZip'] = self.AddrZip.get(closer_style[0])
            else:
                data['AddrZip'] = self.AddrZip.get(data['AddrZip'].values[0])

            return data
        except Exception as err:
            lhelper.getlogger().error(err)
