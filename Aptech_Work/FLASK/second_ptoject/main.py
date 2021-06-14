from flask import Flask, render_template , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:80/db_flask_aptech'
db = SQLAlchemy(app)

class Contact(db.Model):
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(233), nullable=False)
    phone = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        nametxt = request.form.get('name')
        emailtxt = request.form.get('email')
        phonetxt = request.form.get('phone')
        messagetxt = request.form.get('message')
        entry = Contact(name=nametxt, email=emailtxt, phone=phonetxt, message=messagetxt)
        db.session(entry)
        db.session.commit()

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)