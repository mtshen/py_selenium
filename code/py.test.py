from components.event import Event

def a():
  print('1')


e = Event()



e.on('add', a)

e.trigger('add')
