import configparser

import pymysql
from pymysql import InternalError

from Logger.log_helper import LogHelper as LHelper


class DBHelper:

    def __init__(self):
        print("Init DB Helper")

    @staticmethod
    def getconnection():
        try:
            config = configparser.RawConfigParser()
            config.read('Configuration/Config.properties')
            conn = pymysql.connect(user=config.get('DatabaseSection', 'databaseUser'),
                                   password=config.get('DatabaseSection', 'databasePwd'),
                                   host=config.get('DatabaseSection', 'databaseHost'),
                                   database=config.get('DatabaseSection', 'databaseName'))
            return conn
        except pymysql.Error as err:
            if err.errno == InternalError.ER_ACCESS_DENIED_ERROR:
                LHelper.getlogger().error("Wrong password or User Name")
            elif err.errno == InternalError.ER_BAD_DB_ERROR:
                LHelper.getlogger().error("Database does not exist")

            else:
                LHelper.getlogger().error(err)
        except IOError as errorNo:
            LHelper.getlogger().error("I/O error({0}): {1}".format(errorNo))
