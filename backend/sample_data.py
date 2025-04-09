from flask_restful import Resource
from flask import jsonify

# Define the majors collection
# This is a list of dictionaries, where each major is a dictionary
# with an id, name, number_credits
majors = [
    {
        "_id": 1,
        "name": "Computer Science",
        "number_credits": 12
    },
    {
        "_id": 2,
        "name": "Mechanical Engineering",
        "number_credits": 19
    },
    {
        "_id": 3,
        "name": "Mathematics",
        "number_credits": 19
    }
]

class Majors(Resource):
    def get(self):
        return jsonify(majors)  # Send the majors data as a JSON respons
