from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Lidosta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    saisinajums = db.Column(db.String(3), nullable=False)
    adrese = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Task %r' % self.id


class Lidmasina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelis = db.Column(db.String(200), nullable=False)
    razosanas_gads = db.Column(db.String(3), nullable=False)
    vietu_skaits = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Lidmasina %r' % self.id

class Reis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datums = db.Column(db.String(200), nullable=False)
    laiks = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Reis %r' % self.id


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

#Lidmasinas lapa
@app.route('/admin/lidmasinas', methods=['POST', 'GET'])
def lidmasina():
    if request.method == 'POST':
      new_lidmasina = Lidmasina(modelis=request.form['modelis'], razosanas_gads=request.form['razosanas_gads'], vietu_skaits=request.form['vietu_skaits'])
      try:
        db.session.add(new_lidmasina)
        db.session.commit()
        return redirect('/admin/lidmasinas')
      except:
        return "Draugi nav labi!"
    else:
      tasks = Lidmasina.query.order_by(Lidmasina.date_created).all()
      return render_template('adminlidmasinas.html', tasks=tasks)

@app.route('/delete_airplane/<int:id>')
def delete_plane(id):
    task_to_delete = Lidmasina.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/admin/lidmasinas')
    except:
        return 'Brāl nesanāca izdzēst'

@app.route('/update_lidmasinas/<int:id>', methods=['GET', 'POST'])
def update_lidmasinas(id):
    task = Lidmasina.query.get_or_404(id)
    if request.method == 'POST':
      task.modelis = request.form['modelis']
      task.razosanas_gads = request.form['razosanas_gads']
      task.vietu_skaits = request.form['vietu_skaits']
      try:
        db.session.commit()
        return redirect('/admin/lidmasinas')
      except:
        return "Brāl nesanāca update"
    else:
        return render_template("updatelidmasinas.html", task=task)

#Lidostas lapa
@app.route('/admin/lidostas', methods=['POST', 'GET'])
def lidostas():
  if request.method == 'POST':
    new_airport = Lidosta(content=request.form['content'],saisinajums = request.form['saisinajums'], adrese=request.form['adrese'])
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

#Reisu lapa
@app.route('/admin/reisi', methods=['POST', 'GET'])
def reis():
  if request.method == 'POST':
    new_reis = Reis(datums=request.form['datums'],laiks = request.form['laiks'])
    try:
      db.session.add(new_reis)
      db.session.commit()
      return redirect('/admin/reisi')
    except:
      return "Draugi nav labi!"
  else:
      tasks = Reis.query.order_by(Reis.date_created).all()
      return render_template("adminreisi.html", tasks=tasks)

@app.route('/delete_reisi/<int:id>')
def delete_reisi(id):
    task_to_delete = Reis.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/admin/reisi')
    except:
        return 'Brāl nesanāca izdzēst'

@app.route('/update_reisi/<int:id>', methods=['GET', 'POST'])
def update_reisi(id):
    task = Reis.query.get_or_404(id)
    if request.method == 'POST':
        task.datums = request.form['datums']
        task.laiks = request.form['laiks']
        try:
            db.session.commit()
            return redirect('/admin/reisi')
        except:
            return "Brāl nesanāca update"
    else:
        return render_template("updatereisi.html", task=task)

if __name__ == "__main__": 
  app.run(host='0.0.0.0', port=8000)