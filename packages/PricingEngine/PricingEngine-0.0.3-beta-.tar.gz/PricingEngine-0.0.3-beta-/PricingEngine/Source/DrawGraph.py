import matplotlib.pyplot as plt
import numpy as np
from Logger.log_helper import LogHelper as lhelper
import collections


class DrawGraph:
    def acv_with_mileage(self, acv, mileage):
        try:
            plt.scatter(acv / 1000, mileage / 1000, label="line")
            plt.title("ACV with Mileage")
            plt.ylabel("mileage(multiple of 1000)")
            plt.xlabel("ACV (multiple of 1000)")
            plt.show()
        except Exception as err:
            lhelper.getlogger().error(err)

    def acv_with_addrzip(self, acv, zip):
        try:
            plt.scatter( acv/100, zip, label="line")
            plt.title("Zip code with ACV")
            plt.ylabel("Zip code")
            plt.xlabel("ACV(Multiple of 100)")
            plt.show()
        except Exception as err:
            lhelper.getlogger().error(err)

    def acv_with_year(self, acv, year):
        try:
            plt.scatter(year, acv)
            plt.title("ACV with Year")
            plt.ylabel("ACV")
            plt.xlabel("Year")
            plt.show()
        except Exception as err:
            lhelper.getlogger().error(err)

    def acv_with_make_name(self, acv, MakeName):
        try:
            plt.figure(figsize=(6, 10))
            plt.scatter(acv/1000, MakeName,)
            plt.title("ACV with Make Name")
            plt.xlabel("ACV(Multiple of 1000)")
            plt.ylabel("Make Name")
            plt.show()
        except Exception as err:
            lhelper.getlogger().error(err)

    def acv_with_model_name(self, acv, model_name):
        try:
            plt.figure(figsize=(20, 70))
            plt.margins = 2
            plt.scatter(acv/1000, model_name,)
            plt.title("ACV with Model Name")
            plt.xlabel("ACV(Multiple of 1000)")
            plt.ylabel("Model Name")
            plt.show()

        except Exception as err:
            lhelper.getlogger().error(err)

    def acv_with_color(self, acv, color, r_color):
        try:
            plt.figure(figsize=(6, 10))
            plt.scatter(acv / 1000, color)
            plt.title("ACV with Color")
            plt.xlabel("ACV(Multiple of 1000)")
            plt.ylabel("Color")
            plt.subplots_adjust(left=0.2, bottom=0.2)
            plt.yticks(color, r_color, step=0.2)
            plt.show()
        except Exception as err:
            lhelper.getlogger().error(err)

    def makename(self, makename):
        try:
            make_name = collections.Counter(makename)
            plt.figure(figsize=(6, 10))
            plt.scatter(make_name.values(), make_name.keys(), label='bar')
            plt.title("Make Name and Number of car")
            plt.xlabel("Number of car")
            plt.ylabel("Model name")
            plt.show()
        except Exception as err:
            lhelper.getlogger().error(err)
