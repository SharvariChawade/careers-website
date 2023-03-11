from sqlalchemy import create_engine,text
import os

my_secret = os.environ['DB_CONNECTION_STRING']

connection_string = my_secret
engine = create_engine(connection_string,
                       connect_args=
                       {
                         "ssl":{
                           "ssl_ca": "/etc/ssl/cert.pem"
                         }
                       })

def get_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text('SELECT * FROM jobs WHERE id = :val'),
     {'val':int(id)}
    )
  r = result.all()
  if(len(r) != 0):
    r1 = r[0]._asdict()
    return r1
  elif(len(r) == 0):
    return None

def add_jobs_to_db(id,application):
  with engine.connect() as conn:
    conn.execute(text('INSERT INTO applications (job_id, full_name,email,linkedin_url,education,work_experience,resume_url) VALUES (:job, :name,:email,:linkedin,:edu,:work,:resume)'),
              {'job':int(id),
               'name':application['full_name'],
               'email':application['email'],
               'linkedin':application['linkedin'],
               'edu':application['education'],
               'work':application['experience'],
               'resume':application['resume_url']})

#Unused code
# with engine.connect() as conn:
#   result = conn.execute(text("select * from jobs"))
  # print(result.all())
  # l = result.all()
  # f = l[0]
  # job = f._asdict()
  # jobs = []
  # print(job)
  # for res in result.all():
  #   jobs.append(res._asdict())
  # print(jobs)
    