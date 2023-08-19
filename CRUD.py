#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

#David Novosad

class AnimalShelter(object):
    
    def __init__(self, USER, PASS):
        
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30115
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
       
    def create(self, data):
        if data is not None:
            insertValid = self.database.animals.insert_one(data)
            return True if insertValid.acknowledged else False
        else:
            raise Exception("Nothing created! Data parameter is empty or incorrect.")
    
    def read(self, criteria):
        if criteria is not None:
            return self.database.animals.find(criteria,{"id":False})
        else:
            raise Exception("Nothing read! Data parameter is empty or incorrect.")
    
    def update(self, query, data):
        if data is not None:    
            updateValid = self.database.animals.update_many(query, {"$set": data})
            updated_count = updateValid.modified_count
            print(f"{updated_count} records were updated.")
            return True if updated_count > 0 else False
        else:
            raise Exception("Nothing updated! Data parameter is empty or incorrect.")
            

    def delete(self, query):
        if query is not None:
            deleteValid = self.database.animals.delete_many(query)
            delete_count = deleteValid.deleted_count
            print(f"{delete_count} records were deleted.")
            return True if delete_count > 0 else False
        else:
            raise Exception("Nothing deleted! Query parameter is empty or incorrect.")