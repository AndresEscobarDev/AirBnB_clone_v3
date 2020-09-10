#!/usr/bin/python3
"""
Module that holds, app_views stats
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """Endpoint that return the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """Endpoint that retrieves the number of each objects by type"""
    cls_dict = {"amenities": "Amenity",
                "cities": "City",
                "places": "Place",
                "reviews": "Review",
                "states": "State",
                "users": "User"}
    rtrn_dcit = {}
    for k, v in cls_dict.items():
        rtrn_dcit[k] = storage.count(v)
    return jsonify(rtrn_dcit)
