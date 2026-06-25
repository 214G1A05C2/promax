from flask import Blueprint, jsonify, request

from services.call_metrics_service import (
    CallMetricsService
)

call_metrics_bp = Blueprint(
    "call_metrics_bp",
    __name__
)

@call_metrics_bp.route(
    "/api/call-metrics",
    methods=["GET"]
)
def get_call_metrics():

    data = CallMetricsService.fetch_all_calls()

    return jsonify(data)


@call_metrics_bp.route(
    "/api/call-metrics/<int:call_id>",
    methods=["GET"]
)
def get_call_metric(call_id):

    result, status_code = CallMetricsService.fetch_call_by_call_id(call_id)

    return jsonify(result), status_code


@call_metrics_bp.route(
    "/api/call-metrics",
    methods=["POST"]
)
def create_call_metric():

    payload = request.get_json(silent=True) or {}
    if not isinstance(payload, dict):
        return jsonify({
            "success": False,
            "message": "Request body must be a JSON object.",
        }), 400

    result = CallMetricsService.create_call_metric(payload)

    return jsonify(result), 201


@call_metrics_bp.route(
    "/api/call-metrics/<int:call_id>",
    methods=["DELETE"]
)
def delete_call_metric(call_id):

    result = CallMetricsService.delete_call_metric(call_id)

    status_code = 200 if result.get("deleted") else 404

    return jsonify(result), status_code
