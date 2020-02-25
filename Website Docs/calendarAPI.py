from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

from oauth2client import file, client
credentials = client.AccessTokenCredentials('ACCESS_TOKEN', 'USER_AGENT')

scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console() 

service = build('calendar', 'v3', credentials=credentials)
result = service.calendarList().list().execute()

calendar_id = result['items'][0]['id']

result = service.events().list(calendarId=calendar_id).execute()
print(result['items'][0])



#!/usr/bin/python
'''
print "Content-type: text/html\n\n"
import re
import httplib2,urllib2
from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import flow_from_clientsecrets
def getCode(parameters):
    try:
            return re.search('code=(.*)',parameters).group(1)
    except:
            return False
FLOW = flow_from_clientsecrets('client_secrets.json',scope='https://www.googleapis.com/auth/calendar',redirect_uri='http://127.0.0.1/cgi-bin/py.py')

currentUrl=os.environ['REQUEST_URI']
code=getCode(currentUrl)

credentials = FLOW.step2_exchange(code)

http=httplib2.Http()
http=credentials.authorize(http)
calendar = build('calendar', 'v3', http=http)
calendar.calendarList().list().execute()
'''