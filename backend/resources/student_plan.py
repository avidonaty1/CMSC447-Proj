from flask import current_app, request
from flask_restful import Resource
import sample_data
from utils.utility_functions import build_nested_plan

class StudentPlan(Resource):
    """
    StudentPlan Resource
    Handles fetching or updating the student's custom_plan attribute by ID (looks for the _id attribute)
    """
    # Supports GET requests for fetching the custom_plan
    def get(self, student_id):
        try:
            # Fetch the custom_plan for the student_id
            student = next((s for s in sample_data.students if s['_id'] == student_id), None)

            # Handle error for no matching student _id
            if not student:
                return {"error": f"Student with ID {student_id} not found."}, 404
            
            # Otherwise, build a nested plan from the custom plan
            # The custom plan may be an empty dictionary if the student has not selected a major
            custom_plan_raw = student.get("custom_plan", {})
            nested_plan = build_nested_plan(custom_plan_raw)
            return {"student_id": student_id, "custom_plan": nested_plan}, 200
        
        except Exception as e:
            # Log the exception for debugging
            current_app.logger.error("Error retrieving student plan: %s", str(e))
            return {
                "error": "An error occurred while retrieving custom plan for student.",
                "message": str(e)
            }, 500
        
    # Supports POST requests for updating the custom_plan
    # Note this DOES NOT WORK with sample_data.py because you cannot write to it currently
    # This functionality will be used with the mongoDB
    def post(self, student_id):
        # Update the custom_plan for the student_id
        try:
            # Parse incoming JSON data
            data = request.json
            plan = data.get("custom_plan")
            if plan is None:
                return {"error": "No plan data provided."}, 400
            
            # Validate the structure of the custom_plan
            if not isinstance(plan, dict):
                return {"error": "Invalid format of plan data."}, 400
            
            # Find the student
            student = next((s for s in sample_data.students if s["_id"] == student_id), None)
            if not student:
                return {"error": f"Student with ID {student_id} not found."}, 404
            
            # Update the student's custom plan
            student["custom_plan"] = plan

            return {"message": "Student plan updated successfully.", "student": student}, 200
        
        except Exception as e:
            current_app.logger.error("Error updating student plan: %s", str(e))
            return {
                "error": "An error occurred while updating the student plan.",
                "message": str(e)
            }, 500
            
        
