#Sir you should watch re zero
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

with open('data.json') as f:
    data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!' 
@app.route('/students') 
def get_students():
  result = []
  pref = request.args.get('pref') 
  if pref:
    for student in data: 
      if student['pref'] == pref: 
        result.append(student) 
    return jsonify(result) 
  return jsonify(data)
    
  #Watch Re-zero sir its amazing  
# route variables
@app.route('/students/<id>') 
def get_student(id):
  for student in data: 
    if student['id'] == id: # filter out the students without the specified id
      return jsonify(student)

def hello_name(fname, lname):
    return 'Hello ' + fname + ' ' + lname

@app.route('/hello/string/<fname>/<lname>')
def hello_string(fname, lname):
    return hello_name(fname, lname)




@app.route('/stats')
def get_student_count():
    Chicken = 0
    Vegetable = 0
    Fish = 0
    Computer = 0
    InformationTechnology = 0
    Information = 0
    ComputerScience = 0
    for student in data:
        if student['pref'] == 'Chicken':
            Chicken+=1
        elif student['pref'] == 'Fish':
            Fish+=1
        elif student['pref'] == 'Vegetable':
            Vegetable+=1
            
        if student['programme'] == 'Computer Science (Major)':
            Computer+=1
        elif student['programme'] == 'Information Technology (Special)':
            InformationTechnology+=1
        elif student['programme'] == 'Information Technology (Major)':
            Information+=1
        elif student['programme'] == 'Computer Science (Special)':
            ComputerScience+=1

    return jsonify({
        "Chicken": Chicken,
        "Computer Science (Major)": Computer,
        "Computer Science (Special)": ComputerScience,
        "Fish": Fish,
        "Information Technology (Major)": Information,
        "Information Technology (Special)": InformationTechnology,
        "Vegetable": Vegetable,
    })

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return jsonify (a + b)

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return jsonify (a - b)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return jsonify (a * b)

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    return jsonify (a / b)
    
app.run(host='0.0.0.0', port=8080, debug=True)
