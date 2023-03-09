from flask import Flask,render_template,jsonify
from database import engine
from sqlalchemy import text


app = Flask(__name__)

# jobs = [
#   {
#     'id' : 1,
#     'title' : 'Software Engineer',
#     'location': 'Kalyan',
#     'salary': 1200000
#   },
#   {
#     'id' : 2,
#     'title' : 'Data Engineer',
#     'location': 'Kalyan',
#     'salary': 1300000
#   },
#   {
#     'id' : 3,
#     'title' : 'Hardware Engineer',
#     'location': 'Kalyan',
#     'salary': 1400000
#   }
# ]

def get_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    job_openings = []
    for res in result.all():
      job_openings.append(res._asdict())
      a = res._asdict()
      print(type(a['salary']))
  return job_openings

@app.route("/")
def home():
  return render_template ('home.html',job_openings=get_jobs())




@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
