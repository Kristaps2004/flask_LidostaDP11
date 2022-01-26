from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc
from flask_migrate import Migrate
from sqlalchemy import MetaData

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
_metadata = MetaData(naming_convention=convention)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app, metadata=_metadata)
migrate = Migrate(app, db, render_as_batch=True)


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


@app.route('/admin/lidmasinas', methods=['POST', 'GET'])
def lidmasina():
    if request.method == 'POST':
        new_lidmasina = Lidmasina(
            modelis=request.form['modelis'], razosanas_gads=request.form['razosanas_gads'], vietu_skaits=request.form['vietu_skaits'])
        db.session.add(new_lidmasina)
        db.session.commit()
    return render_template('adminlidmasinas.html', tasks=Lidmasina.query.all())


@ app.route('/admin/lidostas', methods=['POST', 'GET'])
def lidostas():
    if request.method == 'POST':
        new_airport = Lidosta(
            content=request.form['content'], saisinajums=request.form['saisinajums'], adrese=request.form['adrese'])
        db.session.add(new_airport)
        db.session.commit()
    return render_template('adminlidostas.html', tasks=Lidosta.query.all())


@ app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Lidosta.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/admin/lidostas')
    except:
        return 'Brāl nesanāca izdzēst'


@app.route('/delete_airport/<int:id>')
def delete_plane(id):
    remove_planes = Lidmasina.query.filter_by(id=id).first()
    db.session.delete(remove_planes)
    db.session.commit()
    return redirect(url_for('adminlidmasinas'))


@ app.route('/update/<int:id>', methods=['GET', 'POST'])
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


@ app.route('/admin/reisi')
def reisi():
    return render_template("adminreisi.html")

    app.run(host='0.0.0.0', port=8000)
