from flask import Flask, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)


# Sample data (majors)
majors = [
    {
        "_id": 1, 
        "name": "Computer Science", 
        "number_credits": 12,
        "plan": {
            "freshman": {
                "fall": ["CMSC 201", "MATH 151", "ENGL GEP", "Foreign Lang 201"],
                "winter": [],
                "spring": ["CMSC 202", "MATH 152", "CMSC 203", "AH GEP", "SS GEP"],
                "summer": [],
            },
            "year_2": {
                    "fall": ["CMSC 331", "CMSC 341", "Science Se I", "SS GEP"],
                    "winter": [],
                    "spring": ["CMSC 313", "MATH 221", "Science Se II", "Science Lab"],
                    "summer": [],
                },
            "year_3": {
                    "fall": ["CMSC 304", "CMSC 411", "CMSC 4XX", "STAT 355"],
                    "winter": [],
                    "spring": ["CMSC 421", "CMSC 4XX", "CMSC 4XX", "AH GEP", "C GEP"],
                    "summer": [],
                },
            "year_4": {
                    "fall": ["CMSC 441", "CMSC 447", "Upper level Elective", "Elective", "Elective"],
                    "winter": [],
                    "spring": ["CMSC 4XX", "CMSC 4XX", "CMSC 4XX", "AH GEP", "C GEP"],
                    "summer": [],
                }
            }
    },

    {
        "_id": 2, 
        "name": "MECH E", 
        "number_credits": 12,
        "plan": {
            "year_1": {
                "fall": ["ENME h;", "ENME", "ENME", "Foreign Language 201"],
                "winter": [],
                "spring": ["ENME", "ENME e", "ENME v", "ENME", "ENME"],
                "summer": [],
            },
            "year_2": {
                    "fall": ["ENME 331", "ENME 341", "ENME", "ENME"],
                    "winter": [],
                    "spring": ["ENME 313", "ENME 221", "ENME", "ENME"],
                    "summer": [],
                }
        }
    }
]

courses = [
    {
        "name": "CMSC 202",
        "number_of_credits": 4,
        "description": "This course continues the student’s development of programming and problem-solving skills by providing an introduction to object-oriented design and programming (OOP). The primary focus is on OOP principles and techniques, including encapsulation, aggregation, inheritance, and polymorphism. Other OOP topics such as exception handling and templates are also covered. This is the second course for students interested in pursuing further study in computer science.",
        "prerequisites": ["CMSC 201", "MATH 151"]
    },
    {
        "name": "CMSC 201",
        "number_of_credits": 4,
        "description": "Introduction to programming using Python. This is the first course for students interested in pursuing further study in computer science.",
        "prerequisites": []
    }
]


# Route to serve the React app (static files)
@app.route('/api/majors')
def get_majors():
    return jsonify(majors)

@app.route('/api/major_details/<int:major_id>')
def get_major_details(major_id):
    major = next((m for m in majors if m["_id"] == major_id), None)
    if major:
        return jsonify(major)
    return jsonify({"error": "Major not found"}), 404

@app.route('/api/course/<string:course_name>')
def get_course(course_name):
    course = next((c for c in courses if c["name"] == course_name), None)
    if course:
        return jsonify(course)
    return jsonify({"error": "Course not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)
