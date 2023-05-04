from flask_restful import Api, Resource, reqparse

class SampleApi(Resource):
    def get(self):
        data = {
            'resultStatus': 'SUCCESS',
            'message': "h"
        }
        return data

    def post(self):
        pass # sends data to server
