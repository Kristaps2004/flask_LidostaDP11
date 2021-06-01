from flask import Flask, render_template
app = Flask('app')


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

app.run(host='0.0.0.0', port=8080)