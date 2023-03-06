from flask import Flask,render_template,jsonify


app = Flask(__name__)

jobs = [
  {
    'id' : 1,
    'title' : 'Software Engineer',
    'location': 'Kalyan',
    'salary': 1200000
  },
  {
    'id' : 2,
    'title' : 'Data Engineer',
    'location': 'Kalyan',
    'salary': 1300000
  },
  {
    'id' : 3,
    'title' : 'Hardware Engineer',
    'location': 'Kalyan',
    'salary': 1400000
  }
]

@app.route("/")
def home():
  return render_template ('home.html',jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
