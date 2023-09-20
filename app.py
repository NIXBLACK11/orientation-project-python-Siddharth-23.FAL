'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill
from utils import validate_index

app = Flask(__name__)

data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify()

    if request.method == 'POST':
        request_data = request.get_json()
        experience_data = Experience(**request_data)
        data["experience"].append(experience_data)
        index = len(data["experience"]) - 1
        return jsonify({"id": index})

    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})

@app.route('/resume/education/<id>', methods=['DELETE'])
def specific_education(id):
    '''
    Handles specific Education requests
    '''
    if not validate_index(id, len(data["skill"])):
        return jsonify({"error": f"Education entry {id} not found"}), 404
    if request.method == 'DELETE':
        index = int(id)
        data["skill"] = data["skill"][:index][index+1:]
        return jsonify({"inf": "Education entry {id} has been deleted"}), 204
