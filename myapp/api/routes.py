from flask import request, jsonify, make_response
from pymongo import MongoClient
from myapp.schema import EmployeeSchema
from pydantic import ValidationError
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity, unset_jwt_cookies
from myapp.api import api_bp

client = MongoClient('mongodb://localhost:27017/')
db = client['employeedb']
collection = db['employees']

revoked_tokens = set()

def format_employee(employee):
    employee['_id'] = str(employee['_id'])
    return employee

limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"],
)

@api_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username', None)
    password = data.get('password', None)

    if username == 'admin' and password == 'admin':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid credentials"}), 401

@api_bp.route('/employee', methods=['GET'])
@limiter.limit("5 per minute")
@jwt_required()
def get_employees():
    empid = request.args.get('empid')
    if empid:
        employee = collection.find_one({'empid': int(empid)})
        if employee:
            return jsonify(format_employee(employee)), 200
        return jsonify({'error': 'No employee found'}), 404
    else:
        employees = list(collection.find())
        if employees:
            return jsonify([format_employee(emp) for emp in employees]), 200
        return jsonify({'error': 'No employees found'}), 404

@api_bp.route('/employee', methods=['POST'])
@limiter.limit("5 per minute")
@jwt_required()
def add_employees():
    data = request.json
    try:
        if isinstance(data, list):
            employees = [EmployeeSchema(**emp) for emp in data]
            collection.insert_many([emp.dict() for emp in employees])
        else:
            employee = EmployeeSchema(**data)
            collection.insert_one(employee.dict())
        return jsonify({'message': 'Employee data inserted'}), 201
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

@api_bp.route('/employee', methods=['PUT'])
@limiter.limit("5 per minute")
@jwt_required()
def update_employee():
    empid = request.args.get('empid')
    data = request.json
    try:
        if empid:
            employee = EmployeeSchema(**data)
            result = collection.update_one({'empid': int(empid)}, {'$set': employee.dict()})
            if result.matched_count:
                return jsonify({"message": "Employee details updated"}), 200
            return jsonify({'error': 'Employee not found'}), 404
        return jsonify({'error': 'Empid missing'}), 400
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

@api_bp.route('/employee', methods=['DELETE'])
@limiter.limit("5 per minute")
@jwt_required()
def delete_employee():
    empid = request.args.get('empid')
    if empid:
        result = collection.delete_one({'empid': int(empid)})
        if result.deleted_count:
            return jsonify({"message": "Employee deleted"}), 200
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify({'error': 'Empid missing'}), 400

@api_bp.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    current_user = get_jwt_identity()
    revoked_tokens.add(current_user)
    response = make_response(jsonify(msg="Successfully logged out"), 200)
    unset_jwt_cookies(response)
    return response