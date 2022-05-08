import flask
from flask import request, jsonify
import json
def main():
    if not request.json:
        abort(400)
    jsonBody = request.json["Node Test"]
    return jsonify({'Server is Up'}), 200
