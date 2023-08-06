from config import db
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List


class Collection:
    def __init__(self, collection: str):
        # Create a new collection called  collection
        self.collection = db[collection]

    def insert_one(self, document: dict):
        # Insert a new document into the  collection
        self.collection.insert_one(document)

    def insert_many(self, documents: List[dict]):
        # Insert a list of documents into the  collection
        self.collection.insert_many(documents)

    def find_all(self):
        # Find all documents in the  collection
        return list(self.collection.find({}))

    def find_one(self, selector: dict):
        # Find one document in the  collection
        return self.collection.find_one(selector)

    def find_many(self, selector: dict):
        # Find many  document in the  collection
        return self.collection.find(selector)

    def update_one(self, selector: dict, document: dict):
        # Update a document in the "users" collection
        self.collection.update_one(selector, {"$set": document})

    def delete_one(self, selector: dict):
        # Delete a document from the "users" collection
        self.collection.delete_one(selector)

    def delete_many(self, selector: dict):
        self.collection.delete_many(selector)

    # Check if a data record existed
    def is_existed(self, selector: dict):
        result = self.collection.find(selector)
        return bool([r for r in result])
