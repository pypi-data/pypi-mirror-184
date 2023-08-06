from flask import Flask,render_template
from threading import Thread
from time import sleep
import datetime
app = Flask('/')
member_view = 0
time_online = 0

def run():
    app.run(host='0.0.0.0',port=8080)
def add_view():
    global member_view
    member_view = member_view+1

class Alice_Host:
  def __init__(self):
    @app.route('/')
    def home():
        global member_view
        global time_online
        add_view()
        return render_template("host_live.html", member_view=member_view, time=str(datetime.timedelta(seconds=time_online)))
    t=Thread(target=run)
    t.start()

    while True:
        global time_online
        time_online = time_online+1
        sleep(1.0)
