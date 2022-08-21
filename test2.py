import pymongo as pm

connection = pm.MongoClient("mongodb+srv://vishwas:hJqP4-ef65@cluster-vishwas.v3i9doq.mongodb.net/?retryWrites=true&w"
                            "=majority")
db = connection.test

data = {
    'name': 'Vishwas',
    'courses': ['data science', 'ML', 'DL', 'Business Analytics'],
    'mail': 'vishwas@mail.com'
}

list_of_records = [
    {
        'name': 'Vishwas',
        'courses': ['data science', 'ML', 'DL', 'Business Analytics'],
        'mail': 'vishwas@mail.com'
    },
    {
        'name': 'Anurag',
        'courses': ['SBI PO', 'IBPS PO', 'HCS'],
        'mail': 'anurag@mail.com'
    }
]
database = connection['mongotest']
collection = database['test2']
# collection.insert_one(data)

# collection.insert_many(list_of_records)

d1 = {"packetType": "D",
         "data": {"checkEngineLightFlag": "F", "batteryVoltageStableTime": 0, "batteryVoltageStable": "0",
                  "batteryVoltageOff": "12.42", "batteryCrankParamTN": "-0.08", "batteryCrankParamVN": "0.00",
                  "batteryCrankParamTP": "-0.08", "batteryCrankParamVP": "0.00", "batteryCrankParamTT": "-0.00008",
                  "batteryCrankParamV0": "0.00", "batteryVoltageMaxOn": "13.05", "batteryVoltageMinOn": "12.97",
                  "batteryVoltageMaxOff": "12.46", "batteryVoltageMinOff": "12.36", "batteryVoltageOnAverage": "13.02",
                  "engineLoadMax": "84", "engineLoadAverage": "39.98", "rpmMax": "3487", "rpmAverage": "1431.29",
                  "gpsSpeedAverage": "21.99", "vssMax": "53.44", "vssAverage": "23.06", "tcuTemperatureMin": "82.40",
                  "tcuTemperatureMax": "109.40", "tcuTemperatureAverage": "104.87", "coolantMin": "158.00",
                  "coolantMax": "188.60", "coolantAverage": "180.20", "packetStartLocal": 1508143346000,
                  "tripStartLocal": 1508143346000, "milIndicator": "F", "monitorsNotReady": 0, "imei": "60DF5417",
                  "gatewayTs": 1515613306592, "diagnosticTroubleCodeData": [345345],
                  "diagnosticPidData": [[64768, 47, 100], [64768, 1, 517376], [64800, 1, 262144], [64768, 5, 125]]},
         "header": {"iwrapVer": "1.9.20", "sourceSystem": "CDP", "configVer": "1.1", "oemName": "HUM", "unitType": 0,
                    "cpVer": "7.50.1.9", "igpsVer": "1.3.7", "messageType": "Notification", "pomVer": "1.0",
                    "headerVer": "V6", "timestamp": 0, "deviceType": "InDrive", "visorVer": "1.4.35",
                    "transactionId": "53098471-7787-4160-94b3-cd69dcc70416", "deviceSerialNo": "60DF5417",
                    "subOrganization": "HUM", "organization": "HUM", "imei": "60DF5417", "operation": "Notification"}}

#collection.insert_one(d1)

collection1 = database['dpkt']
collection1.insert_one(d1)

# ETL in MongoDB

return_collection = collection.find()  # This will return the whole collection/table. Since collection is an interable
# we will run a for loop on it to extract all the data.

#print(type(return_collection))   # pymongo.cursor.Cursor: Means it's a pointer
for i in return_collection:
    print(i)