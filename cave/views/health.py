from flask import jsonify, Blueprint


health_blueprint = Blueprint("health", __name__, url_prefix="/health")


@health_blueprint.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok"}), 200
