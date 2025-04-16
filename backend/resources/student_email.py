from flask import current_app
from flask_restful import Resource
import sample_data

class StudentEmail(Resource):
    """
    StudentEmail Resource
    Fetches: Fetches a student's ID based on their email address
    """
    # Supports GET requests for fetching the email
    def get(self, email):
        try:
            # Find the student by email
            student = next((s for s in sample_data.students if s['email'].lower() == email.lower()), None)

            # Handle error for no matching student email
            if not student:
                return {"error": f"Student with email {email} not found."}, 404
            
            # Otherwise, return the student id
            return {"student_id": student["_id"]}, 200
        
        except Exception as e:
            # Log the exception for debugging
            current_app.logger.error("Error retrieving student by email: %s", str(e))
            return {
                "error": "An error occurred while retrieving the student ID.",
                "message": str(e)
            }, 500
        
    
    
        
