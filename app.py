from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 2,
  'title': 'data scientist',
  'location': 'usa',
  'salary': "Rs. 10,0000"
}, {
  'id': 2,
  'title': 'data scientist',
  'location': 'England',
  'salary': "Rs. 19,0000"
}, {
  'id': 3,
  'title': 'frontend engineer',
  'location': 'canada',
  'salary': "Rs. 15,0000"
}, {
  'id': 4,
  'title': 'backend engineer',
  'location': 'london',
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
