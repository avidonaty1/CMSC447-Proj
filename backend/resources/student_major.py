from flask import current_app, request
from flask_restful import Resource
import sample_data

class StudentMajor(Resource):
    """
    StudentMajor Resource
    Fetches: Fetches or updates the student's major_id attribute by ID (looks for the _id attribute)
    """
    # Supports GET requests for fetching the major
    def get(self, student_id):
        try:
            # Find the student by student_id
            student = next((s for s in sample_data.students if s['_id'] == student_id), None)

            # Handle error for no matching student _id
            if not student:
                return {"error": f"Student with id {student_id} not found."}, 404
            
            # Otherwise, return the major. It may be an empty string if the student has not selected a major
            return {"student_id": student_id, "major_id": student.get("major_id", "")}, 200
        
        except Exception as e:
            # Log the exception for debugging
            current_app.logger.error("Error retrieving student major: %s", str(e))
            return {
                "error": "An error occurred while retrieving major for student.",
                "message": str(e)
            }, 500
        
    # Supports POST requests for updating the major
    # Note this DOES NOT WORK with sample_data.py because you cannot write to it currently
    # This functionality will be used with the mongoDB
    def post(self, student_id):
        # Update the major_id for the student by student_id
        try:
            # Parse incoming JSON data
            data = request.json
            major_id = data.get("major_id")
            if major_id is None:
                return {"error": "No major ID provided."}, 400
            
            # Find the student
            student = next((s for s in sample_data.students if s["_id"] == student_id), None)
            if not student:
                return {"error": f"Student with ID {student_id} not found."}, 404
            
            # Validate the major id
            major = next((m for m in sample_data.majors if m["_id"] == major_id), None)
            if not major:
                return {"error": f"Major with ID {major_id} not found."}, 404
            
            # Update the student's major
            student["major_id"] = major_id

            return {"message": "Student major successfully.", "student": student}, 200
        
        except Exception as e:
            current_app.logger.error("Error updating student major: %s", str(e))
            return {
                "error": "An error occurred while updating the student major.",
                "message": str(e)
            }, 500
            
        
