from dbhelper import DBHelper
from flask import Flask, render_template, request

app = Flask(__name__)
dbHelper = DBHelper()


@app.route("/")
def home():
    try:
        descriptionData = dbHelper.select_all()
    except Exception as e:
        print e
        descriptionData = None
    return render_template("home.html")


@app.route('/add', methods=['POST'])
def add():
    try:
        userinput = request.form.get('userinput')
        dbHelper.insert(des=userinput)
    except Exception as e:
        print e
    return home()


@app.route('/clear')
def clear():
    try:
        dbHelper.delete_all()
    except Exception as e:
        print e
    return home()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
