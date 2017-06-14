import requests
import json
import os

ACCOUNT_NAME = os.environ.get('account_name_input')
REPO_SLUG = os.environ.get('repo_slug_input')
PR_ID = os.environ.get('pull_request_id')
APPROVED = os.environ.get('approved')

AUTH_KEY = os.environ.get('BITBUCKET_AUTH_KEY')
AUTH_SECRET = os.environ.get('BITBUCKET_AUTH_SECRET')
BITRISE_BUILD_URL = os.environ.get('BITRISE_BUILD_URL')

BB_APPROVE_ENDPOINT = 'https://api.bitbucket.org/2.0/repositories/{}/{}/pullrequests/{}/approve'
BB_COMMENT_ENDPOINT = 'https://api.bitbucket.org/1.0/repositories/{}/{}/pullrequests/{}/comments'
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
    approveURL = BB_APPROVE_ENDPOINT.format(accountName, repoSlug, PRid)
    print('Bitbucket PR Approve API URL: ' + approveURL)
    r = requests.post(approveURL, headers = header)
    if not r.ok:
        raise ValueError(r.text)
    print('The PR is Approved')

def comment(approved, accessToken, accountName, repoSlug, PRid):
    header = {'Authorization':'Bearer ' + accessToken}
    commentURL = BB_COMMENT_ENDPOINT.format(accountName, repoSlug, PRid)
    content = "The PR is passed: "
    if not approved:
        content = "The PR is failed: "

    payload = {"content": content + BITRISE_BUILD_URL}
    print('Bitbucket PR Comment API URL: ' + commentURL)
    r = requests.post(commentURL, data = payload, headers = header)
    if not r.ok:
        raise ValueError(r.text)
    print('Comment Added')

accessToken = getAccessToken(AUTH_KEY, AUTH_SECRET)

if APPROVED == 'succeeded':
    approvePR(accessToken, ACCOUNT_NAME, REPO_SLUG, PR_ID)
    comment(True, accessToken, ACCOUNT_NAME, REPO_SLUG, PR_ID)
else:
    comment(False, accessToken, ACCOUNT_NAME, REPO_SLUG, PR_ID)
