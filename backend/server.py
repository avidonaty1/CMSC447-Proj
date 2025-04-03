from flask import Flask, send_from_directory
from flask_restful import Api
from resources.title import Title
from resources.majors import Majors

app = Flask(__name__, static_folder="../frontend/simple-planner-app/dist", static_url_path="/")
api = Api(app)

# Resource for the title
api.add_resource(Title, '/api/v1/title')
# Resource for the list of majors
api.add_resource(Majors, '/api/v1/majors')

# Flask will serve React
@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    app.run(debug=True)