from model.validation_class_model import task_template
shared_def = \
    {
        "Task":{
                "type": "object",
                "properties":{
                    "id":{
                        "type": "integer"
                    },
                    "name":{
                        "type": "string"
                    },
                    "status":{
                        "type": "integer"
                    },
                }
        },
        "CreateTaskRequest":{
                "type": "object",
                "properties":{
                    "name":{
                        "type": "string"
                    }
                }
        },
        "ListTaskResponse":{
                "type": "object",
                "properties":{
                    "result":{
                        "type": "array",
                        "items": {"$ref": "#/definitions/Task"}
                    },
                }
        },
        "CreateTaskResponse":{
                "type": "object",
                "properties":{
                    "result": {"$ref": "#/definitions/Task"}
                }
        }
    }
list_task_spec = {
        "description": "list tasks",
        "definitions": shared_def,
        "responses":{
            200:{"description":"success request",
                "schema": {"$ref":"#/definitions/ListTaskResponse"}},
            400:{"description":"Validation error"}}}
create_task_spec = {
        "description": "create task",
        "definitions": shared_def,
        "consumes": ["application/json"],
        "parameters":[{"name":"task",
                    "in": "body",
                    "required": True,
                    "schema": {"$ref": "#/definitions/CreateTaskRequest"},
                    "examples":{"name":"name"}}],
        "responses":{
            201:{"description":"Success request",
                "schema": {"$ref":"#/definitions/CreateTaskResponse"}},
            400:{"description":"Validation error"}}}
update_task_spec = {
        "description": "update task",
        "definitions": shared_def,
        "consumes": ["application/json"],
        "parameters":[
            {"name":"task_id",
                    "in": "path",
                    "type": "integer",
                    "required": True,
                    "description": "id of created task",
                    "examples": 1},
            {"name":"task",
                    "in": "body",
                    "required": True,
                    "schema": {"$ref": "#/definitions/Task"},
                    "examples":task_template}],
        "responses":{
            201:{"description":"Success request",
                "schema": {"$ref":"#/definitions/CreateTaskResponse"}},
            400:{"description":"Validation error"}}}
delete_task_spec = {
        "description": "delete task",
        "parameters":[
            {"name":"task_id",
                    "in": "path",
                    "type": "integer",
                    "required": True,
                    "description": "id of created task",
                    "examples": 1}],
        "responses":{200:{"description":"Success request"},
                    400:{"description":"Validation error"}}}