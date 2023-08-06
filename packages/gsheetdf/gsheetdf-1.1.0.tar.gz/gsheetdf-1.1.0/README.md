# gsheetdf

Export Google Sheet to Pandas dataframe

## Getting started

### Install
```
pip install gsheetdf
```

### Google credentials
Obtain a Google oauth2 or service account credential file.

If using service account authentication, ensure the service account email is added to the Google Sheet.

### Usage

```
from gsheetdf import get_service_account_credentials, export_sheet_to_dataframe

# file id (can be found in url, e.g. https://docs.google.com/spreadsheets/d/FILE_ID )
FILE_ID = "FILE_ID"

# service account credential file
SERVICE_ACCOUNT_FILE = os.path.expanduser("/path/to/keys/project-6c3bd3f37392.json")

# create credential object
credentials get_service_account_credentials(SERVICE_ACCOUNT_FILE)

# creates a pandas dataframe from the google sheet
df = export_sheet_to_dataframe(FILE_ID, credentials)

print(df.head())
```

## Appendix

### Generating google credentials

#### oauth2

* Authentication flow occurs on code execution - choose the google account that has access to the document.

##### Creating credential in Google Cloud console
https://console.cloud.google.com/apis/credentials -> Create credentials -> Oauthclient ID

Select options:
* Application type = **Other**
* Name = whatever you want
Creates and downloads credential file with name format `client_secret_xxx-xxx.apps.googleusercontent.com.json`

#### Service account
With service account authentication:
* Google Doc must be shared with the service account email
* No additional authentication step needed on code execution

##### Creating credential in google cloud console

https://console.cloud.google.com/apis/credentials -> Create credentials -> Service account key

Select options: 
* service account: App engine default service account (or custom service account if you have created one)
* Key type = JSON

Creates and downloads a credential file with name format `project-xxx.json`.
