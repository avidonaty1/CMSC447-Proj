# import libraries for mongoDB
from pymongo import MongoClient
import pymongo
import pandas as pd
import openpyxl

def testingConnection():
    """ 
        This function tests the connection to MongoDB Atlas.
    """
    try:
        # replace <username>, <password>, and <dbname> in the URL
        client = MongoClient("mongodb+srv://davidn4:upP7VRk03qb2DnKk@davidn4.bcabt.mongodb.net/?retryWrites=true&w=majority&appName=davidn4")
        db = client["mydatabase"]
        print("Connected to MongoDB Atlas!")
    except Exception as e:
        print(e)

# [CONNECTING TO DATABASE] ========================================
def connectingToDatabase():
    """_summary_ Connecting to MongoDB Atlas and returns the client object
    
    Returns:
        _type_: Returns the client object
    """
    uri = "mongodb://davidn4:upP7VRk03qb2DnKk@davidn4-shard-00-00.bcabt.mongodb.net:27017,davidn4-shard-00-01.bcabt.mongodb.net:27017,davidn4-shard-00-02.bcabt.mongodb.net:27017/?replicaSet=atlas-laj9s7-shard-0&ssl=true&authSource=admin&retryWrites=true&w=majority&appName=davidn4"
    client = MongoClient(uri)
    return client

def enterDatabase(name, client):
    """_summary_ Enters the database and returns the database object
    
    Args:
        name (_string_): name of the database
        client (_client_): client object

    Returns:
        return database object
    """
    db = client[name]
    return db

def openCourseDB(db):
    """_summary_ Opens the collection in the database
    
    Args:
        db (_database_): database object

    Returns:
        return collection object
    """
    collection = db["classes"]
    return collection
   
def openStudentDB(db):
    """_summary_ Opens the collection in the database
    
    Args:
        db (_database_): database object

    Returns:
        return collection object
    """
    collection = db["students"]
    return collection  

def openMajorDB(db):
    """_summary_ Opens the collection in the database

    Args:
        db (_database_): database object

    Returns:
        return collection object
    """
    collection = db["majors"]
    return collection


# [INSERT COURSE DATA INTO DATABASE] ========================================
def insertCourseData(fileAddress, collection):
    """_summary_ Insert course data into the course collection

    Args:
        fileAddress (_string_): address of the file
        collection (_collection_): collection object in the database
    """
    # read the excel file
    df = pd.read_excel(fileAddress)
    # making sure '\n' is removed from the column names
    df.columns = df.columns.str.replace('\n', ' ')
    # convert the rows into a list of dictionaries
    data = df.to_dict('records')
    # iterate through each record
    for record in data:
        # Use the 'Course Number' as the unique identifier
        if 'Course Number' in record:
            collection.update_one(
                {"Course Number": record["Course Number"]}, # Match by 'Course Number'
                {"$set": record},        # Update the document with the new data
                upsert=True              # Insert if it doesn't exist
            )
        else:
            # Insert the record if it doesn't have an 'Course Number' field
            collection.insert_one(record)
    print("Data inserted/updated successfully!")
    
    
# [DEBUGGING] ========================================
def isDatabaseOnline(db):
    """Check if the database is online by listing its collections.

    Args:
        db (_type_): database object

    Returns:
        bool: True if the database is online, False otherwise
    """
    try:
        # Attempt to list collections in the database
        collections = db.list_collection_names()
        print("Database is online. Collections:", collections)
        return True
    except Exception as e:
        print("Database is offline. Error:", e)
        return False

    
# [MAIN] ========================================
if __name__ == "__main__":
    # Open the database
    print("Python: Connecting to MongoDB Atlas")
    client = connectingToDatabase()
    db = enterDatabase("UMBC", client)
    
    # Check if the database is online
    if not isDatabaseOnline(db):
        print("Python: Failed to access the database.")
    else:
        print("Python: Database is accessible.")
        
        # Open the collections
        course = openCourseDB(db)
        student = openStudentDB(db)
        major = openMajorDB(db)
        
        # Insert course data
        print("Python: Inserting course data")
        insertCourseData("/Users/davidzhang/Downloads/Basic Majors.xlsx", course)
    

    
    
    