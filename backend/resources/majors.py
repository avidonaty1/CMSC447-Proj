from flask import current_app
from flask_restful import Resource
#from sample_data import majors
from Database import connectingToDatabase, enterDatabase, openMajorDB

class Majors(Resource):
    # This class defines a RESTful resource for handling GET requests
    # to retrieve a list of majors. 
    # Intended use is in the major dropdown menu

    def get(self):
        """
        Handles GET requests for retrieving the list of majors
        *** FUTURE UPDATE is to retrieve information from mongoDB

        Returns:
        - Success: A JSON object containing a list of majors (HTTP 200)
        - Failure: An error message id no majors are found (HTTP 404)
                   or if an internal server error occurs (HTTP 500)
        """
        try:
            # Opening the connection for mongoDB
            client = connectingToDatabase()
            # Getting to our database
            db = enterDatabase("UMBC", client)
            # Opening the Collection 
            major = openMajorDB(db)

            # Handle error case where no (major collection) are found in the dataset
            if not major:
                return {"error": "No majors found."}, 404
            
            # Return the list of majors as a JSON response with HTTP 200 status
            return {"majors": major}, 200
        
        except Exception as e:
            # Log the error for debugging
            current_app.logger.error("Error retrieving majors: %s", str(e))

            return {
                "error": "An error occurred while retrieving majors.",
                "message": str(e)
            }, 500

# 'major' collection looks like this:
# {'_id': ObjectId(STRING), 'name': STRING, 'number_credits': INT, 
#   'required_courses': ARRAY OF STRING, 'default_plan': {NESTED DICTIONARY}

# Example:
# 'default_plan': {'MATH151': {'year': 1, 'session': 'Fall'}, 'CMSC201': {'year': 1, 'session': 'Fall'}, 'CMSC202': {'year': 1, 'session': 'Spring'}}}

