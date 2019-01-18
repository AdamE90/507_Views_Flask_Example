# Import statements necessary
from flask import Flask, render_template
from flask_script import Manager

# Set up application
app = Flask(__name__)

manager = Manager(app)

# Routes

@app.route('/')
def hello_world():
    return render_template("hello_world.html")

@app.route('/user/<yourname>')
def hello_name(yourname):
    return render_template("hello_name.html", name=yourname)

@app.route('/showvalues/<name>')
def basic_values_list(name):
    lst = ["hello","goodbye","tomorrow","many","words","jabberwocky"]
    if len(name) > 3:
        longname = name
        shortname = None
    else:
        longname = None
        shortname = name
    return render_template('values.html',word_list=lst,long_name=longname,short_name=shortname)


if __name__ == '__main__':
    manager.run() # Runs the flask server in a special way that makes it nice to debug
