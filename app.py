from flask import Flask, request, jsonify
from pymongo import MongoClient

app=Flask(__name__)
client=MongoClient('mongodb://localhost:27017/')
db=client['employeedb']
collection=db['employees']

def format_employee(employee):
    employee['_id']=str(employee['_id'])
    return employee

@app.route('/api/employee', methods=['GET'])
def get_employees():
    empid=request.args.get('empid')
    if empid:
        employee=collection.find_one({'empid': int(empid)})
        if employee:
            return jsonify(format_employee(employee)), 200
        return jsonify({'error': 'No employee found'}), 404
    else:
        employees=list(collection.find())
        if employees:
            return jsonify([format_employee(emp) for emp in employees]), 200
        else:
            return jsonify({'error': 'No employees found'}), 404
    
@app.route('/api/employee',methods=['POST'])
def add_employees():
    data=request.json
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)
    return jsonify({'message': 'Employee data inserted'})

@app.route('/api/employee',methods=['PUT'])
def update_employee():
    empid=request.args.get('empid')
    data=request.json

    if empid:
        result=collection.update_one({'empid': int(empid)},{'$set': data})
        if result.matched_count:
            return jsonify({"message": "Employee details updated"}), 200
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify({'error': 'Empid missing'}), 400

@app.route('/api/employee', methods=['DELETE'])
def delete_employee():
    empid=request.args.get('empid')
    if empid:
        result=collection.delete_one({'empid': int(empid)})
        if result.deleted_count:
            return jsonify({"message": "Employee deleted"}), 200
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify({'error': 'Empid missing'}), 400

if __name__ =='__main__':
    app.run(debug=True)