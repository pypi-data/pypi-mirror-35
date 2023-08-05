import logging


class LogHelper:

    def __init__(self):
        print("Init")

    @staticmethod
    def getlogger():
        try:
            logger = logging.getLogger('pricingEngine')
            handler = logging.FileHandler('Logger/pricingEngine.log')
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s  Mathod Name:- %(funcName)20s() :%(lineno)s  File Path: %(pathname)s ')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.WARNING)
            return logger
        except IOError as errorNo:
            print("I/O error({0}): {1}".format(errorNo))
