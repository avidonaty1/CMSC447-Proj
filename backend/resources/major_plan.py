from flask import current_app
from flask_restful import Resource
import sample_data
from utils.utility_functions import build_nested_plan

class MajorPlan(Resource):
    """
    MajorPlan Resource
    Provides the course sequence for the default 4 year plan for a given major
    Supports GET requests to fetch the default plan structured by year and semester

    Returns:
    - The major id, and a nested plan organized by years and sessions containing courses.
    - The courses are dictopnaries with key-value pairs:
    id-course.id
    number-course.number
    offered_winter-course.offered_winter
    offered_summer-course.offered_summer
    credit_hours-course.credit_hours
    corequisites-course.corequisites 
    - JSON, appears as an array (i.e [101, MATH151])
    - HTTP status codes: 200 (Success), 404 (Not Found), 500 (Internal Server Error)
    
    Example object returned in JSON
    {
      "major_id": 1,
      "default_plan": {
        "year1": {
          "Fall": []
            {"id": 101,
            "number": "MATH151",
            "credit_hours": 4,
            "offered_winter": false,
            "offered_summer": true,
            "prerequisites", [],
            "corequisites", []
            },
            {"id": 103,
            "number": "CMSC201",
            "credit_hours": 4,
            "offered_winter": false,
            "offered_summer": true,
            "prerequisites", [],
            "corequisites", []
            },
          ],
          "Winter": [],
          "Spring": [
            {"id": 104,
            "number": "CMSC202",
            "offered_winter": false,
            "offered_summer": true,
            "credit_hours": 4,
            "prerequisites", [103],
            "corequisites", []
            }
          ],
          "Summer": []
        },
        "year2": { "Fall": [], "Winter": [], "Spring": [], "Summer": [] },
        "year3": { "Fall": [], "Winter": [], "Spring": [], "Summer": [] },
        "year4": { "Fall": [], "Winter": [], "Spring": [], "Summer": [] }
      }
    }
    """
    # Supports GET requests
    def get(self, major_id):
        try:
            # Fetch the data for the provided major_id
            major = next((m for m in sample_data.majors if m['_id'] == major_id), None)

            # Handle error for no matching major _id
            if not major:
                return {"error": f"Major with id {major_id} not found."}, 404
            
            # Ensure that the major has a default plan
            default_plan_raw = major.get("default_plan")
            if not default_plan_raw:
                return {"error": "No default plan available for major."}, 404

            nested_plan = build_nested_plan(default_plan_raw)
            return {"major_id": major_id, "default_plan": nested_plan}, 200
        
        except Exception as e:
            # Log the exception for debugging
            current_app.logger.error("Error retrieving default plan: %s", str(e))
            return {
                "error": "An error occurred while retrieving default plan for major.",
                "message": str(e)
            }, 500
        
