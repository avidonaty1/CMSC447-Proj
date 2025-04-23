# For David's Mac: source .venv/bin/activate
# For David's Mac: deactivate
# (Check for Dependencies)
#   python --version
#   pip list

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
    string = "mongodb://davidn4:<db_password>@davidn4-shard-00-00.bcabt.mongodb.net:27017,davidn4-shard-00-01.bcabt.mongodb.net:27017,davidn4-shard-00-02.bcabt.mongodb.net:27017/?replicaSet=atlas-laj9s7-shard-0&ssl=true&authSource=admin&retryWrites=true&w=majority&appName=davidn4"
    string = string.replace("<db_password>", "upP7VRk03qb2DnKk")
    client = MongoClient(string)
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
    # ensure that each datapoint of prerequisites and corequisites is a list with , as the delimiter
    for record in data:
        if 'prerequisites' in record:
            record['prerequisites'] = [x.strip() for x in record['prerequisites'].split(',')]
        if 'corequisites' in record:
            record['corequisites'] = [x.strip() for x in record['corequisites'].split(',')]
    # iterate through each record
    for record in data:
        # Use the 'number' as the unique identifier
        if 'number' in record:
            collection.update_one(
                {"number": record["number"]}, # Match by 'number'
                {"$set": record},        # Update the document with the new data
                upsert=True              # Insert if it doesn't exist
            )
        else:
            # Insert the record if it doesn't have an 'number' field
            collection.insert_one(record)
    print("Data inserted/updated successfully!")

def insertMajorData(fileAddress, collection): # （INCOMPLETE)
    """_summary_ Insert major data into the major collection

    Args:
        fileAddress (_string_): address of the file
        collection (_collection_): collection object in the database
    """
    # read each sheet of the excel file
    sheets = pd.read_excel(fileAddress, sheet_name=None)
    # iterate through each sheet and extract the data
    for sheet_name, df in sheets.items():
        # making sure '\n' is removed from the column names
        df.columns = df.columns.str.replace('\n', ' ')
        # drop rows with NaN values in either of the first two columns
        filtered_df = df.dropna(subset=[df.columns[0], df.columns[1]])
        # create a dictionary using the first column as keys and the second column as values
        dict_elements = dict(zip(filtered_df.iloc[:, 0], filtered_df.iloc[:, 1]))
        # for "required_courses", drop NaN values and convert the column to a single list
        required_courses_array = df['required_courses'].dropna().astype(str).str.strip().tolist()        
        # convert last columns to a nested dictionary
        filtered_df = df.dropna(subset=['default_plan', 'year', 'session'])
        nested_dict = filtered_df.set_index('default_plan')[['year', 'session']].to_dict(orient='index')
        
        # use 'Mechanical Engineering' as the unique identifier
        if 'Mechanical Engineering' in dict_elements:
            # Update the document with the new data
            collection.update_one(
                {"name": dict_elements["name"]}, # Match by 'Mechanical Engineering'
                {"$set": {
                    "number_credits": dict_elements["number_credits"],
                    "required_courses": required_courses_array,
                    "default_plan": nested_dict
                }},
                upsert=True              # Insert if it doesn't exist
            )
        else:
            # Insert the record if it doesn't have an 'Mechanical Engineering' field
            collection.insert_one({
                "name": dict_elements["name"],
                "number_credits": dict_elements["number_credits"],
                "required_courses": required_courses_array,
                "default_plan": nested_dict
            })
    print("Data inserted/updated successfully!")
        
        
    
def insertStudentData(fileAddress, collection):
    """_summary_ Insert student data into the student collection

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
        # Use the 'Campus ID' as the unique identifier
        if 'campus_id' in record:
            collection.update_one(
                {"campus_id": record["campus_id"]}, # Match by 'Campus ID'
                {"$set": record},        # Update the document with the new data
                upsert=True              # Insert if it doesn't exist
            )
        else:
            # Insert the record if it doesn't have an 'Campus ID' field
            collection.insert_one(record)
    print("Data inserted/updated successfully!")
    

# [FETCHING DATA FROM DATABASE] ========================================
    
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

def printCollection(collection):
    """_summary_ Print the collection from mongoDB

    Args:
        collection (_collection_): collection object in the database
    """
    # Pulling collection from mongoDB
    cursor = collection.find()
    # Printing the collection
    for document in cursor:
        print(document)
        # Print a new line
        print("\n")


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
        
        """
        # Insert course data
        print("Python: Inserting course data")
        insertCourseData("/Users/davidzhang/Downloads/Classes.xlsx", course)
        
        #Insert student data
        print("Python: Inserting student data")
        insertStudentData("/Users/davidzhang/Downloads/Students.xlsx", student)
        
        # Insert major data
        print("Python: Inserting major data")
        insertMajorData("/Users/davidzhang/Downloads/Major.xlsx", major)
        """
        
        
        # acessing student data
        print("Python: Accessing student data", "\n")
        # get doucment with campus_id OF66938
        student_data = student.find_one({"campus_id": "OF66938"})
        print(student_data)
        # print the student email
        print("Student email: ", student_data["email"])
        