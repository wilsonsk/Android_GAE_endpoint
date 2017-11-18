from flask import Flask, render_template
from flask_restful import Resource, Api

class Houses(Resource):
        def get(self):
                return 'Hello GET houses'

        def delete(self):
                return 'Hello DELETE houses'

