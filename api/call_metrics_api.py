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
    "/api/call-metrics",
    methods=["POST"]
)
def create_call_metric():

    payload = request.get_json(silent=True) or {}

    result = CallMetricsService.create_call_metric(payload)

    return jsonify(result), 201
