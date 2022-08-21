import pymongo as pm

connection = pm.MongoClient("mongodb+srv://vishwas:hJqP4-ef65@cluster-vishwas.v3i9doq.mongodb.net/?retryWrites=true&w"
                            "=majority")
db = connection.test

database = connection['Inventory']
collection = database['Store']

# return_collection = collection.find({'name': 'Vishwas'})
# for i in return_collection:
#     print(i)

# return_coll = collection.find({'courses': {'$gt': 'd'}})
# for i in return_coll:
#     print(i)

data = [
    {
        "item": "canvas",
        "qty": 100,
        "size": {"h": 28, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "journal",
        "qty": 25,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mat",
        "qty": 85,
        "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "mousepad",
        "qty": 25,
        "size": {"h": 19, "w": 22.85, "uom": "cm"},
        "status": "P",
    },
    {
        "item": "notebook",
        "qty": 50,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "P",
    },
    {
        "item": "paper",
        "qty": 100,
        "size": {"h": 8.5, "w": 11, "uom": "in"},
        "status": "D",
    },
    {
        "item": "planner",
        "qty": 75,
        "size": {"h": 22.85, "w": 30, "uom": "cm"},
        "status": "D",
    },
    {
        "item": "postcard",
        "qty": 45,
        "size": {"h": 10, "w": 15.25, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketchbook",
        "qty": 80,
        "size": {"h": 14, "w": 21, "uom": "cm"},
        "status": "A",
    },
    {
        "item": "sketch pad",
        "qty": 95,
        "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
        "status": "A",
    },
]

# collection.insert_many(data)
# return_stores = collection.find({'status': 'A'})
# return_stores = collection.find({'status': {'$in': ['A', 'P']}})
# return_stores = collection.find({'status': {'$gt': 'B'}})
# return_stores = collection.find({'qty': {'$gte': 70}})
#return_stores = collection.find({'item': 'planner', 'qty': 75}) # AND Condition
# print(next(return_stores))
# return_stores = collection.find({'item': 'sketch pad', 'qty': {'$gte': 75}})
# return_stores = collection.find({'$or': [{'item': 'sketch pad'}, {'qty': {'$gte': 75}}]})

# for i in return_stores:
#     print(i)

#update_stores = collection.update_one({'item': 'mat'}, {'$set':{'item': 'vishwas'}})
delete_stores = collection.delete_one({'item': 'vishwas'})
return_stores = collection.find({'item': 'vishwas'})
for i in return_stores:
    print(i)