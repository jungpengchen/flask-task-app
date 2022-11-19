#!/usr/local/bin/python3
import os
from flask import Flask, request

FLASK_DEBUG = bool(os.getenv("FLASK_DEBUG", "1"))
app = Flask(__name__)

task_max_id = 0
task_id_dict = {}
task_template = {'id':1, 'name':'name', 'status': 0}

@app.route('/tasks', methods=['GET'])
def list_task():
    if not len(task_id_dict):
        result_list = [task_template]
    else:
        result_list = [task_id_dict[i] for i in task_id_dict.keys()]
    return {"result": result_list}

@app.route('/task', methods=['POST'])
def create_task():
    global task_max_id, task_id_dict
    name = request.values.get('name')
    new_task = task_template.copy()
    new_task['id'] = task_max_id = task_max_id+1
    new_task['name'] = name
    task_id_dict[new_task['id']] = new_task
    return {"result": new_task}, 201

@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    global task_max_id, task_id_dict
    new_name = request.values.get('name')
    new_status = request.values.get('status')
    new_task_id = request.values.get('id')
    task_id_dict[new_task_id] = new_task = task_id_dict[task_id].copy()
    new_task['new_name'], new_task['new_status'], new_task['id'] = new_name, new_status, new_task_id
    if new_task_id != task_id:
        del task_id_dict[task_id]
        task_max_id = max(task_id_dict.keys())
    else:
        pass
    return {"result": new_task}

    
@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global task_max_id, task_id_dict
    del task_id_dict[task_id]
    task_max_id = max(task_id_dict.keys())
    return

if __name__ == '__main__':
    app.run(debug=FLASK_DEBUG, host='0.0.0.0',port=8080,threaded=FLASK_DEBUG)