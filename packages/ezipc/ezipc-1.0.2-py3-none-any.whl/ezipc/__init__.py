import time
from os import path

class client:
  
  def __init__(self,**kwargs):
    
    try:self.id=kwargs['id']
    except:self.id=""
    
    try:self.time=int(kwargs['time'])
    except:self.time=0.5
    
    self.clid=0
    self.handlers = {}
  def get(self):
    time.sleep(self.time)
    with open(f"{path.dirname(__file__)}/df.txt") as df:
      cv=df.read().split("\n")
    ccid=self.clid
    evnts = []
    for ln in cv:  
      if ln=="":continue
      cvs = ln.split(":")
      cid =int(cvs[0])
      if cid>self.clid:
        if cid>ccid:
          ccid=cid
        cmg = cvs[1]
        cda = cvs[2]
        cfor = cvs[3]
        if cfor == ".ALL" or cfor == self.id:
          evnts.append([cmg,cda])
    self.clid=ccid 
    return evnts
  def send(self,msg,data,for_=".ALL"):
      id = int(time.time())
      l = f"{id}:{msg}:{data}:{for_}\n"
    
      with open(f"{path.dirname(__file__)}/df.txt","a") as df:
        df.write(l)
        df.flush()
  def clear(self):
    with open(f"{path.dirname(__file__)}/df.txt","w")as cf2:
      cf2.write("")

  def add_handler(self,event,func):
    self.handlers[event] = func
  def handler_listen(self,quit=True):
    while True:
      events = self.get()
      for event in events:
        if event[0] == "QUIT":
          break
        else:
          for evnt,fn in self.handlers.items():
            if evnt == event[0]:
              fn(event[1])
              
