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
    