import os
import requests

api_key = os.environ["DEEPNOTE_API_KEY"]
project_id = os.environ['DEEPNOTE_PROJECT_ID']
notebook_id = "05fe16e1-ee0a-4da6-8e05-546ae0f7c441"
pull_id = "2af01c66-23e6-4d7f-9a73-ccbff67c2b2d"

headers = {"Authorization": f"Bearer {api_key}"}
url1 = f"https://api.deepnote.com/v1/projects/{project_id}/notebooks/{pull_id}/execute"
r = requests.post(url1, headers=headers)
print("Pull request:", r.status_code, r.text)
# now we can fire the HTTP request
url2 = (
    f"https://api.deepnote.com/v1/projects/{project_id}/notebooks/{notebook_id}/execute"
)
r = requests.post(url2, headers=headers)
print("Notebook : ", r.status_code, r.text)

