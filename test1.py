import pymongo as pm

# Previously, when we had Mysql, we installed the database in our system, so we're using host = localhost
# But with MongoDB Database, everything is going on cloud, so we're getting a URL for making a connection

connection = pm.MongoClient("mongodb+srv://vishwas:hJqP4-ef65@cluster-vishwas.v3i9doq.mongodb.net/?retryWrites=true&w"
                            "=majority")
db = connection.test
# print(db)

d = {
    'name': 'vishwas',
    'mail': 'vishwas@mail.com',
    'surname': 'K. Sharma'
}
d = {
    'name': 'vishwas',
    'mail': 'vishwas@mail.com',
    'surname': 'K. Sharma'
}

qury1 = connection['mongotest']
coll1 = qury1['test']
coll1.insert_one(d)