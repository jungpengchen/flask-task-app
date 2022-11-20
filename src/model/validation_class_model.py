from flasgger import fields, Schema
from marshmallow.validate import Length, OneOf, Range
class CreateTaskRequest(Schema):
    name = fields.String(required=True, validate=Length(min=1), example="name") 
class Task(CreateTaskRequest):
    id = fields.Int(required=True, validate=Range(min=1))
    status = fields.Int(required=True, validate=OneOf([0,1]))
task_template = Task().dump({'id':1, 'name':'name', 'status': 0})