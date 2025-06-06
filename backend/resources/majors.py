from flask import current_app
from flask_restful import Resource
from sample_data import majors

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
            # Fetch the data for the majors list. Only needs to display the name.
            # For now this is from the majors list in sample_data.py
            majors_data = [
                {
                    "_id": major["_id"], 
                    "name": major["name"],  
                }
                for major in majors
            ]

            # Handle error case where no majors are found in the dataset
            if not majors_data:
                return {"error": "No majors found."}, 404
            
            # Return the list of majors as a JSON response with HTTP 200 status
            return {"majors": majors_data}, 200
        
        except Exception as e:
            # Log the error for debugging
            current_app.logger.error("Error retrieving majors: %s", str(e))

            return {
                "error": "An error occurred while retrieving majors.",
                "message": str(e)
            }, 500
