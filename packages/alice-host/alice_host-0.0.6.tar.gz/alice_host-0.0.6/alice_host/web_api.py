from flask import Flask,render_template
from threading import Thread
from time import sleep
import datetime
app = Flask('/')
member_view = 0
time_online = 0

def run():
  global member_view, time_online
  app.run(host='0.0.0.0',port=8080)
  while True:
    time_online = time_online+1
    sleep(1.0)

def add_view():
  global member_view, time_online
  member_view = member_view+1

@app.route('/')
def home():
  add_view()
  return render_template("host_live.html", member_view=member_view, time=str(datetime.timedelta(seconds=time_online)))
