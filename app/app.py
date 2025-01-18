from flask import Flask, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from models import db, Bank, Branch
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from werkzeug.exceptions import HTTPException
import time  
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Saikrishna2005@localhost:5432/bankdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

class BankSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Bank
        load_instance = True

class BranchSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Branch
        load_instance = True

@app.before_request
def before_request():
    g.start_time = time.time()

@app.after_request
def after_request(response):
    duration = time.time() - g.start_time
    response.headers['X-Duration'] = str(duration)
    return response

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }).data
    response.content_type = "application/json"
    return response

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Bank API!"})

@app.route('/api/branches', methods=['GET'])
def get_branches():
    query = Branch.query
    q = request.args.get('q')
    if q:
        query = query.filter(
            (Branch.branch.ilike(f'%{q}%')) |
            (Branch.address.ilike(f'%{q}%')) |
            (Branch.city.ilike(f'%{q}%')) |
            (Branch.district.ilike(f'%{q}%')) |
            (Branch.state.ilike(f'%{q}%'))
        )
    branches = query.all()
    branch_schema = BranchSchema(many=True)
    return jsonify(branch_schema.dump(branches))

@app.route('/api/branches/autocomplete', methods=['GET'])
def autocomplete_branches():
    query = Branch.query
    q = request.args.get('q')
    if q:
        query = query.filter(Branch.branch.ilike(f'%{q}%'))
    branches = query.all()
    branch_schema = BranchSchema(many=True)
    return jsonify(branch_schema.dump(branches))

@app.route('/api/banks', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    bank_schema = BankSchema(many=True)
    return jsonify(bank_schema.dump(banks))

@app.route('/api/branches/branch', methods=['GET'])
def get_branch_details():
    ifsc = request.args.get('ifsc')
    bank_id = request.args.get('bank_id')
    branch_name = request.args.get('branch')
    
    query = Branch.query
    if ifsc:
        query = query.filter(Branch.ifsc == ifsc)
    if bank_id:
        query = query.filter(Branch.bank_id == bank_id)
    if branch_name:
        query = query.filter(Branch.branch.ilike(f'%{branch_name}%'))

    branch = query.first()
    if not branch:
        return jsonify({"error": "Branch not found"}), 404

    branch_schema = BranchSchema()
    return jsonify(branch_schema.dump(branch))

if __name__ == '__main__':
    app.run(debug=True)
