import pymongo
import json
from pprint import pprint
 
client = pymongo.MongoClient("localhost", 27017)
db = client.yelp
users = db.users
reviews = db.reviews
businesses = db.businesses
print db.name
count = 0
 
with open('yelp_academic_dataset.json') as yelp_data:
    for line in yelp_data:
    	count += 1
    	data = json.loads(line)
    	if data['type'] == 'business':
    	    businesses.insert(data)
    	elif data['type'] == 'user':
    		users.insert(data)
    	elif data['type'] == 'review':
    	    reviews.insert(data)
 
print count #checks number of lines of file read through (should be about 470,000)
print("done")
print db.collection_names(include_system_collections=False) #prints out your collections, should be users, reviews, businesses
print users.count() #number of documents in users collection
print reviews.count() #number of documents in reviews collection
print businesses.count() #number of documents in businesses collection
print users.count() + reviews.count() + businesses.count() #total number of documents in your yelp db