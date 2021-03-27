from . import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    first_name = db.Column(db.VARCHAR(20), nullable=False)
    last_name = db.Column(db.VARCHAR(20), nullable=False)
    email = db.Column(db.VARCHAR(80), nullable=False)
    password = db.Column(db.VARCHAR(300), nullable=False)
    mobile_number = db.Column(db.BIGINT, nullable=False)
    # email_confirmation_sent_on = db.Column(db.DATETIME, nullable=True)
    # email_confirmed = db.Column(db.Boolean, nullable=True, default=False)
    # email_confirmed_on = db.Column(db.DATETIME, nullable=True)

    def __init__(self, first_name, last_name, email, password, mobile_number, email_confirmation_sent_on):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_number = mobile_number
        # self.email_confirmation_sent_on = email_confirmation_sent_on
        # self.email_confirmed = False
        # self.email_confirmed_on = None


class Company(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    company_name = db.Column(db.VARCHAR(50), nullable=False)
    company_data = db.Column(db.JSON, nullable=False)

    def __init__(self, company_name, company_data):
        self.company_name = company_name,
        self.company_data = company_data
