import socket
import sys
import signal
from ShellCommands import *

class NWShell(ShellCommands):
  def __init__(self,
               ip,
               port,
               client,
               initial,
               recvBuff,
               interactive,
               lpersist,
               execRecv,
               execVar):

    ShellCommands.__init__(self)

    signal.signal(signal.SIGINT, self.signalHandler)

    self.ip   = ip
    self.port = port

    self.MAX_RECV_BUFF = 4096
    self.DEF_RECV_BUFF = 1024
    self.MIN_RECV_BUFF = 64

    self.recvBuff = 1024

    try:
      int(recvBuff)
    except ValueError:
      print("[ERROR] RecvBuff of value: " + recvbuff + " is invalid. Defaulting.")
    else:
      self.recvBuff = int(recvBuff)
      if(self.recvBuff > self.MAX_RECV_BUFF or self.recvBuff < self.MIN_RECV_BUFF):
        print("[ERROR] RecvBuff too large or too small.")
        self.recvBuff = self.DEF_RECV_BUFF

    self.run = True
    self.prompts = ["coninfo", "none"]
    self.prompt = "coninfo"

    self.lpersist = lpersist
    self.execRecv = execRecv
    self.execVar  = execVar

    if(client):
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      try:
        self.socket.connect((ip, port))
      except ConnectionRefusedError:
        print("[ERROR] Server is not online.")
        exit();
      else:
        self.executeInitial(initial)
      if(interactive):
        self.clientMainloop()
    else:
      self.executeInitial(initial)
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.socket.bind((ip, port))
      self.socket.listen()
      self.serverMainloop()

  def executeInitial(self, initial):
    if(len(initial) > 0):
      print("[WAIT] Executing intial commands.")
      for command in initial:
        self.handleCommand(command)
      print("[INFO] Done.\n")

  def clientMainloop(self):
    while self.run:
      self.handleCommand(input(self.getPrompt()))
    return

  def serverMainloop(self):
    try:
      conn, _ = self.socket.accept()
    except OSError:
      print("[INFO] Closing server.")
    else:
      print("[INFO] Connected to " + conn.getsockname()[0] + " on port " + str(conn.getsockname()[1]) + ".\n")
      while self.run:
        data = conn.recv(self.recvBuff)
        if not data and self.lpersist:
          print("[INFO] Disconnected from " + conn.getsockname()[0] + " on port " + str(conn.getsockname()[1]) + ".\n")
          self.serverMainloop()
        elif not data and not self.lpersist:
          break
        else:
          if not self.execRecv:
            print(conn.getsockname()[0] + "@" + str(conn.getsockname()[1]) + ">> " + str(data))
          else:
            self.handleCommand(data.decode("utf-8"))
      conn.close()

  def signalHandler(self, sig, frame):
    self.exit_()

def parseArguments():
  attributes = {
                  "ip"          : None,
                  "port"        : None,
                  "client"      : True,
                  "initial"     : [],
                  "recvbuff"    : 1024,
                  "interactive" : True,
                  "lpersist"    : False,
                  "execRecv"    : False,
                  "execVar"     : False
               }

  i = 0
  counter = 0

  for argument in sys.argv:
    counter += 1
    if(argument == "-l"):
      attributes["client"] = False
    elif(i == 0):
      #maybe add something here later
      i += 1
    elif(i == 1):
      attributes["ip"] = argument
      i += 1
    elif(i == 2):
      try:
        int(argument)
      except ValueError:
        print("[ERROR] Invalid port " + argument + ".")
        exit()
      else:
        attributes["port"] = int(argument)
        i += 1
    elif(argument == "-i" and counter < len(sys.argv)):
      attributes["initial"].append(sys.argv[counter])
    elif(argument == "-buff" and counter < len(sys.argv)):
      attributes["recvbuff"] = sys.argv[counter]
    elif(argument == "-q"):
      attributes["interactive"] = False
    elif argument == "-lp":
      attributes["lpersist"] = True
    elif argument == "-x":
      attributes["execRecv"] = True
    elif argument == "-xv":
      attributes["execVar"] = True
  return attributes