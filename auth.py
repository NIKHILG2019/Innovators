from flask import Blueprint, render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from .model import User, Company
from flask_login import login_user, logout_user, login_required
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/")
def login():
    return render_template('login.html')


@auth.route("/login", methods=['POST'])
def login_post():
    email = request.form.get('email')
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, request.form.get('password')):
            login_user(user, remember=True)
            return redirect(url_for('main.index'))
        else:
            flash("Incorrect password pls try again")
            return redirect(url_for('auth.login'))
    else:
        flash("Invalid username pls try again")
        return redirect(url_for('auth.login'))


@auth.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("Successfully Logged out")
    return redirect(url_for('auth.login'))


@auth.route('/signup')
def sign_up():
    return render_template('register.html')


@auth.route('/signup', methods=['POST'])
def sign_up_post():
    if User.query.filter_by(email=request.form.get('email')).first():
        flash('Your Email is Registered with us')
        return redirect(url_for('auth.login'))
    new_user = User(request.form.get('first_name'), request.form.get('last_name'), request.form.get('email'),
                    generate_password_hash(request.form.get('password')), request.form.get('contact_no'))
    db.session.add(new_user)
    db.session.commit()
    flash("Successfully Registered Please Login to Continue")
    return redirect(url_for('auth.login'))


@auth.route("/createcompany")
def create_company():
    new_company = Company('Infosys',
                          {
    "company_image_url":"https://www.infosys.com/content/dam/infosys-web/en/global-resource/media-resources/infosys-nyn-tagline-jpg.jpg",
    "about_company" : " Infosys Limited is an Indian multinational corporation that provides business consulting, information technology and outsourcing services. It has its headquarters in Bangalore, Karnataka, India.Infosys helps clients in 45 countries to create and execute different strategies for their digital transformation. Infosys helps businesses to renew & improve existing conditions so that their business can achieve higher efficiencies and stay relevant according to current times.Infosys is also famous for its the best IT training in the world, with lavish center in Mysore. Every year infosys intake thousands of students in bulk, train them for 6 months paid training in Mysore and then, on the basis of performance and preference allocate them centers across country with varied profiles.",
    "overview_company" : "Infosys begins its on-campus recruitments from early September. During July and August, they continue with their off-campus activities. If you fail in the first attempt, you can retake the exam after one month’s time. You can reappear for the certification examination after a month. However, upon two unsuccessful attempts, you will need to wait for 3 months to reappear for the next attempt. The level of exam is moderate to difficult.",
    "eligibility_criteria":" If you are dreaming of working with Infosys, you are at the right place. Infosys is one of the top recruiters in India in the field of information technology, therefore it is imperative for the aspirants to know the company's eligibility criteria. Read on to find out Infosys selection policies, graduation criteria, academic criteria and documents needed for applying for the positions of Systems Engineer Trainee / Software Engineer trainee at Infosys. Infosys Off Campus Recruitment has same eligibility criteria.",
    "graduation criteria" : "1) B.E / B.Tech  in any discipline (CSE/ECE/IT/CIVIL/ME/EEE/Automobile/Aeronautical etc. 2) M.Sc graduates in Computer Science/ Information technology can apply. 3) MCA graduates are also eligible to apply.",
    "academic criteria" : "1) A candidate must have more than 60% marks in 10th and 12th (or diploma). 2) A candidate must have a minimum of 65% marks or CGPA 6.5 in graduation. 3) A maximum of 2 years of gap is permissible in the entire education. 4) A candidate should not have any pending backlogs at the time of appearing for Infosys selection process.",
    "selection process" : "Infosys has a simple process of online aptitude test followed by technical interview of the shortlisted candidate. The profile is usually of System Engineers with 3.6 LPA package. Infosys does have a bond of 1 year after the training is over of 1.25 LPA as amount against it. The training is in Mysore with facilities of hostel, mess etc. and you would get around 13K-14K in hand. The aptitude test result is declared after 3-4 hours followed by technical interview the very next day. INTERVIEW Technical Interview The questions are entirely based on the technologies mentioned in the Job Description. The candidate might be asked to write a piece of code, or an algorithm to demonstrate the knowledge required in the particular field. Questions might also be based on the tools and technologies used in past projects HR Interview It helps to determine a candidate's personality. Questions can be of wide range starting from your introduction, Qualification, Experience, Industry specific experience, Courses done, your strengths and weaknesses, salary expectations, friends, family etc. . Be ready to take questions based on your CV - internships, projects, volunteerships and co-curricular activities.Never say No when interviewer asks - Do you have any questions for me? Ask about company's culture and progress associated or something you wnat to know.",
    "pattern" : "Infosys Recruitment process includes a selection stage when decisions are made as to the viability of a particular candidate's job application.The process of selecting candidates focuses on abilities, knowledge, skills, experience and various other related factors.Infosys Test Papers and Infosys Sample Papers are of moderate to high in difficulty level.Stages of selection process to get recruited in Infosys: Online Aptitude Test Infosys Interview Process Technical Round HR Round There is no negative marking. There is sectional cut off (60-70% approx)."
}

                          )
    db.session.add(new_company)
    db.session.commit()
    return "Successfully added company"
