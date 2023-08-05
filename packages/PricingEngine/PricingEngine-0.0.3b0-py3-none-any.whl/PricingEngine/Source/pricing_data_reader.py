import pandas as pd
import pymysql

from Logger.log_helper import LogHelper as lhelper
from Utilities.db_helper import DBHelper as dbhelper


class PricingDataReader:
    def __init__(self):
        print("Init Pricing Data Reader")

    # def readTestData(self):
    #     print("Read Test Data")
    #
    # def readTrainingData(self):
    #     print("Read Training Data")
    #
    # def readValidationData(self):
    #     print("Read Validation Data")

    def readRawdata(self, sqlquery):
        # Open database connection
        con = dbhelper.getconnection()
        # prepare a cursor object using cursor() method
        # cursor = con.cursor()
        # Prepare SQL query to get Car information from database.
        # statement = """select cfv.fvid, cfv.FileNum, av.VIN, cfv.VehicleID, cfv.Mileage, cfv.Color, cfv.MMRAvgValue,
        # cfv.AcquiredOn,cfv.AcquiredBy, cfv.AcquiredFromLocation, cfv.AcquistionCost, cfv.CarFax, ac.CustomerDisplayName,
        # if(Customername = ac.customerid in (select customerid from cfgserviceplan), 'Internal', 'External')
        # As GroupName, av.`Year`,msmake.MakeName , msmodel.ModelName , msstyle.StyleName, msa.AddrZip
        # from ((cfgfilevehicle cfv
        # left join appvehicle av on cfv.VehicleID = av.VehicleID)
        # left join cfgcustomerlocation ccl on ccl.clid = cfv.acquiredfromlocation
        # left join msaddress msa on msa.AddrId = ccl.AddrId) , msmake, msmodel, msstyle, appcustomer ac
        # where cfv.VehicleID = av.VehicleID and av.MakeId=msmake.MakeId and av.ModelId=msmodel.ModelId and cfv.AcquistionCost<30000 and  cfv.AcquistionCost>200 and cfv.Mileage > 1000 and msa.AddrZip!='' and
        # cfv.Mileage<999999 and av.StyleId=msstyle.StyleId and ccl.clid = cfv.AcquiredFromLocation and  ac.CustomerId = ccl.Customerid  group by av.VIN order by msa.Addrzip asc """ #group by msa.AddrZip asc

        # train ="""select cfv.fvid, cfv.FileNum, av.VIN, cfv.VehicleID, cfv.Mileage, cfv.Color,
        # cfv.AcquiredOn,cfv.AcquiredBy, cfv.AcquiredFromLocation, cfv.AcquistionCost, ac.CustomerDisplayName,
        # if(Customername = ac.customerid in (select customerid from cfgserviceplan), 'Internal', 'External')
        # As GroupName, av.Year,msmake.MakeName , msmodel.ModelName , msstyle.StyleName, msa.AddrZip
        # from ((cfgfilevehicle cfv
        # left join appvehicle av on cfv.VehicleID = av.VehicleID)
        # left join cfgcustomerlocation ccl on ccl.clid = cfv.acquiredfromlocation
        # left join msaddress msa on msa.AddrId = ccl.AddrId) , msmake, msmodel, msstyle, appcustomer ac
        # where cfv.VehicleID = av.VehicleID and av.MakeId=msmake.MakeId and av.ModelId=msmodel.ModelId and
        #  msstyle.StyleName!='' and msa.AddrZip!=' '
        # and av.StyleId=msstyle.StyleId and ccl.clid = cfv.AcquiredFromLocation and  ac.CustomerId = ccl.Customerid
        # group by av.VIN order by (msa.AddrZip) asc limit 6001,10000"""
        #
        # test = """select cfv.fvid, cfv.FileNum, av.VIN, cfv.VehicleID, cfv.Mileage, cfv.Color,
        #        cfv.AcquiredOn,cfv.AcquiredBy, cfv.AcquiredFromLocation, cfv.AcquistionCost, ac.CustomerDisplayName,
        #        if(Customername = ac.customerid in (select customerid from cfgserviceplan), 'Internal', 'External')
        #        As GroupName, av.Year,msmake.MakeName , msmodel.ModelName , msstyle.StyleName, msa.AddrZip
        #        from ((cfgfilevehicle cfv
        #        left join appvehicle av on cfv.VehicleID = av.VehicleID)
        #        left join cfgcustomerlocation ccl on ccl.clid = cfv.acquiredfromlocation
        #        left join msaddress msa on msa.AddrId = ccl.AddrId) , msmake, msmodel, msstyle, appcustomer ac
        #        where cfv.VehicleID = av.VehicleID and av.MakeId=msmake.MakeId and av.ModelId=msmodel.ModelId
        #        and msstyle.StyleName!=''and msa.AddrZip!=' ' and av.StyleId=msstyle.StyleId
        #        and ccl.clid = cfv.AcquiredFromLocation and  ac.CustomerId = ccl.Customerid  group by av.VIN
        #        order by (msa.AddrZip) asc limit 6000,7000"""

        # print(len(pd.read_sql_query("select * from appfile limit 101, 900", con)))
        try:
            # replace sql query with pandas
            result = pd.read_sql_query(sqlquery, con)
            # test = pd.read_sql_query(test, con)


            # Execute the SQL command
            # cursor.execute(statement)
            # Fetch all the rows in a list of lists.
            # results = cursor.fetchall()
            return result
            # return pd.read_csv("C:/Users/Administrator/Desktop/IVV.csv")
        except pymysql.Error as err:
            lhelper.getlogger().error(err)
        except IOError as errorNo:
            lhelper.getlogger().error("I/O error({0}): {1}".format(errorNo))

        # disconnect from server
        con.close()
