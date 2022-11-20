#!/usr/local/bin/python3
import os, threading
from flasgger import Swagger, swag_from
from flask import Flask, request
from model.validation_class_model import CreateTaskRequest, Task, task_template
from model.swagger_spec_model import list_task_spec, create_task_spec, update_task_spec, delete_task_spec

FLASK_DEBUG = bool(os.getenv("FLASK_DEBUG", "1"))
FLASK_APP_PORT = int(os.getenv("FLASK_APP_PORT", "5000"))
SWAGGER_ON = bool(int(os.getenv("SWAGGER_ON", "1")))
app = Flask(__name__)
Swagger(app) if SWAGGER_ON else None

task_max_id = 0 #change to redis server when multiple api servers
task_id_dict = {} #write records to DB when multiple api servers
lock = threading.RLock() #change to redis lock with multiple api servers

def init_task_list():
    global task_max_id, task_id_dict, lock
    lock.acquire()
    task_max_id = 0
    task_id_dict.clear()
    lock.release()

@app.route('/tasks', methods=['GET'])
@swag_from(list_task_spec)
def list_task():
    if not len(task_id_dict):
        result_list = [task_template]
    else:
        result_list = [task_id_dict[i] for i in task_id_dict.keys()]
    return {"result": result_list}

@app.route('/task', methods=['POST'])
@swag_from(create_task_spec)
def create_task():
    global task_max_id, task_id_dict, lock
    request_json = request.get_json()
    name = CreateTaskRequest().dump(request_json)['name']
    new_task = task_template.copy()
    lock.acquire()
    new_task['id'] = task_max_id = task_max_id+1
    new_task['name'] = name
    task_id_dict[new_task['id']] = new_task
    lock.release()
    return {"result": new_task}, 201

@app.route('/task/<int:task_id>', methods=['PUT'])
@swag_from(update_task_spec)
def update_task(task_id: int):
    global task_max_id, task_id_dict, lock
    request_json = request.get_json()
    task = Task().dump(request_json)
    lock.acquire()
    if task_id not in task_id_dict:
        return f"task id {task_id}(type: {type(task_id)}) not in {task_id_dict.keys()}", 404
    task_id_dict[task['id']] = task
    if task['id'] != task_id:
        del task_id_dict[task_id]
        task_max_id = max(task_id_dict.keys())
    else:
        pass
    lock.release()
    return {"result": task}
    
@app.route('/task/<int:task_id>', methods=['DELETE'])
@swag_from(delete_task_spec)
def delete_task(task_id: int):
    global task_max_id, task_id_dict, lock
    lock.acquire()
    if task_id not in task_id_dict:
        return f"task id {task_id}(type: {type(task_id)}) not in {task_id_dict.keys()}", 404
    del task_id_dict[task_id]
    task_max_id = max(task_id_dict.keys()) if len(task_id_dict) else 0
    lock.release()
    return 'OK'

def main(app):
    app.run(debug=FLASK_DEBUG, host='0.0.0.0',port=FLASK_APP_PORT,threaded=True)

if __name__ == '__main__':
    main(app)