"""Root Endpoints"""
from flask import Blueprint, jsonify

home_blueprint = Blueprint("home", __name__, url_prefix="/")


@home_blueprint.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to CAVE"}), 200
