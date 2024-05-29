from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__) # create a blueprint used to define routes and views

@main.route('/api/data', methods=['GET']) # defines a route to endpoint
def get_data():
    return jsonify({"data": "example data"})  # call external API and return data
