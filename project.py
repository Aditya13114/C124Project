from flask import Flask,jsonify, request

app = Flask(__name__)

tasks = [
    {
        'Contact': 8849665317,
        'name': "Aditya",
        'done': False, 
        'id': 1
    },
    {
        'Contact': 9716180961,
        'name': "Alpana",
        'done': False, 
        'id': 2,
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    task = {
        'Contact': request.json['Contact'],
        'name': request.json['name'],
        'done': request.json.get('done', ""),
        'id': tasks[-1]['id'] + 1,
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message": "Task added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : tasks
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)