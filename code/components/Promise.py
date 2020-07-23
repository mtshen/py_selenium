class Promise:
  def __init__(self, callback):
    self.thenCall = None
    callback(self.resolve, self.reject)
    return self

  def resolve():
    self.thenCall and self.thenCall()

  def reject():


  def then(thenCall):
    self.thenCall = thenCall
