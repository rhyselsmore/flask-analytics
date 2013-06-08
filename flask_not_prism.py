class Analytics():
  
  def __init__(self, app=None):
    
    if app:
      self.init_app(app)
      
  def dont_send_to_prism(self):
    print "woop"
    
  def init_app(self, app):
    
    self.app = app
    
    app.before_request(dont_send_to_prism)
