from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    first_name = db.Column(db.VARCHAR(20), nullable=False)
    last_name = db.Column(db.VARCHAR(20), nullable=False)
    email = db.Column(db.VARCHAR(80), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(300), nullable=False)
    mobile_number = db.Column(db.BIGINT, nullable=False)

    def __init__(self, first_name, last_name, email, password, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_number = mobile_number


class Company(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    company_name = db.Column(db.VARCHAR(50), nullable=False)
    feedback_work_life_balance = db.Column(db.INTEGER, nullable=False, default=0)
    feedback_types_of_project = db.Column(db.INTEGER, nullable=False, default=0)
    feedback_work_culture = db.Column(db.INTEGER, nullable=False, default=0)
    feedback_pay = db.Column(db.INTEGER, nullable=False, default=0)
    number_of_feedback = db.Column(db.INTEGER, nullable=False, default=0)
    company_data = db.Column(db.JSON, nullable=False)

    def __init__(self, company_name, company_data):
        self.company_name = company_name,
        self.company_data = company_data


class Review(db.Model):
    id = db.Column(db.INTEGER, autoincrement=True, primary_key=True, nullable=False)
    company_id = db.Column(db.INTEGER, db.ForeignKey('company.id'))
    user_id = db.Column(db.INTEGER, db.ForeignKey('user.id'))

    def __init__(self, user_id, company_id):
        self.user_id = user_id
        self.company_id = company_id
