#!/usr/bin/python
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
