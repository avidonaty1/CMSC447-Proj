from flask import current_app
from flask_restful import Resource
from sample_data import majors

class Majors(Resource):
    # Supports GET requests
    def get(self):
        try:
            # Fetch the data for the majors list
            majors_data = [
                {
                    "id": major["_id"], 
                    "name": major["name"],
                    "number_credits": major["number_credits"]    
                }
                for major in majors
            ]
            if not majors_data:
                return {"error": "No majors found."}, 404
            return {"majors": majors_data}, 200
        
        except Exception as e:
            current_app.logger.error("Error retrieving majors: %s", str(e))
            return {
                "error": "An error occurred while retrieving majors.",
                "message": str(e)
            }, 500
