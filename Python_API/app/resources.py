from importlib import resources
from flask_restful import Resource, abort, fields, marshal_with, reqparse

from app import db
from .models import Course 

resource_fields = {
  'department': fields.String,
  'number': fields.Integer,
  'title': fields.String,
  'units': fields.Integer,
  'desc': fields.String
}

class CoursesResource(Resource):
  @marshal_with(resource_fields)
  def get(self):
    return Course.query.all(), 200