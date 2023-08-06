from os import system
from sys import platform as _platform

class ShellCommands:
  def __init__(self):
    self.commands = {
                      "send"   :  self.send,
                      "clear"  :  self.clear,
                      "exit"   :  self.exit_,
                      "q"      :  self.exit_,
                      "prompt" :  self.changePrompt,
                      "set"    :  self.set_,
                      "unset"  :  self.unset_,
                      "echo"   :  self.echo,
                      "sys"    :  self.sys
                    }

    self.userVariables = {
                            "userVariables" : None
                         }

  def handleCommand(self, command):
    command = command.split(" ", 1)
    if(command[0] in self.commands):
      if(len(command) > 1):
        self.commands[command[0]](command[1])
      else:
        self.commands[command[0]]()
    else:
      print("[ERROR] Command does not exist.")
    return

  def sys(self, text = ""):
    if self.execVar and len(text):
      system(self.replaceVariables(self.unescapeVariables(text), True))
    elif len(text) > 0:
      system(self.replaceVariables(text))

  def set_(self, text = ""):
    if(len(text) > 0):
      text = text.split(" ", 1)
      if(len(text) < 2):
        print("[ERROR] Value was not given.")
      else:
        if text[1].startswith('"') and text[1].endswith('"') or text[1].startswith("'") and text[1].endswith("'"):
          text[1] = text[1][1:-1]
          text[1] = text[1].encode("utf-8")
          text[1] = text[1].decode('unicode_escape')
          self.userVariables[text[0]] = text[1]
        else:
          self.userVariables[text[0]] = text[1]
  def unset_(self, text = ""):
    if(len(text) > 0):
      if not text == "userVariables":
        if(text in self.userVariables):
          del self.userVariables[text]
        else:
          print("[ERROR] Variable does not exist")
      else:
        print("[ERROR] Cannot delete.")

  def send(self, text = ""):
    if(len(text) > 0):
      if text.startswith('"') and text.endswith('"') or text.startswith("'") and text.endswith("'"):
        text = text[1:-1]
        text = self.replaceVariables(text)
        text = text.encode("utf-8")
        text = text.decode('unicode_escape')
        self.socket.send(bytes(text, "utf-8"))
      else:
        text = self.replaceVariables(text)
        self.socket.send(bytes(text, "utf-8"))
    return

  @staticmethod
  def clear():
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
      system("clear")
    elif _platform == "win32" or _platform == "win64":
      system("cls")
    return

  def exit_(self):
    self.run = False
    self.socket.close()
    return

  def echo(self, string):
    print(self.replaceVariables(string))
    return

  def getPrompt(self):
    if(self.prompt == "coninfo"):
      r = "[" + self.ip + "@" + str(self.port) + "]>> "
    elif(self.prompt == "none"):
      r = ""
    else:
      r = self.prompt + ">> "
    return r

  def replaceVariables(self, string, onlyvar = False):
    result = ""
    i = 0
    previousVariable = False
    for word in string.split():
      if word.startswith("$"):
        key = word[1::]
        if not key == "userVariables":
          if(key in self.userVariables):
            result += self.userVariables[key]
            previousVariable = True
          else:
            print("[ERROR] Variable " + key + " is not defined.")
        else:
          result += str(self.userVariables);
      elif not onlyvar:
        if i == 0:
          result += word
        elif i < len(string.split()) and not previousVariable:
          result += " "
          result += word
        else:
          result += word
        previousVariable = False
      i += 1
    return result

  @staticmethod
  def unescapeVariables(string):
    result = ""
    i = 0

    for word in string.split():
      if word.startswith("\$"):
        var = word[1::]
        if i == 0:
          result += var
        else:
          result += " " + var
      i += 1

    return result

  def changePrompt(self, prompt = ""):
    self.prompt = self.replaceVariables(prompt)
    return