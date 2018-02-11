from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def run_homepage():
    template='firstPage.html'
    return render_template(template)

@app.route('/mentorSignup')
def mentorCompany():
    template='mentorSignin.html'
    return render_template(template)

@app.route('/menteesignup')
def menteeSignup():
    template='templates/newmenteeform.html'
    return render_template(template)

@app.route('/menteeSchoolval')
def menteeSchoolval():
    template='templates/mstudentemailpage.html'
    return render_template(template)

@app.route('/login')
def login():
    template='templates/login.html'
    return render_template(template)

@app.route('/mentorinitForm')
def mentorForm():
    template='templates/mentorForm.html'
    return render_template(template)

@app.route('/menteeinitForm')
def menteeForm():
    template='temlates/newmenteeform.html'
    return render_template(template)


if __name__ == "__main__":
    app.run()