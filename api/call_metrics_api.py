from flask import Blueprint, jsonify

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