from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'YOUR DATABASE_URI HERE'


db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    time_ = db.Column(db.Integer)

    def __init__(self, email_, time_):
        self.email_ = email_
        self.time_ = time_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form["email_name"]
        commuteTime = request.form["commuteTime_name"]
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, commuteTime)
            db.session.add(data)
            db.session.commit()
            average_time = db.session.query(func.avg(Data.time_)).scalar()
            average_time = round(average_time, 1)
            count = db.session.query(Data.time_).count()
            send_email(email, commuteTime, average_time, count)
            return render_template("success.html")
    return render_template('index.html',
                           text="Oops! Seems like email address entered has been used already!")


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)