from __future__ import print_function

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import argparse

scope = "https://www.googleapis.com/auth/spreadsheets"

class PyGsheetAPI():
  def __init__(self):
    self.store = file.Storage('credentials.json')
    self.creds = self.store.get()
    if not self.creds or self.creds.invalid:
      self.flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
      self.flow = client.flow_from_clientsecrets('credentials.json', scope)
      self.creds = tools.run_flow(self.flow, self.store)
    self.service = discovery.build('sheets', 'v4', http=self.creds.authorize(Http()))

def test():
  return 'testing'
