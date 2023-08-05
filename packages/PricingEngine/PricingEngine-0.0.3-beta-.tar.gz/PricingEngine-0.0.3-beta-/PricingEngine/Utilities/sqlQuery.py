class sqlQuery:

    sql_query = {
        'sql_query': """select cfv.Mileage, cfv.Color, cfv.AcquistionCost, av.Year,msmake.MakeName , msmodel.ModelName , msstyle.StyleName, msa.AddrZip
                    from ((cfgfilevehicle cfv
                    left join appvehicle av on cfv.VehicleID = av.VehicleID)
                    left join appfile af on af.filenum = cfv.filenum
                    left join cfgcustomerlocation ccl on ccl.clid = cfv.acquiredfromlocation
                    left join msaddress msa on msa.AddrId = ccl.AddrId) , msmake, msmodel, msstyle, appcustomer ac
                    where cfv.VehicleID = av.VehicleID and av.MakeId=msmake.MakeId and av.ModelId=msmodel.ModelId 
                    and msstyle.StyleName!=''and msa.AddrZip!=' ' and av.StyleId=msstyle.StyleId 
                    and ccl.clid = cfv.AcquiredFromLocation and  ac.CustomerId = ccl.Customerid
                    and cfv.Mileage > 10000 and cfv.Mileage is not null and cfv.Color not like '%#%' and cfv.Color is not null
                    and msmake.MakeName != '' and msmodel.ModelName != '' and msstyle.StyleName != '' and msstyle.StyleName not like '%!%'
                    and af.filestatusid in (1,2) and cfv.AcquistionCost >= 300 and cfv.AcquistionCost <= 100000 
                    and cfv.Mileage != cfv.AcquistionCost and cfv.Mileage < 400000 group by av.VIN 
                    order by (msa.AddrZip) desc""",

        'train': """select cfv.Mileage, cfv.Color, cfv.AcquistionCost, av.Year,msmake.MakeName , msmodel.ModelName , msstyle.StyleName, msa.AddrZip
                    from ((cfgfilevehicle cfv
                    left join appvehicle av on cfv.VehicleID = av.VehicleID)
                    left join appfile af on af.filenum = cfv.filenum
                    left join cfgcustomerlocation ccl on ccl.clid = cfv.acquiredfromlocation
                    left join msaddress msa on msa.AddrId = ccl.AddrId) , msmake, msmodel, msstyle, appcustomer ac
                    where cfv.VehicleID = av.VehicleID and av.MakeId=msmake.MakeId and av.ModelId=msmodel.ModelId 
                    and msstyle.StyleName!=''and msa.AddrZip!=' ' and av.StyleId=msstyle.StyleId 
                    and ccl.clid = cfv.AcquiredFromLocation and  ac.CustomerId = ccl.Customerid
                    and cfv.Mileage > 10000 and cfv.Mileage is not null and cfv.Color not like '%#%' and cfv.Color is not null
                    and msmake.MakeName != '' and msmodel.ModelName != '' and msstyle.StyleName != '' and msstyle.StyleName not like '%!%'
                    and af.filestatusid in (1,2) and cfv.AcquistionCost >= 300 and cfv.AcquistionCost <= 100000 
                    and cfv.Mileage != cfv.AcquistionCost and cfv.Mileage < 400000 group by av.VIN 
                    order by (msa.AddrZip) desc limit 12000 OFFSET 6000""",

        'test': """select cfv.Mileage, cfv.Color, cfv.AcquistionCost, av.Year,msmake.MakeName , msmodel.ModelName , msstyle.StyleName, msa.AddrZip
                    from ((cfgfilevehicle cfv
                    left join appvehicle av on cfv.VehicleID = av.VehicleID)
                    left join appfile af on af.filenum = cfv.filenum
                    left join cfgcustomerlocation ccl on ccl.clid = cfv.acquiredfromlocation
                    left join msaddress msa on msa.AddrId = ccl.AddrId) , msmake, msmodel, msstyle, appcustomer ac
                    where cfv.VehicleID = av.VehicleID and av.MakeId=msmake.MakeId and av.ModelId=msmodel.ModelId 
                    and msstyle.StyleName!=''and msa.AddrZip!=' ' and av.StyleId=msstyle.StyleId 
                    and ccl.clid = cfv.AcquiredFromLocation and  ac.CustomerId = ccl.Customerid
                    and cfv.Mileage > 10000 and cfv.Mileage is not null and cfv.Color not like '%#%' and cfv.Color is not null
                    and msmake.MakeName != '' and msmodel.ModelName != '' and msstyle.StyleName != '' and msstyle.StyleName not like '%!%'
                    and af.filestatusid in (1,2) and cfv.AcquistionCost >= 300 and cfv.AcquistionCost <= 100000 
                    and cfv.Mileage != cfv.AcquistionCost and cfv.Mileage < 400000 group by av.VIN 
                    order by (msa.AddrZip) desc limit 5000 OFFSET 1000"""
    }
