import requests
import json
import os

ACCOUNT_NAME = os.environ.get('account_name_input')
REPO_SLUG = os.environ.get('repo_slug_input')
PR_ID = os.environ.get('pull_request_id')

AUTH_KEY = os.environ.get('AUTH_KEY')
AUTH_SECRET = os.environ.get('AUTH_SECRET')

BB_API_ENDPOINT = 'https://api.bitbucket.org/2.0/repositories/{}/{}/pullrequests/{}/approve'
AUTH_ENDPOINT = 'https://{}:{}@bitbucket.org/site/oauth2/access_token'

def getAccessToken(key, Secret):
    payload = {"grant_type":"client_credentials"}
    header = {'content-type':"application/x-www-form-urlencoded"}
    authURL = AUTH_ENDPOINT.format(key, Secret)
    print('Bitbucket Auth API URL: ' + authURL)
    r = requests.post(authURL, data = payload, headers = header)
    if not r.ok:
        raise ValueError(r.text)
    print('Got access token successfully')
    return json.loads(r.text)['access_token']

def approvePR(accessToken, accountName, repoSlug, PRid):
    header = {'Authorization':'Bearer ' + accessToken}
    approveURL = BB_API_ENDPOINT.format(accountName, repoSlug, PRid)
    print('Bitbucket PR Approve API URL: ' + approveURL)
    r = requests.post(approveURL, headers = header)
    if not r.ok:
        raise ValueError(r.text)
    print('The PR is Approved')


accessToken = getAccessToken(AUTH_KEY, AUTH_SECRET)
approvePR(accessToken, ACCOUNT_NAME, REPO_SLUG, PR_ID)
