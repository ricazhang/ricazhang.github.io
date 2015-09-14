import pymongo
import json
from pprint import pprint
import numpy
import scipy
 
client = pymongo.MongoClient("localhost", 27017)
db = client.yelp
users_collection = db.users
reviews_collection = db.reviews
businesses_collection = db.businesses
restaurant_review_collection = db.restaurant_reviews
food_review_collection = db.food_reviews
restaurants_collection = db.restaurants
culinary_businesses_collection = db.culinary_businesses
print db.name
 
print "loading dictionaries..."
b_dict = {}
for business in businesses_collection.find().limit(500):
	b_dict.setdefault(business["business_id"], len(b_dict))
print "...dictionaries loaded!"
 
i = 0  
for review in reviews_collection.find():
	b_id = review["business_id"]
	b_current = businesses_collection.find({"business_id":b_id})[0]
	if "Restaurants" in b_current["categories"]:
		restaurants_collection.save(b_current)
		culinary_businesses_collection.save(b_current)
		restaurant_review_collection.insert(review)
		food_review_collection.insert(review)
		i = i + 1
	elif "Food" in str(b_current["categories"]).split(',')[0]:
		culinary_businesses_collection.save(b_current)
		food_review_collection.insert(review)
		i = i + 1 
 
		#print b_current["categories"]
	#elif "Cafe" in b_current["categories"]:
		#	print b_current["categories"]
	#else:
		#	print b_current["categories"]
	if i % 5000 == 0:
		print i
#print "Number of Restaurant Reviews: " +  str(i)