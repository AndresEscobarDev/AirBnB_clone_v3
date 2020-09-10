#!/usr/bin/python3
"""
States handler for all default RestFul API
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<string:state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """Retrieve all cities from a State"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    cities_by_state = [v.to_dict() for v in storage.all(
        City).values() if v.state_id == state_id]
    """cities = storage.all(City)
    for v in cities.values():
        if v.state_id == state_id:
            cities_by_state.append(v.to_dict())"""
    return jsonify(cities_by_state)


@app_views.route('/cities/<string:city_id>',
                 methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Retrieve a City by ID"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<string:city_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """ Deletes a city """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    city.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<string:state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def post_city(state_id):
    """ Create a city """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    update_dict = request.get_json()
    update_dict['state_id'] = state_id
    city = City(**update_dict)
    city.save()
    return make_response(jsonify(city.to_dict()), 201)


@app_views.route('/cities/<string:city_id>',
                 methods=['PUT'], strict_slashes=False)
def put_city(city_id):
    """ Update a city """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at', 'state_id']:
            setattr(city, key, value)
    city.save()
    return make_response(jsonify(city.to_dict()), 200)
