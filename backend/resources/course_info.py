from flask import current_app
from flask_restful import Resource
import sample_data

def get_course_display(course_id):
    """
    Helper function to look up a course in sample_data.py by its id 
    and return the course number (i.e. CMSC201). Future: query from mongoDB.
   
    Args: course_id (int): The course's numeric ID.

    Returns: The course's number if found, otherwise return the original ID.
    """
    course = next((c for c in sample_data.courses if c['_id'] == course_id), None)
    return course['number'] if course else str(course_id)

class CourseInfo(Resource):
    """
    CourseInfo Resource
    Provides detailed information for a specific course based on its course id.
    Takes the course ids for the prerequisites and converts them to names for display.

    Returns:
    - A JSON object containing course details (if found)
    - HTTP status codes: 200 (Success), 404 (Not Found), 500 (Internal Server Error)
    
    Example object returned in JSON:
    {
        "_id": 102
        "number": "MATH152"
        "title": "Calculus and Analytic Geometry II",
        "description": "Topics of this course include ... ",
        "credit_hours": 4,
        "fills_up_quickly": "Rarely",
        "offered_winter": false,
        "offered_summer": true,
        "prerequisites": ["MATH151"],
        "corequisites": [],
    }
    """
    # Supports GET requests
    def get(self, course_id):
        """
        Args: course_id(int): Idenfier of course (expected as int)
        """
        try:
            # Look up course in sample_data.courses list based on its idea
            # Future: query from mongoDB
            course_details = next((c for c in sample_data.courses if c['_id'] == course_id), None)
            if not course_details:
                return {"error":f"Course with id {course_id} not found."}, 404
            
            # Convert prerequisites and corequisites from an array of ids to any array of course numbers
            if "prerequisites" in course_details:
                course_details["prerequisites"] = [ 
                    get_course_display(prereq_id) for prereq_id in course_details["prerequisites"]
                ]
        
            if "prerequisites" in course_details:
                course_details["corequisites"] = [ 
                    get_course_display(coreq_id) for coreq_id in course_details["corequisites"]
                ]
            
            
            return course_details, 200
            
        except Exception as e:
            # Log the exception for debugging
            current_app.logger.error("Error retrieving course info: %s", str(e))
            return {
                "error": "An error occurred while retrieving course info.",
                "message": str(e)
            }, 500
        
