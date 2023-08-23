from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


def mark_emails_as_read():
    creds = Credentials.from_authorized_user_file('credentials.json',
                                                  scopes=['https://www.googleapis.com/auth/gmail.modify'])

    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(
        userId='me', labelIds=['INBOX'], q='is:unread').execute()
    messages = results.get('messages', [])

    if not messages:
        print('No unread messages found.')
        return

    for message in messages:
        msg = service.users().messages().get(
            userId='me', id=message['id']).execute()
        msg['labelIds'] = [label for label in msg['labelIds'] if label != 'UNREAD']
        service.users().messages().modify(
            userId='me', id=message['id'], body=msg).execute()
        print(f"Marked email as read: {msg['snippet']}")


if __name__ == '__main__':
    mark_emails_as_read()
