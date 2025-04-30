# Future: import logging and set up custom logging
from flask import Flask, send_from_directory
from flask_restful import Api
from resources.majors import Majors
from resources.major_plan import MajorPlan
from resources.course_info import CourseInfo
from resources.course_requirements import CourseRequirements
from resources.student_email import StudentEmail
from resources.student_major import StudentMajor
from resources.student_plan import StudentPlan
# from flask_cors import CORS  


app = Flask(__name__, static_folder="../my-react-app/dist", static_url_path="/")
api = Api(app)
# CORS(app, origins=["http://localhost:5173"])

# Resource for retrieving the list of majors
api.add_resource(Majors, '/api/v2/majors')

# Resource for retrieving the default plan of a major (Years 1-4 and Sessions Fall, Winter, Spring and Summer)
api.add_resource(MajorPlan, '/api/v2/majors/<int:major_id>/plan')

# Resource for retrieving course details for a given course
api.add_resource(CourseInfo, '/api/v2/courses/<int:course_id>')

# Resource for retrieving the prerequisites and corequisistes for a course
api.add_resource(CourseRequirements, '/api/v2/courses/<int:course_id>/requirements')

# Resource for retrieving a student id by an email address (used for login)
# Future: add a new resource for retrieving email and password for login if 
# passwords are implemented 
api.add_resource(StudentEmail, '/api/v2/students/email/<string:email>')

# Resource for retrieving/updating a student major by student id
api.add_resource(StudentMajor, '/api/v2/students/<int:student_id>/major')

# Resource for retrieving/updating a students custom plan by student id
api.add_resource(StudentPlan, '/api/v2/students/<int:student_id>/plan')

# Flask will serve React
@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    app.run(debug=True)
