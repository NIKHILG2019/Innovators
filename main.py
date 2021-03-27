from flask import Blueprint, render_template, request
from . import db
from .model import Company
from flask_login import login_required, current_user
main = Blueprint("main", __name__)


@main.route("/dashboard")
@login_required
def index():
    list_of_companies = db.session.query(Company).all()
    for instatnce in list_of_companies:
        print(instatnce.company_name)
    return render_template('dashboard.html', data=list_of_companies)



@main.route("/subtopic")
@login_required
def subtopic():
    return render_template('subtopic.html')


@main.route("/exam")
@login_required
def exam():
    return render_template('exam2.html')




@main.route("/company", methods=['POST'])
@login_required
def company_post():
    data = Company.query.filter_by(company_name=request.form.get('company')).first()
    print(data.company_name)
    return render_template('company_new.html', data=data)


@main.route("/profile")
@login_required
def profile():
    return current_user.first_name
