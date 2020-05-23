from pymongo import MongoClient
client = MongoClient()
print("Client Is Ready")

empDB = client['pdbcmongo']
print("DB Is Created")

empCollection = empDB.mongoemp
print("mongoemp Collection/table is Created")

docuemnt = empCollection.insert_one({'ENO':111,'ENAME':"AAA",'ESAL':5000,'EADDR':"Hyd"})
print("Docuemt Inserted")
client.close()
print("Client Closed")