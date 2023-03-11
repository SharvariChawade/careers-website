from flask import Flask, render_template, jsonify, request
from database import engine, get_job_from_db, add_jobs_to_db
from sqlalchemy import text

app = Flask(__name__)


def get_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    job_openings = []
    for res in result.all():
      job_openings.append(res._asdict())
  return job_openings

#<> is used to create dynamic route
@app.route("/job/<id>")
def individual_job(id):
  job = get_job_from_db(id)
  responsibilities = []
  requirements = []
  # if(job == None):
  #   return 'no such job'
  if (job['requirements'] != None):
    requirements = job['requirements'].split(". ")
  if (job['responsiblities'] != None):
    responsibilities = job['responsiblities'].split(". ")

  return render_template('job.html',
                         job=job,
                         responsibilities=responsibilities,
                         requirements=requirements)


@app.route("/job/<id>/apply", methods=['post'])
def jobapply(id):
  data = request.form
  add_jobs_to_db(id,data)
  return render_template('submitted_application.html', application=data)


@app.route("/")
def home():
  return render_template('home.html', job_openings=get_jobs())


@app.route("/api/jobs")
def list_jobs():
  jobs = get_jobs()
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

# Unused code
# def get_job_from_db(id):
#   jobs = get_jobs()
#   for j in jobs:
#     x = j['id']
#     if f'{x}' == id:
#       return j
#   return None

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