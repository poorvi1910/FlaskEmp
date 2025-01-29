from flask import request, jsonify
from pymongo import MongoClient
from schema import EmployeeSchema
from pydantic import ValidationError

client = MongoClient('mongodb://localhost:27017/')
db = client['employeedb']
collection = db['employees']

def format_employee(employee):
    employee['_id'] = str(employee['_id'])
    return employee

def api_routes(app):

    @app.route('/api/employee', methods=['GET'])
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

    @app.route('/api/employee', methods=['POST'])
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

    @app.route('/api/employee', methods=['PUT'])
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

    @app.route('/api/employee', methods=['DELETE'])
    def delete_employee():
        empid = request.args.get('empid')
        if empid:
            result = collection.delete_one({'empid': int(empid)})
            if result.deleted_count:
                return jsonify({"message": "Employee deleted"}), 200
            return jsonify({'error': 'Employee not found'}), 404
        return jsonify({'error': 'Empid missing'}), 400
