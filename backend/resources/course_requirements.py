from flask import current_app, jsonify
from flask_restful import Resource
import sample_data

class CourseRequirements(Resource):
    """
    CourseRequirements Resource
    Retrieves the prerequisite and corequisite course IDs for a given 
    course ID. Used for controlling the drag and drop in the Schedule.

    Returns:
    - A JSON object containing the array of prequisite ids and the array of corequisite ids
    - HTTP status codes: 200 (Success), 404 (Not Found), 500 (Internal Server Error)
    
    Example object returned in JSON:
    {
        "prerequisites": [101],
        "corequisites": [],
    }
    """
    # Supports GET requests
    def get(self, course_id):
        try:
            # Ensure that course id is always an integer
            course_id = int(course_id)
            
            # Look up course in sample_data.courses list based on its idea
            # Future: query from mongoDB
            course_details = next((c for c in sample_data.courses if c['_id'] == course_id), None)
            if not course_details:
                return {"error":f"Course with id {course_id} not found."}, 404
            
            # Normalize and extract the prerequisite and corequisite lists from the course details
            requirements = {
                "prerequisites": [int(p) if isinstance(p, str) else p for p in course_details.get("prerequisites", [])],
                "corequisites": [int(c) if isinstance(c, str) else c for c in course_details.get("corequisites", [])],
            } 
            # Ensure requirements can be serialized
            try: 
                serilaized_output = jsonify(requirements)
            except Exception as serialization_error:
                return {
                    "error": "Data serialization error occurred.",
                    "message": str(serialization_error)
                }, 500

            return requirements, 200
            
        except Exception as e:
            # Log the exception for debugging
            current_app.logger.error("Error retrieving course requirements: %s", str(e))
            return {
                "error": "An error occurred while retrieving course requirements.",
                "message": str(e)
            }, 500
        
