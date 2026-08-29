import datetime
import os
import re
#from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

from stvlog import stνlαt, stναδeut, STANVOR, INVASH



def load_calendar(creds) -> str:
    """Load activities from Google calendar.."""

    try:
        #if 'service' not in globals(): Check this global statement
        service = build("calendar", "v3", credentials=creds)
        # Call the Calendar API
        now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=20,
                singleEvents=True,
                orderBy="startTime",
                ).execute()
        )
        events = events_result.get("items", [])
        if not events:
            return 'Dyαteνuα yeναq'

        # Prints the start and name of the next 10 events
        events_info = 'SHIVEN DYATEVNA\n\n'
        cal_revalues = {
            (r'\d{2}(\d{2})-(\d{2})-(\d{2})', r'\3\2\1'),
            (r'(\d{2}):(\d{2}):\d{2}-\d{2}:\d{2}', r'\1.\2'),
            (r'(\d{2})0(\d{3})', r' \1\2'),
            (r'^0(\d{4,})', r' \1'),
            (r'(\d{2}).00', r'\1   '),
            (r' 0(\d) ', r' \1  '),
        }

        for index, event in enumerate(events, start=1):
            start = event["start"].get("dateTime", event["start"].get("date"))
            start = start.replace('T', ' ')
            # Remove secs and format date and time
            # Remove leading zero from month and day
            # Remove .00 from minutes and remove leading 0 from hour

            for pattern, replacement in cal_revalues:
                start = re.sub(pattern, replacement, start)
            events_info += ' ' if index < 10 else ''
            events_info += f"{index} │ {start}    {event['summary']}\n"
        return events_info
    except HttpError as error:
        return f"An error occurred: {error}"


def calendar(logged: bool, creds, αδeutαr: int) -> str:
    """Returns name, date and time of the next 10 events on calendar."""
    #cal = calendar.TextCalendar(calendar.SUNDAY)
    #cal_month = cal.formatmonth(year, month)
    #S.υprαν = cal.formatyear(2025) + '\n\n'
    if logged and creds:
        try:
            return load_calendar(creds)
        except Exception as e:
            _ = calendar(False, creds, αδeutαr)
            return stναδeut(αδeutαr, str(e), 0)

    try:
        # If modifying these scopes, delete the file token.json.
        #load_dotenv()
        #CLIENT_ID = os.getenv(CLIENT_ID)
        client_secret_file = ''#path

        scopes = ["https://www.googleapis.com/auth/calendar.readonly"]
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", scopes)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            elif os.path.exists(client_secret_file):
                flow = InstalledAppFlow.from_client_secrets_file(
                    client_secret_file, scopes)
                creds = flow.run_local_server(port=0)
            else:
                return 'Dyαteν αqyeμreu: client_secret.json αqμerzeu'
            # Save the credentials for the next run
            with open("token.json", "w", encoding='utf8') as token:
                token.write(creds.to_json())
    except Exception as e:
        _ = stναδeut(αδeutαr, str(e), 0)
        if os.path.exists("token.json"):
            os.remove('token.json')
        calendar(True, creds, αδeutαr)  # Retry after removing token.json

    stνlαt(STANVOR, '❯ Dyevast', 0)
    return load_calendar(creds)
