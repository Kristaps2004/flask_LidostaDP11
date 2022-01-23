from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Todo(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  content = db.Column(db.String(200), nullable = False)
  date_created = db.Column(db.DateTime, default = datetime.utcnow)

  def __repr__(self):
    return 'Task %r' %self.id

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/admin')
def admin():
  return render_template("admin.html")

@app.route('/izvele')
def izvele():
  return render_template("izvele.html")

@app.route('/rezervacijas')
def rezervacijas():
  return render_template("rezervacijas.html")

@app.route('/statistika')
def statistika():
  return render_template("statistika.html")

@app.route('/admin/lidostas')
def lidostas():
  return render_template("adminlidostas.html")

@app.route('/admin/lidmasinas')
def lidmasinas():
  return render_template("adminlidmasinas.html")

@app.route('/admin/reisi')
def reisi():
  return render_template("adminreisi.html")

if __name__ == "__main__": 
  app.run(host='0.0.0.0', port=8000)