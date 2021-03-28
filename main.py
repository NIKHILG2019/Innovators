from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .model import Company, Review
from flask_login import login_required, current_user
main = Blueprint("main", __name__)


@main.route("/dashboard")
@login_required
def index():
    list_of_companies = db.session.query(Company).all()
    for instance in list_of_companies:
        print(instance.company_name)
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
    feedback_toggle = False
    work_life_balance = 0
    work_culture = 0
    pay = 0
    types_of_project = 0
    button_toggle = True
    data = Company.query.filter_by(company_name=request.form.get('company')).first()
    review_list = Review.query.filter_by(company_id=data.id).all()
    for instance in review_list:
        if instance.user_id == current_user.id:
            button_toggle = False
            break
    if int(data.number_of_feedback) != 0:
        feedback_toggle = True
        work_life_balance = ((int(data.feedback_work_life_balance)/5)/int(data.number_of_feedback))*100
        work_culture = ((int(data.feedback_work_culture) / 5) / int(data.number_of_feedback)) * 100
        pay = ((int(data.feedback_pay) / 5) / int(data.number_of_feedback)) * 100
        types_of_project = ((int(data.feedback_types_of_project) / 5) / int(data.number_of_feedback)) * 100
    return render_template('company_new.html', data=data, button_toggle=button_toggle, work_life_balance=work_life_balance, work_culture=work_culture, pay=pay, types_of_project=types_of_project, feedback=feedback_toggle)


@main.route("/profile")
@login_required
def profile():
    return current_user.first_name


@main.route("/feedback")
@login_required
def feedback():
    data = request.args.get('company_name')
    return render_template('feedback.html', data=data)


@main.route('/feedback', methods=['POST'])
@login_required
def feedback_post():
    data = Company.query.filter_by(company_name=request.form.get('company_name')).first()
    data.feedback_pay = int(data.feedback_pay) + int(request.form.get('pay'))
    data.feedback_work_life_balance = int(data.feedback_work_life_balance) + int(request.form.get('work_life_balance'))
    data.feedback_types_of_project = int(data.feedback_types_of_project) + int(request.form.get('types_of_projects'))
    data.feedback_work_culture = int(data.feedback_work_culture) + int(request.form.get('work_culture'))
    data.number_of_feedback = int(data.number_of_feedback) + 1
    new_review = Review(current_user.id, data.id)
    db.session.add(new_review)
    db.session.commit()
    return redirect(url_for('main.index'))


    # print(request.form.get('work_life_balance'))
    # print(request.form.get('types_of_projects'))
    # print(request.form.get('work_culture'))
    # print(request.form.get('pay'))
    # data.company_data["feedback_work_life_balance"] = str(int(data.company_data["feedback_work_life_balance"])+int(request.form.get('work_life_balance')))
    # data.company_data["feedback_types_of_project"] = str(int(data.company_data["feedback_work_life_balance"])+int(request.form.get('work_life_balance')))
    # data.company_data["feedback_work_culture"] = str(int(data.company_data["feedback_work_life_balance"])+int(request.form.get('work_life_balance')))
    # data.company_data["feedback_pay"] = str(int(data.company_data["feedback_work_life_balance"])+int(request.form.get('work_life_balance')))
    # data.company_data["number_of_feedback"] = str(int(data.company_data["number_of_feedback"]) + 1)
    # data.company_data["feedback_user_id"] = data.company_data["feedback_user_id"] + ","+current_user.email