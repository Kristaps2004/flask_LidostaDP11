from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
    content = db.Column(db.String(200), nullable=False)
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
    nolidostas = db.Column(db.String(200), nullable=False)
    uzlidostas = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Reis %r' % self.id

class Lietotajs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vards = db.Column(db.String(200), nullable=False)
    uzvards = db.Column(db.String(200), nullable=False)
    vecums = db.Column(db.String(200), nullable=False)
    dzimums = db.Column(db.String(200), nullable=False)
    tautiba = db.Column(db.String(200), nullable=False)
  
    def __repr__(self):
        return 'Lietotajs %r' % self.id

class Rezervacija(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nolidostas = db.Column(db.String(200), nullable=False)
  uzlidostas = db.Column(db.String(200), nullable=False)
  datumsno = db.Column(db.String(200), nullable=False)

  def __repr__(self):
        return 'Rezervacija %r' % self.id

@app.route('/', methods=["POST", "GET"])
def rezervacija():
  if request.method == 'POST':
    new_rezervacija = Rezervacija(nolidostas=request.form['nolidostas'],uzlidostas=request.form['uzlidostas'], datumsno=request.form['datumsno'])
    try:
      db.session.add(new_rezervacija)
      db.session.commit()
      return redirect('/izvele')
    except:
      return "Draugi nav labi!"
  else:
    lidostas = Lidosta.query.order_by(Lidosta.id).all()
    tasks = Rezervacija.query.order_by(Rezervacija.id).all()
    return render_template('index.html', tasks=tasks, lidostas=lidostas)

@app.route('/admin')
def admin():
    return render_template("admin.html")

#Izvele
@app.route('/izvele', methods=['POST', 'GET'])
def lietotajs():
  if request.method == 'POST':
    new_lietotajs = Lietotajs(vards=request.form['vards'],uzvards=request.form['uzvards'], vecums=request.form['vecums'], dzimums=request.form['dzimums'], tautiba=request.form['tautiba'])
    try:
      db.session.add(new_lietotajs)
      db.session.commit()
      return redirect('/rezervacijas')
    except:
      return "Draugi nav labi!"
  else:
    tasks = Lietotajs.query.order_by(Lietotajs.id).all()
    return render_template('izvele.html', tasks=tasks)

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
      new_lidmasina = Lidmasina(content=request.form['content'],modelis=request.form['modelis'], razosanas_gads=request.form['razosanas_gads'], vietu_skaits=request.form['vietu_skaits'])
      try:
        db.session.add(new_lidmasina)
        db.session.commit()
        return redirect('/admin/lidmasinas')
      except:
        return "Draugi nav labi!"
    else:
      lidostas = Lidosta.query.order_by(Lidosta.id).all()
      tasks = Lidmasina.query.order_by(Lidmasina.date_created).all()
      return render_template('adminlidmasinas.html', tasks=tasks, lidostas = lidostas)

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
      task.content = request.form['content']
      task.modelis = request.form['modelis']
      task.razosanas_gads = request.form['razosanas_gads']
      task.vietu_skaits = request.form['vietu_skaits']
      try:
        db.session.commit()
        return redirect('/admin/lidmasinas')
      except:
        return "Brāl nesanāca update"
    else:
        lidostas = Lidosta.query.order_by(Lidosta.id).all()
        return render_template("updatelidmasinas.html", task=task, lidostas = lidostas)

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
    new_reis = Reis(nolidostas=request.form['nolidostas'], uzlidostas=request.form['uzlidostas'], datums=request.form['datums'],laiks = request.form['laiks'])
    try:
      db.session.add(new_reis)
      db.session.commit()
      return redirect('/admin/reisi')
    except:
      return "Draugi nav labi!"
  else:
      lidostas = Lidosta.query.order_by(Lidosta.id).all()
      tasks = Reis.query.order_by(Reis.date_created).all()
      return render_template("adminreisi.html", tasks=tasks, lidostas=lidostas)

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
        task.nolidostas = request.form['nolidostas']
        task.uzlidostas = request.form['uzlidostas']
        try:
            db.session.commit()
            return redirect('/admin/reisi')
        except:
            return "Brāl nesanāca update"
    else:
        lidostas = Lidosta.query.order_by(Lidosta.id).all()
        return render_template("updatereisi.html", task=task, lidostas=lidostas)

if __name__ == "__main__": 
  app.run(host='0.0.0.0', port=8000)