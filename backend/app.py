from flask import Flask, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)


# Sample data (majors)
majors = [
    {
        "_id": 1, 
        "name": "Computer Science - B.S.", 
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
        "name": "Mechanical Engineering - B.S.", 
        "number_credits": 12,
        "plan": {
            "year_1": {
                "fall": ["CHEM 101", "MATH 151", "ENES 101 Y/H", "ENGL GEP", "AH GEP"],
                "winter": [],
                "spring": ["CHEM 102", "CHEM 102L", "PHYS 121", "MATH 152", "ENME 110"],
                "summer": [],
            },

            "year_2": {
                    "fall": ["ENME 220", "STAT 355", "MATH 251", "PHYS 122"],
                    "winter": [],
                    "spring": ["ENME 221", "MATH 225", "ENME 204", "ENME 217", "AH GEP"],
                    "summer": [],
                },

            "year_3": {
                    "fall": ["CMPE 306", "ENME 320", "ENME 303", "ENME 301", "SS GEP"],
                    "winter": [],
                    "spring": ["ENME 304", "ENME 321", "ENME 360", "ENME 332L", "Foreign Language 201"],
                    "summer": [],
                },
            
            "year_4": {
                    "fall": ["ENME 403", "ENME 432L", "Science/Technical elective" ,"ENME 4XX", "SS GEP", "AH GEP"],
                    "winter": [],
                    "spring": ["ENME 482L", "ENME 444", "ENME 4XX", "ENME 332L", "SS GEP","C GEP"],
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
