from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Texas,USA',
  'Salary': '3 LPA'
}, {
  'id': 2,
  'title': 'Data science',
  'location': 'Chennai,India',
  'Salary': '5 LPA'
}, {
  'id': 3,
  'title': 'Blockchain Developer',
  'location': 'Chennai,India',
  'Salary': '10 LPA'
}, {
  'id': 1,
  'title': 'Python Developer',
  'location': 'Chennai,India',
  'Salary': '12 LPA'
}]


@app.route("/")
def index():
  return render_template("index.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
