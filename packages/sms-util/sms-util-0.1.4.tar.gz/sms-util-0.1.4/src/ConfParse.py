#encoding:utf-8
#name:ConfigParser.py
import ConfigParser

class ConfParser(object):
    def __init__(self,confile="config.ini"):
        self.config = ConfigParser.ConfigParser()
        self.config.read(confile)
    def get(self,section, key):
        return self.config.get(section,key)
