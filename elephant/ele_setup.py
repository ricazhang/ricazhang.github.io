import pymongo
import csv
import json
from pprint import pprint
 
client = pymongo.MongoClient("localhost", 27017)
db = client.elephant
locations = db.locations
print "database name: " + db.name
count = 0
 
with open('ele_latlong.csv') as ele_data:
    reader = csv.reader(ele_data)
    for line in reader:
        count += 1
        ele_dict = {"name": line[0], 
                    "timestamp": line[2], 
                    "x": line[3], 
                    "y": line[4]}
        print ele_dict
        #print line
        locations.insert(ele_dict)
        #continue

print "number of lines read: " + str(count) #checks number of lines of file read through (should be about 22,440)
print("done")
print "collections: " + str(db.collection_names(include_system_collections=False)) #prints out your collections, should be elephants
print "documents in locations collection: " + str(locations.count()) #number of documents in elephants collection