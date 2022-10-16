import pymongo
client = pymongo.MongoClient("mongodb+srv://tarunineuron:tarun1947@cluster0.ndr6d24.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name":"tarun", "email":"tarun_rao@hotmail.com", "surname":"rao"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)