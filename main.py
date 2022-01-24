from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Lidosta(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  content = db.Column(db.String(200), nullable = False)
  saisinajums = db.Column(db.String(3), nullable = False)
  adrese = db.Column(db.String(200), nullable = False)
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

@app.route('/admin/lidmasinas')
def lidmasinas():
  return render_template("adminlidmasinas.html")

@app.route('/admin/lidostas', methods=['POST', 'GET'])
def lidostas():
  if request.method == 'POST':
    new_airport = Lidosta(content=request.form['content'],saisinajums = request.form['saisinajums'], adrese =request.form['adrese'])

    try:
      db.session.add(new_airport)
      db.session.commit()

      return redirect('/admin/lidostas')
    except:
      return "Draugi nav labi!"

  else:
    tasks = Lidosta.query.order_by(Lidosta.date_created).all()
    return render_template('adminlidostas.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
  task_to_delete = Lidosta.query.get_or_404(id)

  try:
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect('/admin/lidostas')

  except:
    return 'Brāl nesanāca izdzēst'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
  task = Lidosta.query.get_or_404(id)

  if request.method == 'POST':
    task.content = request.form['content']
    task.saisinajums = request.form['saisinajums']
    task.adrese = request.form['adrese']

    try:
      db.session.commit()
      return redirect('/admin/lidostas')
    except:
      return "Brāl nesanāca update"
  else:
    return render_template("update.html", task=task)

@app.route('/admin/reisi')
def reisi():
  return render_template("adminreisi.html")

if __name__ == "__main__": 
  app.run(host='0.0.0.0', port=8000)